from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "<h1>Welcome to My Flask App 🚀</h1><p>Its Hanaan Here.!!</p>"

# Dynamic route with query parameter
@app.route("/hello")
def hello():
    name = request.args.get("name", "Guest")
    return f"<h2>Hello, {name}!</h2>"

# About route
@app.route("/about")
def about():
    return "<h3>This is a simple Flask app example.</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
