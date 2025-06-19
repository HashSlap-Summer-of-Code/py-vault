

# 🧠 Git Basics for Beginners

Welcome to your first step into the world of **Git** and **GitHub**!  




## 📦 What is Git? What is GitHub?

> 🔧 **Git** is a *version control system* — like a time machine for your code.  
> ☁️ **GitHub** is a *cloud platform* that stores your Git repositories online and makes collaboration easy.

| Tool      | Purpose                        |
|-----------|--------------------------------|
| Git       | Track versions locally         |
| GitHub    | Host your Git repositories     |


## 🔧 Getting Started

### 1️⃣ Install Git

- 🪟 Windows: https://git-scm.com/download/win  
- 🍎 macOS: https://git-scm.com/download/mac  
- 🐧 Linux: `sudo apt install git`

### 2️⃣ Configure Git (Run once after installation)


git config --global user.name "Your Name"
git config --global user.email "your@email.com"


## 🚀 Git Workflow (Visual)

```plaintext
Working Directory → Staging Area → Local Repository → Remote Repository (GitHub)
         |                |                |
         |                |                |
         ↓                ↓                ↓
      git add         git commit       git push




## ⚙️ Most Useful Git Commands

| Command                   | Description                          |
| ------------------------- | ------------------------------------ |
| `git init`                | Initialize a new Git repository      |
| `git clone <repo-url>`    | Clone an existing repo from GitHub   |
| `git status`              | Show the current state of your files |
| `git add .`               | Stage all changes                    |
| `git commit -m "message"` | Commit staged changes                |
| `git push origin main`    | Push changes to GitHub               |
| `git pull origin main`    | Pull the latest from GitHub          |
| `git branch <name>`       | Create a new branch                  |
| `git checkout <name>`     | Switch to another branch             |
| `git merge <branch>`      | Merge a branch into current branch   |

---



git checkout -b new-feature    # Create and switch to a branch
... (make changes)
git add .                       #this adds all files
git commit -m "Add feature"
git checkout main              # Go back to main
git merge new-feature          # Merge feature branch
```

---

## 📘 Sample Workflow Summary


# Step 1: Clone the repo
git clone https://github.com/yourusername/yourrepo.git

# Step 2: Work on a new branch
git checkout -b my-new-feature

# Step 3: Make changes, stage, and commit
git add .
git commit -m "Add something cool"

# Step 4: Push the branch to GitHub
git push origin my-new-feature

# Step 5: Create a Pull Request (PR) on GitHub
```

---

## 🧪 Practice Exercise

Try this on your own machine:

1. Create a folder and run `git init`
2. Create a file named `hello.txt` and add some text
3. Use `git add .` and `git commit -m "First commit"`
4. Push it to a new repo on GitHub

---

## 🧠 Pro Tips

* ✅ Commit often with meaningful messages.
* ❌ Don’t commit `.env`, API keys, or sensitive files.
* 🌀 Use `.gitignore` to exclude unnecessary files.
* 🧼 Use `git status` and `git log` to stay in control.

---

## 📚 Additional Resources

* 📝 [GitHub Docs](https://docs.github.com/en/get-started)
* 🧾 [Git Cheatsheet PDF](https://education.github.com/git-cheat-sheet-education.pdf)
* 🎥 [Git & GitHub for Beginners (Video)](https://www.youtube.com/watch?v=RGOj5yH7evk)
