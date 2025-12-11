# Git Configuration Script for Novyra CMS
# Run this script to configure Git with your GitHub credentials

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Git Configuration for Novyra CMS" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Refresh PATH to include Git
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Verify Git is available
try {
    $gitVersion = git --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Error: Git is not installed or not in PATH." -ForegroundColor Red
        Write-Host "Please install Git from https://git-scm.com/download/win" -ForegroundColor Yellow
        exit 1
    }
} catch {
    Write-Host "Error: Git is not installed or not in PATH." -ForegroundColor Red
    Write-Host "Please install Git from https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}

# Get user information
$userName = Read-Host "Enter your GitHub username (or your full name)"
$userEmail = Read-Host "Enter your GitHub email address"

# Configure Git
git config --global user.name "$userName"
git config --global user.email "$userEmail"

Write-Host ""
Write-Host "Git configured successfully!" -ForegroundColor Green
Write-Host "Name: $userName" -ForegroundColor Yellow
Write-Host "Email: $userEmail" -ForegroundColor Yellow
Write-Host ""
Write-Host "You can now proceed with making commits." -ForegroundColor Green

