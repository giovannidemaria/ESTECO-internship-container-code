from flask import Flask, request

app = Flask(__name__)

@app.route('/uppercase', methods=['POST'])
def uppercase():
    data = request.get_data().decode('utf-8') # Get the request data and decode it to a string
    print("Received data:", data) # Add this line
    response_data = data.upper() # Convert the string to uppercase
    return response_data # Return the uppercase string as the response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)