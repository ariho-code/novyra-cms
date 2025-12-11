# Push to GitHub - Quick Guide

## ✅ What's Already Done
- ✅ Git installed and configured
- ✅ Repository initialized
- ✅ Initial commit created (149 files)
- ✅ Git configured with:
  - Username: `ariho-code`
  - Email: `arihotimothy89@gmail.com`

## 🚀 Next Steps: Push to GitHub

### Step 1: Create GitHub Repository

1. Go to https://github.com and sign in
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in the details:
   - **Repository name**: `novyra-cms` (or any name you prefer)
   - **Description**: `Novyra CMS - Content Management System`
   - **Visibility**: Choose **Public** or **Private**
   - ⚠️ **IMPORTANT**: Do NOT check:
     - ❌ Add a README file
     - ❌ Add .gitignore
     - ❌ Choose a license
   - (We already have these files)
5. Click **"Create repository"**

### Step 2: Connect and Push

After creating the repository, GitHub will show you commands. Use these:

**Copy and paste these commands in your PowerShell** (replace `YOUR_USERNAME` with `ariho-code` if different):

```powershell
# Refresh PATH (needed in new PowerShell sessions)
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Add GitHub as remote (replace ariho-code if your username is different)
git remote add origin https://github.com/ariho-code/novyra-cms.git

# Rename branch to main (GitHub standard)
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 3: Authentication

When you run `git push`, you'll be prompted for credentials:

- **Username**: `ariho-code`
- **Password**: Use a **Personal Access Token** (NOT your GitHub password)

#### How to Create Personal Access Token:

1. Go to GitHub → Click your profile picture (top right)
2. Click **Settings**
3. Scroll down → Click **Developer settings**
4. Click **Personal access tokens** → **Tokens (classic)**
5. Click **Generate new token** → **Generate new token (classic)**
6. Fill in:
   - **Note**: `Novyra CMS Deployment`
   - **Expiration**: Choose duration (90 days recommended)
   - **Select scopes**: Check ✅ **`repo`** (Full control of private repositories)
7. Click **Generate token**
8. **COPY THE TOKEN IMMEDIATELY** (you won't see it again!)
9. Use this token as your password when pushing

### Step 4: Verify Upload

1. Go to your repository: `https://github.com/ariho-code/novyra-cms`
2. You should see all your files
3. Verify that sensitive files are NOT visible:
   - ✅ `db.sqlite3` should NOT be there
   - ✅ `media/` folder should NOT be there
   - ✅ `.env` files should NOT be there

## 🔄 Future Updates

After the initial push, to update your GitHub repository:

```powershell
# Refresh PATH (if in new session)
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Check what changed
git status

# Add all changes
git add .

# Commit changes
git commit -m "Description of your changes"

# Push to GitHub
git push
```

## 🐛 Troubleshooting

### "Git is not recognized"
**Solution**: Refresh PATH in your PowerShell session:
```powershell
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
```

### "Authentication failed"
**Solution**: 
- Make sure you're using a Personal Access Token, not your GitHub password
- Generate a new token if needed

### "Repository not found"
**Solution**: 
- Check the repository name matches exactly
- Ensure the repository exists on GitHub
- Verify your username is correct

### "Large file" errors
**Solution**: 
- Check `.gitignore` includes `media/` and `db.sqlite3`
- If a large file was already committed, remove it:
  ```powershell
  git rm --cached largefile.ext
  git commit -m "Remove large file"
  git push
  ```

## 📝 Quick Reference

```powershell
# Always refresh PATH first (in new sessions)
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Check status
git status

# Add files
git add .

# Commit
git commit -m "Your message"

# Push
git push
```

## ✅ Success Checklist

- [ ] GitHub repository created
- [ ] Remote added (`git remote add origin ...`)
- [ ] Branch renamed to main (`git branch -M main`)
- [ ] Personal Access Token created
- [ ] Code pushed successfully (`git push -u origin main`)
- [ ] Files visible on GitHub
- [ ] Sensitive files NOT visible (db.sqlite3, media/, .env)

---

**Need help?** Check `GITHUB_DEPLOYMENT.md` for more detailed instructions.

