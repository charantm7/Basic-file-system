from flask import Flask, render_template, request, jsonify
from waitress import serve
app = Flask(__name__)

# Endpoint to handle user messages
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    # Here you would typically call your chat logic or AI model.
    # For now, let's send a simple response back
    bot_response = "Thank you for your query. We will assist you with ticketing information shortly."
    
    return jsonify({'message': bot_response})

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=505100, threads=2)
    
