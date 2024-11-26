from flask import Flask, request, jsonify,url_for,redirect,render_template
from backend.file_system import FileSystemManager

app = Flask(__name__)
fsm_manager = FileSystemManager()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/read_file', methods=['GET'])
def read_file():
    filename = request.args.get('filename')
    if filename:
        data = fsm_manager.read_file(filename)
        return jsonify({"data": data})
    return jsonify({"error": "Filename not provided"}), 400

@app.route('/write_file', methods=['POST'])
def write_file():
    content = request.get_json()
    filename = content.get('filename')
    data = content.get('data')
    if filename and data:
        fsm_manager.write_file(filename, data)
        with open (filename, 'a') as f:
            f.write(data)
        return jsonify({"message": "File written successfully."})
    return jsonify({"error": "Invalid data"}), 400
@app.route('/features')
def features():
    return render_template('features.html')

if __name__ == '__main__':
    app.run(debug=True,port=8080)
