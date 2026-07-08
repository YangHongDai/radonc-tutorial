[CmdletBinding()]
param(
    [string]$Owner = "YangHongDai",
    [string]$RepoName = "radonc-tutorial",
    [string]$ProjectPath,
    [string]$DefaultBranch = "main",
    [string]$CommitMessage = "Initial GitHub publish",
    [string]$Description = "Radiation Oncology Interactive Tutorial",
    [string]$GitUserName,
    [string]$GitUserEmail,
    [string]$GitHubToken = $env:GITHUB_TOKEN,
    [switch]$CreateRepo,
    [switch]$Private,
    [switch]$OpenCreatePage,
    [switch]$OverwriteOrigin,
    [switch]$SkipPush
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Write-Step {
    param([string]$Message)
    Write-Host ""
    Write-Host "==> $Message" -ForegroundColor Cyan
}

function Invoke-Git {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$Args,
        [switch]$AllowFailure
    )

    function Format-Argument {
        param([string]$Value)

        if ($null -eq $Value) {
            return '""'
        }

        if ($Value -notmatch '[\s"]') {
            return $Value
        }

        $escaped = $Value -replace '(\\*)"', '$1$1\"'
        $escaped = $escaped -replace '(\\+)$', '$1$1'
        return '"' + $escaped + '"'
    }

    $stdoutPath = [System.IO.Path]::GetTempFileName()
    $stderrPath = [System.IO.Path]::GetTempFileName()
    try {
        $argumentLine = ($Args | ForEach-Object { Format-Argument $_ }) -join " "
        $process = Start-Process -FilePath "git" -ArgumentList $argumentLine -NoNewWindow -Wait -PassThru -RedirectStandardOutput $stdoutPath -RedirectStandardError $stderrPath
        $stdout = if (Test-Path $stdoutPath) { Get-Content -LiteralPath $stdoutPath -Raw -ErrorAction SilentlyContinue } else { "" }
        $stderr = if (Test-Path $stderrPath) { Get-Content -LiteralPath $stderrPath -Raw -ErrorAction SilentlyContinue } else { "" }
        $parts = @()
        if (-not [string]::IsNullOrWhiteSpace($stdout)) { $parts += $stdout.Trim() }
        if (-not [string]::IsNullOrWhiteSpace($stderr)) { $parts += $stderr.Trim() }
        $output = $parts -join [Environment]::NewLine
        $exitCode = $process.ExitCode
    } finally {
        Remove-Item -LiteralPath $stdoutPath, $stderrPath -Force -ErrorAction SilentlyContinue
    }

    if (-not $AllowFailure -and $exitCode -ne 0) {
        $text = ($output | Out-String).Trim()
        if ([string]::IsNullOrWhiteSpace($text)) {
            $text = "git $($Args -join ' ') failed with exit code $exitCode."
        }
        throw $text
    }

    return [pscustomobject]@{
        ExitCode = $exitCode
        Output   = ($output | Out-String).Trim()
    }
}

function Get-GitConfigValue {
    param([string]$Key)

    $result = Invoke-Git -Args @("config", "--get", $Key) -AllowFailure
    if ($result.ExitCode -ne 0) {
        return $null
    }
    return $result.Output
}

function Ensure-GitIdentity {
    param(
        [string]$UserName,
        [string]$UserEmail
    )

    if ($UserName) {
        Invoke-Git -Args @("config", "user.name", $UserName) | Out-Null
    }

    if ($UserEmail) {
        Invoke-Git -Args @("config", "user.email", $UserEmail) | Out-Null
    }

    $resolvedName = Get-GitConfigValue "user.name"
    $resolvedEmail = Get-GitConfigValue "user.email"

    if ([string]::IsNullOrWhiteSpace($resolvedName) -or [string]::IsNullOrWhiteSpace($resolvedEmail)) {
        throw @"
Git user.name / user.email is not configured.

Run one of these, then rerun the script:
  git config --global user.name "Your Name"
  git config --global user.email "you@example.com"

Or pass:
  -GitUserName "Your Name" -GitUserEmail "you@example.com"
"@
    }
}

function Ensure-GitInstalled {
    if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
        throw "Git is not installed or not on PATH."
    }
}

function Ensure-GitHubRepo {
    param(
        [string]$OwnerName,
        [string]$Name,
        [string]$RepoDescription,
        [bool]$IsPrivate,
        [string]$Token
    )

    if ([string]::IsNullOrWhiteSpace($Token)) {
        throw "CreateRepo was requested, but no GitHub token was provided. Set GITHUB_TOKEN or pass -GitHubToken."
    }

    $headers = @{
        Authorization         = "Bearer $Token"
        Accept                = "application/vnd.github+json"
        "X-GitHub-Api-Version" = "2022-11-28"
    }

    $repoApi = "https://api.github.com/repos/$OwnerName/$Name"
    try {
        Invoke-RestMethod -Method Get -Uri $repoApi -Headers $headers | Out-Null
        Write-Host "GitHub repo already exists: $OwnerName/$Name" -ForegroundColor Yellow
        return
    } catch {
        $statusCode = $_.Exception.Response.StatusCode.value__
        if ($statusCode -ne 404) {
            throw
        }
    }

    $body = @{
        name        = $Name
        description = $RepoDescription
        private     = $IsPrivate
    } | ConvertTo-Json

    Invoke-RestMethod -Method Post -Uri "https://api.github.com/user/repos" -Headers $headers -Body $body | Out-Null
    Write-Host "Created GitHub repo: $OwnerName/$Name" -ForegroundColor Green
}

Ensure-GitInstalled

$scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($ProjectPath)) {
    $ProjectPath = Join-Path $scriptDir ".."
}

$resolvedProjectPath = (Resolve-Path $ProjectPath).Path
$remoteUrl = "https://github.com/$Owner/$RepoName.git"
$createPageUrl = "https://github.com/new?owner=$Owner&name=$RepoName"

Push-Location $resolvedProjectPath
try {
    Write-Step "Working in $resolvedProjectPath"

    if (-not (Test-Path ".git")) {
        Write-Step "Initializing Git repository"
        Invoke-Git -Args @("init") | Out-Null
    }

    Ensure-GitIdentity -UserName $GitUserName -UserEmail $GitUserEmail

    Write-Step "Setting default branch to $DefaultBranch"
    Invoke-Git -Args @("branch", "-M", $DefaultBranch) | Out-Null

    Write-Step "Staging files"
    Invoke-Git -Args @("add", "-A") | Out-Null

    $status = Invoke-Git -Args @("status", "--porcelain")
    $hasHead = (Invoke-Git -Args @("rev-parse", "--verify", "HEAD") -AllowFailure).ExitCode -eq 0

    if (-not [string]::IsNullOrWhiteSpace($status.Output) -or -not $hasHead) {
        Write-Step "Creating commit"
        Invoke-Git -Args @("commit", "-m", $CommitMessage) | Out-Null
    } else {
        Write-Host "No new changes to commit." -ForegroundColor Yellow
    }

    $origin = Invoke-Git -Args @("remote", "get-url", "origin") -AllowFailure
    if ($origin.ExitCode -ne 0) {
        Write-Step "Adding origin remote"
        Invoke-Git -Args @("remote", "add", "origin", $remoteUrl) | Out-Null
    } elseif ($origin.Output -ne $remoteUrl) {
        if ($OverwriteOrigin) {
            Write-Step "Updating origin remote"
            Invoke-Git -Args @("remote", "set-url", "origin", $remoteUrl) | Out-Null
        } else {
            throw "Origin already points to '$($origin.Output)'. Re-run with -OverwriteOrigin if you want to replace it with '$remoteUrl'."
        }
    }

    if ($CreateRepo) {
        Write-Step "Ensuring GitHub repo exists"
        Ensure-GitHubRepo -OwnerName $Owner -Name $RepoName -RepoDescription $Description -IsPrivate:$Private.IsPresent -Token $GitHubToken
    } elseif ($OpenCreatePage) {
        Write-Step "Opening GitHub create-repo page"
        Start-Process $createPageUrl
        Write-Host "Create an empty repo named '$RepoName' under '$Owner', then rerun this script." -ForegroundColor Yellow
        return
    }

    if ($SkipPush) {
        Write-Host ""
        Write-Host "Local Git repo is ready. Push skipped by request." -ForegroundColor Green
        Write-Host "Remote configured as: $remoteUrl"
        return
    }

    Write-Step "Pushing to GitHub"
    try {
        Invoke-Git -Args @("push", "-u", "origin", $DefaultBranch) | Out-Null
    } catch {
        Write-Host ""
        Write-Host "Push failed." -ForegroundColor Red
        Write-Host "If the repo does not exist yet, create it here:" -ForegroundColor Yellow
        Write-Host "  $createPageUrl"
        Write-Host ""
        Write-Host "If GitHub asks for authentication, sign in through Git Credential Manager or use a Personal Access Token." -ForegroundColor Yellow
        throw
    }

    Write-Host ""
    Write-Host "Publish complete: $remoteUrl" -ForegroundColor Green
} finally {
    Pop-Location
}
