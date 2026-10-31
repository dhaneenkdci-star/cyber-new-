from flask import Flask, render_template, request, jsonify
from password_checker import check_password, generate_password

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/check")
def api_check():
    data = request.get_json(silent=True) or {}
    password = data.get("password", "")
    if not isinstance(password, str):
        return jsonify({"error": "Password must be text."}), 400
    if len(password) > 256:
        return jsonify({"error": "Password is too long (maximum 256 characters)."}), 400

    result = check_password(password)
    return jsonify(result)

@app.get("/api/generate")
def api_generate():
    try:
        length = int(request.args.get("length", 16))
    except (TypeError, ValueError):
        return jsonify({"error": "Length must be a number."}), 400

    if not 8 <= length <= 64:
        return jsonify({"error": "Choose a length between 8 and 64."}), 400

    return jsonify({"password": generate_password(length)})

if __name__ == "__main__":
    # Local development only. Do not use Flask's development server in production.
    app.run(host="127.0.0.1", port=5000, debug=False)
