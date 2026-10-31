# Password Security Checker

A beginner-friendly full-stack password checker built with HTML, CSS, JavaScript, Python and Flask.

## Features
- Responsive dark cybersecurity-inspired interface
- Password strength estimate based on five visible rules
- Suggestions for missing password characteristics
- Secure random password generator using Python's `secrets` module
- Copy generated password to clipboard
- No database: passwords are not stored by this demo

## Requirements
- Python 3.10 or newer
- VS Code
- VS Code Python extension (recommended)

## Run in VS Code

1. Extract this project ZIP.
2. Open the `Password-Security-Checker` folder in VS Code.
3. Open Terminal → New Terminal.
4. Create a virtual environment:

   Windows:
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

5. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

6. Start the app:
   ```bash
   python app.py
   ```

7. Open this address in your browser:
   http://127.0.0.1:5000

Stop the server with `Ctrl + C`.

## API routes
- `POST /api/check` with JSON body `{"password":"Example!123456"}`
- `GET /api/generate?length=16`

## Important security notes
- The strength result is a simple educational estimate, not a breach check or a guarantee of security.
- This local demo does not save passwords, but the password is sent from the browser to the local Flask server for checking.
- Do not enter real account passwords into demonstration apps.
- Before public deployment, use HTTPS, production hosting, security testing, rate limiting and appropriate request protections. Do not use Flask's development server in production.
