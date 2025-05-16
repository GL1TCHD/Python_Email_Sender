# Contributing to CV Email Sender

First off, thanks for taking the time to contribute!

The goal of this project is to help job seekers quickly send their CVs to HR managers through a friendly desktop interface.

---

## Ways to Contribute

- **Bug Reports** – If something doesn’t work, open an issue.
- **Feature Requests** – Suggest new ideas to improve the app.
- **Code Contributions** – Submit pull requests to fix bugs or add features.
- **UI/UX Suggestions** – Propose design changes or user experience improvements.
- **Translations** – Help translate the app to other languages.

---

## Code Guidelines

- Keep code readable and organized.
- Follow the existing style (PEP8 for Python).
- Comment any complex logic.
- Use meaningful commit messages.
- Test your changes thoroughly before submitting.

---

## Workflow

1. Fork the repo
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes
4. Test everything
5. commit and push
```bash
git add .
git commit -m "Add: Your message"
git push origin feature/your-feature-name
```
6. Open a pull requset on Github
---

## Setup for development
install Install dependencies:
```bash
pip install openpyxl pyinstaller
```

Run the app:
```bash
python cv_sender.py
```
Build `.exe`:
```bash
pyinstaller --onefile --windowed cv_sender.py
```


Thanks again for helping improve CV Email Sender!
