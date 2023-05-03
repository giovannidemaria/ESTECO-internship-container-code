from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def uppercase():
    if request.method == 'POST':
        data = modify_string(request.get_data().decode('utf-8'))
        url = 'http://10.39.248.223/uppercase'
        headers = {'Content-Type': 'text/plain'}
        response = requests.post(url, headers=headers, data=data)
        return render_template('index.html', response=response.text)
    else:
        return render_template('index.html')

def modify_string(input_string):
    # Rimuovi i primi 3 caratteri
    input_string = input_string[4:]
    # Sostituisci i '+' con gli spazi
    output_string = input_string.replace('+', ' ')
    return output_string

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
