[CmdletBinding()]
param(
    [string]$ProjectPath,
    [string]$CommitMessage = "Update project content",
    [string]$Branch,
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

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git is not installed or not on PATH."
}

$scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($ProjectPath)) {
    $ProjectPath = Join-Path $scriptDir ".."
}

$resolvedProjectPath = (Resolve-Path $ProjectPath).Path

Push-Location $resolvedProjectPath
try {
    if (-not (Test-Path ".git")) {
        throw "No Git repository found in $resolvedProjectPath. Run scripts\publish-to-github.ps1 first."
    }

    $origin = Invoke-Git -Args @("remote", "get-url", "origin") -AllowFailure
    if ($origin.ExitCode -ne 0) {
        throw "No origin remote is configured. Run scripts\publish-to-github.ps1 first."
    }

    if (-not $Branch) {
        $Branch = (Invoke-Git -Args @("branch", "--show-current")).Output
        if ([string]::IsNullOrWhiteSpace($Branch)) {
            $Branch = "main"
        }
    }

    Write-Step "Staging files"
    Invoke-Git -Args @("add", "-A") | Out-Null

    $status = Invoke-Git -Args @("status", "--porcelain")
    if ([string]::IsNullOrWhiteSpace($status.Output)) {
        Write-Host "No changes to commit." -ForegroundColor Yellow
        return
    }

    Write-Step "Creating commit"
    Invoke-Git -Args @("commit", "-m", $CommitMessage) | Out-Null

    if ($SkipPush) {
        Write-Host "Commit created. Push skipped by request." -ForegroundColor Green
        return
    }

    Write-Step "Pushing to $Branch"
    Invoke-Git -Args @("push", "origin", $Branch) | Out-Null
    Write-Host "Push complete." -ForegroundColor Green
} finally {
    Pop-Location
}
