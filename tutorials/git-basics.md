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
| `git commit -a -m "commit message"` | Save all the tracked changes with a comment.                                                              |
| `git status`                        | Illustrates the state of the directory that you are currently in dynamically.                             |
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

