import re
import secrets
import string

COMMON_PASSWORDS = {
    "password", "password123", "123456", "12345678",
    "qwerty", "admin", "letmein", "welcome", "iloveyou"
}

def check_password(password: str) -> dict:
    """Return a simple rule-based password assessment.

    This is an educational strength estimate, not a guarantee that a
    password is safe or has never appeared in a data breach.
    """
    if not password:
        return {
            "strength": "Not rated",
            "score": 0,
            "percentage": 0,
            "suggestions": ["Enter a password to begin."],
            "checks": []
        }

    checks = [
        {"label": "At least 12 characters", "passed": len(password) >= 12},
        {"label": "Uppercase letter (A-Z)", "passed": bool(re.search(r"[A-Z]", password))},
        {"label": "Lowercase letter (a-z)", "passed": bool(re.search(r"[a-z]", password))},
        {"label": "Number (0-9)", "passed": bool(re.search(r"\d", password))},
        {"label": "Special character", "passed": bool(re.search(r"[^A-Za-z0-9]", password))},
    ]

    score = sum(item["passed"] for item in checks)
    suggestions = [f"Add: {item['label'].lower()}." for item in checks if not item["passed"]]

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        suggestions.insert(0, "Avoid this commonly used password.")

    if len(password) < 8:
        strength = "Very weak"
    elif score <= 2:
        strength = "Weak"
    elif score <= 3:
        strength = "Fair"
    elif score == 4:
        strength = "Good"
    else:
        strength = "Strong"

    if strength == "Strong" and len(password) < 12:
        strength = "Good"

    if not suggestions:
        suggestions = ["Good work. Consider using a unique passphrase for every account."]

    return {
        "strength": strength,
        "score": score,
        "percentage": round((score / 5) * 100),
        "suggestions": suggestions,
        "checks": checks
    }

def generate_password(length: int = 16) -> str:
    """Generate a password containing each character category."""
    if not 8 <= length <= 64:
        raise ValueError("Password length must be between 8 and 64.")

    groups = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        "!@#$%^&*()-_=+[]{}?"
    ]
    password_chars = [secrets.choice(group) for group in groups]
    all_chars = "".join(groups)
    password_chars.extend(secrets.choice(all_chars) for _ in range(length - len(password_chars)))

    # Use a cryptographically secure shuffle.
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    return "".join(password_chars)
