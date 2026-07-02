# GitHub Setup Notes

This folder has been prepared as a Git-ready project folder. GitHub CLI is not currently available in the parent workspace, so remote repository creation and push need one of these options.

## Option 1: Install GitHub CLI

Install GitHub CLI, then run:

```powershell
gh auth login
cd "C:\Users\14375\Desktop\PostDoc microplastic\papers\channel MPs\channel-mps-project"
gh repo create channel-mps-project --private --source . --remote origin --push
```

Use `--public` instead of `--private` only if the data/code are ready to share publicly.

## Option 2: Create Repository in Browser

1. Create a new empty repository on GitHub.
2. Copy the repository URL.
3. Run:

```powershell
cd "C:\Users\14375\Desktop\PostDoc microplastic\papers\channel MPs\channel-mps-project"
git remote add origin https://github.com/YOUR_USER/YOUR_REPO.git
git branch -M main
git push -u origin main
```

## Recommended Privacy

Start private until the README, data licensing, author list, and publication constraints are settled.

