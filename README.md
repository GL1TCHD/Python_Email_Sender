# CV Email Sender

A simple desktop application built with Python that helps you send your CV (PDF) to a list of HR managers' email addresses automatically. You can paste emails manually. It also supports delays to prevent spam filters, logs successful/failed sends, and shows real-time progress.

## Features

- Attach your PDF CV to all emails
- Automatically log all successful and failed sends
- Delay between each email to avoid spam filters
- GUI preview before sending
- Live progress bar
- Packaged as a Windows `.exe` (no Python required)

## Requirements (for development)

- Python 3.8+
- `openpyxl`
- `tkinter` (comes with standard Python)
- `PyInstaller` (for building the .exe)

## Installation (for Users)

Download the latest release from the `dist/` folder or run the installer if provided.

## Usage

1. Open the app.
2. Enter your email and app password.
3. Upload your CV (PDF).
4. Click "Preview" to verify email format.
5. Click "Send Emails" to start sending.
6. Check `email_log.txt` for logs.


## Build (for Developers)

To package the app as `.exe`:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed cv_sender.py
```
Output will be in the dist/ folder

## License
MIT License. See [LICENSE](https://github.com/GL1TCHD/Python_Email_Sender/blob/master/LICENSE) file.

## Contributing
Pull requests are welcome! See [CONTRIBUTING.md](https://github.com/GL1TCHD/Python_Email_Sender/blob/master/CONTRIBUTING.md) for details.
