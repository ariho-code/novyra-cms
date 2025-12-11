# Deploying to GitHub - Step by Step Guide

## Step 1: Install Git (if not already installed)

### For Windows:
1. Download Git from: https://git-scm.com/download/win
2. Run the installer
3. Use default settings (recommended)
4. After installation, restart your terminal/PowerShell

### Verify Installation:
Open a new terminal/PowerShell and run:
```bash
git --version
```
You should see something like: `git version 2.x.x`

---

## Step 2: Configure Git (First Time Only)

Set your name and email (replace with your GitHub credentials):
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## Step 3: Initialize Git Repository

Navigate to your project folder and run:
```bash
cd "C:\Users\mujun\Desktop\novyra cms"
git init
```

---

## Step 4: Add All Files

Add all files to Git:
```bash
git add .
```

---

## Step 5: Make Your First Commit

```bash
git commit -m "Initial commit: Novyra CMS project"
```

---

## Step 6: Create GitHub Repository

### Option A: Using GitHub Website
1. Go to https://github.com
2. Click the "+" icon in the top right
3. Select "New repository"
4. Repository name: `novyra-cms` (or any name you prefer)
5. Description: "Novyra CMS - Content Management System"
6. Choose **Public** or **Private**
7. **DO NOT** initialize with README, .gitignore, or license (we already have these)
8. Click "Create repository"

### Option B: Using GitHub CLI (if installed)
```bash
gh repo create novyra-cms --public --source=. --remote=origin --push
```

---

## Step 7: Connect Local Repository to GitHub

After creating the repository on GitHub, you'll see instructions. Use these commands:

```bash
# Add GitHub as remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/novyra-cms.git

# Or if you prefer SSH (requires SSH key setup):
# git remote add origin git@github.com:YOUR_USERNAME/novyra-cms.git
```

---

## Step 8: Push to GitHub

```bash
# Push to main branch
git branch -M main
git push -u origin main
```

If prompted for credentials:
- **Username**: Your GitHub username
- **Password**: Use a Personal Access Token (not your GitHub password)
  - Generate token: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
  - Select scopes: `repo` (full control of private repositories)
  - Copy the token and use it as password

---

## Step 9: Verify Upload

1. Go to your GitHub repository page
2. You should see all your files
3. Check that sensitive files (like `.env`, `db.sqlite3`) are NOT visible

---

## Common Commands for Future Updates

### Check status:
```bash
git status
```

### Add specific files:
```bash
git add filename.py
```

### Add all changes:
```bash
git add .
```

### Commit changes:
```bash
git commit -m "Description of your changes"
```

### Push to GitHub:
```bash
git push
```

### Pull latest changes (if working on multiple machines):
```bash
git pull
```

---

## Troubleshooting

### "Git is not recognized"
- Install Git from https://git-scm.com/download/win
- Restart your terminal after installation

### "Authentication failed"
- Use Personal Access Token instead of password
- Generate token: GitHub → Settings → Developer settings → Personal access tokens

### "Repository not found"
- Check repository name and username are correct
- Ensure repository exists on GitHub

### "Large file" errors
- Check `.gitignore` includes `media/` and `db.sqlite3`
- If needed, remove large files: `git rm --cached largefile.ext`

---

## Next Steps After GitHub Upload

1. **Deploy to Render**: Follow `RENDER_DEPLOYMENT.md`
2. **Set up CI/CD**: Automate deployments
3. **Add README.md**: Document your project
4. **Add LICENSE**: Choose a license for your project

