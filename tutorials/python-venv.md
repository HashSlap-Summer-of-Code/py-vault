# Python Virtual Environments

A virtual environment is a self-contained directory that contains a Python installation and dependencies for a specific project.

---

## 🔧 Why Use Virtual Environments?

- Isolate dependencies per project
- Avoid version conflicts
- Reproducible environments for teams

---

## 🚀 How to Create a Virtual Environment

```bash
python -m venv env


✅ How to Activate It

On Windows:

.\env\Scripts\activate


On macOS/Linux:

source env/bin/activate


💡 Best Practices

Use a virtual environment per project
Add env/ to .gitignore

Freeze dependencies using:
pip freeze > requirements.txt

To install them:
pip install -r requirements.txt

❌ Deactivating and Removing

deactivate     # exit virtual environment
rm -rf env     # delete the environment folder
