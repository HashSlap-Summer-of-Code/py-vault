# Git Basics Tutorial - Beginner Friendly Guide

Welcome to the **Git Basics Tutorial**, a beginner-friendly guide that walks you through essential Git and GitHub commands and workflows. This guide is designed to help new developers understand how Git works and how to contribute to repositories using common commands.

## 🚀 Overview

This tutorial introduces key Git commands used in daily development workflows. Whether you're managing your own project or contributing to open source, this guide will boost your confidence in using Git effectively.

> ✅ **Tip:** If you're a visual learner, consider checking out this Git workflow infographic or animated GIF: ![Git Workflow](git-workflow.gif)

---

## 📘 Common Git Commands & Explanation

| Command                             | Description                                                                                               |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `git diff`                          | Installed Git to a directory and made some changes to a file, then shows file differences not yet staged. |
| `git push` | Upload local repository changes to a remote repository. |
| `git pull` | Download changes from remote repository and merge them. |
| `git clone <url>` | Create a local copy of a remote repository. |
| `git init` | Initialize a new Git repository in the current directory. |
| `git log` | Display the commit history for the current branch. |
| `git merge <branch>` | Merge changes from another branch into current branch. |
| `git fetch` | Download changes from remote repository without merging. |
| `git reset <file>` | Remove file from staging area (unstage changes). |
| `git rm <file>` | Remove file from repository and working directory. |
| `git branch` | List all branches or create a new branch. |
| `git branch -d <branch>` | Delete a local branch safely. |
| `git remote -v` | Show remote repository URLs. |
| `git stash` | Temporarily save changes without committing. |
| `git stash pop` | Apply most recent stashed changes. |

---

## 🌟 GitHub Workflow for Beginners

### Step 1: Fork a Repository
When contributing to open source projects, start by forking the repository to your GitHub account.

```bash
# Click "Fork" button on GitHub website
# This creates a copy of the repository in your account
```

### Step 2: Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
cd REPOSITORY_NAME
```

### Step 3: Create a New Branch
Always create a new branch for your changes:
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

### Step 4: Make Your Changes
Edit files, add features, or fix bugs as needed.

### Step 5: Stage and Commit Changes
```bash
git add .                                    # Stage all changes
git add specific-file.txt                    # Stage specific file
git commit -m "Add: Brief description of changes"
```

### Step 6: Push Changes to Your Fork
```bash
git push origin feature/your-feature-name
```

### Step 7: Create a Pull Request
1. Go to your fork on GitHub
2. Click "New Pull Request"
3. Write a clear description of your changes
4. Submit the pull request

---

## 🔧 Practical Examples

### Example 1: Starting a New Project
```bash
mkdir my-project
cd my-project
git init
echo "# My Project" >> README.md
git add README.md
git commit -m "Initial commit: Add README"
```

### Example 2: Working with Remote Repository
```bash
git remote add origin https://github.com/username/repository.git
git push -u origin main
```

### Example 3: Collaboration Workflow
```bash
git pull origin main                    # Get latest changes
git checkout -b feature/new-feature    # Create feature branch
# Make your changes...
git add .
git commit -m "Add new feature"
git push origin feature/new-feature    # Push to remote
# Create Pull Request on GitHub
```

---

## 🚨 Common Git Commands for Troubleshooting

| Problem | Solution |
|---------|----------|
| Undo last commit (keep changes) | `git reset --soft HEAD~1` |
| Undo last commit (discard changes) | `git reset --hard HEAD~1` |
| Fix commit message | `git commit --amend -m "New message"` |
| Discard changes in working directory | `git checkout -- <filename>` |
| View differences before staging | `git diff` |
| View differences after staging | `git diff --staged` |
| Unstage a file | `git reset HEAD <filename>` |
| Delete untracked files | `git clean -f` |

---

## 📚 Git Best Practices

### Commit Message Guidelines
- **Use present tense**: "Add feature" not "Added feature"
- **Be descriptive**: Explain what and why, not how
- **Keep first line under 50 characters**
- **Use conventional prefixes**:
  - `Add:` for new features
  - `Fix:` for bug fixes
  - `Update:` for changes to existing features
  - `Remove:` for deletions
  - `Docs:` for documentation changes

### Branch Naming Conventions
- `feature/feature-name` - for new features
- `fix/bug-description` - for bug fixes
- `hotfix/critical-fix` - for urgent fixes
- `docs/documentation-update` - for documentation
- `refactor/code-improvement` - for code refactoring

### General Best Practices
1. **Commit frequently** with small, logical changes
2. **Write clear commit messages** that explain the "why"
3. **Test before committing** to avoid broken code
4. **Use branches** for different features or experiments
5. **Keep your fork updated** with the original repository
6. **Review your changes** before pushing

---

## 🎯 Quick Reference Card

### Most Used Commands (Daily Workflow)
```bash
git status          # Check current status
git add .           # Stage all changes
git commit -m "msg" # Commit with message
git push            # Push to remote
git pull            # Pull from remote
git checkout -b br  # Create and switch branch
git merge branch    # Merge branch
git log --oneline   # View commit history
```

### Emergency Commands
```bash
git stash           # Save work temporarily
git reset --hard    # Discard all changes
git clean -fd       # Remove untracked files/dirs
git reflog          # View reference log (recovery)
```

---

## 🏆 Conclusion

Congratulations! You now have a solid foundation in Git and GitHub basics. This tutorial covered:

- ✅ Essential Git commands and their purposes
- ✅ GitHub workflow for open source contribution  
- ✅ Practical examples and use cases
- ✅ Troubleshooting common issues
- ✅ Best practices for clean Git history
- ✅ Quick reference for daily use

### Next Steps
1. **Practice** these commands on a test repository
2. **Contribute** to open source projects
3. **Explore** advanced Git features like rebasing and cherry-picking
4. **Join** developer communities to learn from others

### Additional Resources
- [Official Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)
- [Pro Git Book (Free)](https://git-scm.com/book)

---

**Happy coding and contributing! 🚀**

> **Note**: Remember that Git is a powerful tool that becomes more intuitive with practice. Don't be afraid to experiment in test repositories, and always make backups of important work.| `git status`                        | Illustrates the state of the directory that you are currently in dynamically.                             |
| `git add file_path`                 | Save changes made in files and add those file(s) to the staging area.                                     |
| `git checkout -b branch_name`       | Create and switch to a new branch.                                                                        |
| `git checkout branch_name`          | Switch to an existing branch.                                                                             |
| `git commit --amend`                | Amend the last commit (e.g., update message or files).                                                    |
| `git push origin branch_name`       | Push local changes to the remote repository.                                                              |
| `git pull`                          | Retrieve more changes from a remote repository and merge them.                                            |
| `git rebase -i`                     | Reorder, squash, or modify commits in a branch's history.                                                 |
| `git clone`                         | Clone a remote repository to your local system.                                                           |
| `git merge`                         | Merge changes from one branch into another.                                                               |
| `git log --stat`                    | Show commit history with statistics (lines added/removed).                                                |
| `git stash`                         | Temporarily shelve changes you don’t want to commit yet.                                                  |
| `git stash pop`                     | Reapply stashed changes to your working directory.                                                        |
| `git show commit_id`                | Display information about a specific commit.                                                              |
| `git reset HEAD~1`                  | Undo the most recent commit while retaining local changes.                                                |
| `git format-patch -1 commit_id`     | Create a patch file of a specific commit.                                                                 |
| `git apply patch_file_name`         | Apply changes from a patch file.                                                                          |
| `git branch -D branch_name`         | Delete a branch forcefully.                                                                               |
| `git reset`                         | Revert changes by moving the branch reference.                                                            |
| `git revert`                        | Revert changes by creating a new commit.                                                                  |
| `git cherry-pick commit_id`         | Apply changes from a unique commit onto the current branch.                                               |
| `git branch`                        | Lists all the branches in your repo.                                                                      |
| `git reset --hard`                  | Discards all changes to tracked files since the last commit.                                              |

---

## 📌 Best Practices

* Always create a new branch for your changes (`git checkout -b my-feature`)
* Write meaningful commit messages
* Use `git pull --rebase` to avoid unnecessary merge commits
* Use `.gitignore` to exclude unwanted files



## 📂 Contribution Workflow

1. **Fork** the repository on GitHub
2. **Clone** your forked repo to your local machine
3. **Create a branch** for your feature: `git checkout -b feature-name`
4. Make your changes ✅
5. **Stage & commit** your changes: `git add . && git commit -m "Added feature"`
6. **Push** your branch: `git push origin feature-name`
7. Create a **Pull Request** from GitHub



## 🔗 Useful Links

* [Git Official Documentation](https://git-scm.com/doc)
* [GitHub Docs](https://docs.github.com/en)
* [Git Cheatsheet PDF](https://education.github.com/git-cheat-sheet-education.pdf)

