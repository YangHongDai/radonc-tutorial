#!/usr/bin/env bash

set -euo pipefail

# Usage:
#   ./update-and-push.sh
#   ./update-and-push.sh "Update website content"
#
# Run this script from inside your existing Git repository.
# It does not create a new repository or change the origin URL.
chmod +x update-and-push.sh
COMMIT_MESSAGE="${1:-Update website content $(date '+%Y-%m-%d %H:%M')}"

fail() {
  echo
  echo "Error: $1" >&2
  exit 1
}

echo "Checking Git repository..."

git rev-parse --is-inside-work-tree >/dev/null 2>&1 \
  || fail "This folder is not a Git repository. Run the script inside your project repository."

BRANCH="$(git branch --show-current)"
[[ -n "$BRANCH" ]] || fail "Detached HEAD detected. Check out a branch before pushing."

git remote get-url origin >/dev/null 2>&1 \
  || fail "No 'origin' remote is configured."

ORIGIN_URL="$(git remote get-url origin)"

echo "Repository: $(pwd)"
echo "Branch:     $BRANCH"
echo "Origin:     $ORIGIN_URL"

# GitHub no longer accepts account passwords for HTTPS Git operations.
# Use GitHub CLI to configure token-based authentication.
if [[ "$ORIGIN_URL" == https://github.com/* ]]; then
  if ! command -v gh >/dev/null 2>&1; then
    cat >&2 <<'EOF'

GitHub CLI is required for easy HTTPS authentication.

Install it on macOS with:
  brew install gh

Then run:
  gh auth login
  gh auth setup-git

After that, run this script again.
EOF
    exit 1
  fi

  if ! gh auth status >/dev/null 2>&1; then
    echo
    echo "GitHub CLI is not authenticated."
    echo "Starting browser-based GitHub login..."
    gh auth login
  fi

  gh auth setup-git
fi

echo
echo "Current changes:"
git status --short

echo
echo "Synchronizing with origin/$BRANCH..."
git pull --rebase --autostash origin "$BRANCH"

echo
echo "Staging all changes..."
git add -A

if git diff --cached --quiet; then
  echo "No new file changes to commit."
else
  echo
  echo "Creating commit:"
  echo "  $COMMIT_MESSAGE"
  git commit -m "$COMMIT_MESSAGE"
fi

echo
echo "Pushing to origin/$BRANCH..."
git push -u origin "$BRANCH"

echo
echo "Done. Updates were pushed successfully."
