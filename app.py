from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('app.html')  # Loads the frontend

if __name__ == '__main__':
    app.run(debug=True)
