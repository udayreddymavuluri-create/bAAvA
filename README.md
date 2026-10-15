# 💛 A Little Appreciation — Brother-in-Law Edition

A small, personalized Streamlit app made to celebrate a brother-in-law with heartfelt messages, family appreciation, memories, and a little friendly sarcasm.

## Features

- Personalize the page with his name and your name
- Share a meaningful appreciation message
- Generate random heartfelt notes and lighthearted jokes
- Add a favorite memory
- Responsive, dark navy and gold design

## Run locally

### 1. Open the project in VS Code

Unzip the project, then open the `brother-in-law-app` folder in VS Code using **File → Open Folder**.

### 2. Create a virtual environment (recommended)

On macOS, open **Terminal → New Terminal** in VS Code and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 4. Launch the app

```bash
python3 -m streamlit run app.py
```

Streamlit will show a local URL, usually `http://localhost:8501`. Open it in your browser.

## Push to GitHub

Create a **new, empty repository** on GitHub (for example, `brother-in-law-app`). Do not add a README or `.gitignore` on GitHub because this project already includes them.

In the VS Code terminal, from this project folder, run:

```bash
git init
git add .
git commit -m "Create brother-in-law appreciation app"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/brother-in-law-app.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. If Git asks you to sign in, follow the browser authentication prompt. Never put passwords or access tokens directly into project files.

If `git` is not installed, install Apple's command-line developer tools with:

```bash
xcode-select --install
```

## Personalize it

Run the app and use the sidebar to enter his name, your name, what you appreciate about him, and a favorite memory. You can also edit the message lists in `app.py` to add your own inside jokes.

## Tech stack

- Python
- Streamlit
- Git and GitHub

---

Made with ❤️ and a little sarcasm.
