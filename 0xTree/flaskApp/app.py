from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

def get_earn():
    valor = 42;
    return valor

# Ruta de inicio
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/crearFormulario', methods=['POST'])
def crearFormulario():
    # data = request.get_json()
    texto1 = request.form.get('texto1', '')
    texto2 = request.form.get('texto2', '')
    # Aquí puedes procesar los datos recibidos
    print(request.form.get('Nombre'))
    return render_template('index.html')

@app.route('/form')
def redirect_to_form():
    return render_template('form.html')

@app.route('/family')
def redirect_to_family():
    return render_template('family.html')

@app.route('/home')
def redirect_to_home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

    
# Token eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyYlllanJ5RTdYVHluaXgxT1hqY0s1MlB0NnIiLCJ0eXBlIjoiZXJwIiwiaWQiOiIiLCJ1c2VybmFtZSI6ImRhbml0aTMzM0BnbWFpbC5jb20iLCJjaWQiOiIzN2Q2NmIwMS1jM2Y3LTQyZjMtOTU1Zi04ZWRiNzI5YTFhMTciLCJza3UiOlt7InIiOjExLCJzIjo4LCJlIjowfSx7InIiOjExLCJzIjo4MDAzLCJlIjowfSx7InIiOjExLCJzIjozLCJlIjowfSx7InIiOjExLCJzIjo4MDA1LCJlIjowfSx7InIiOjExLCJzIjo4MDAxLCJlIjowfSx7InIiOjExLCJzIjo4MDAyLCJlIjowfSx7InIiOjExLCJzIjo4MDEwLCJlIjowfV0sInB1YyI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMCJ9.pI22n21wVywdnuOc-qfYKunIn7fm8RrjJndH1jY39JB6N48ZoH7gXTZGrgeJ8clkOOK8_OEZPy6Fq-KTdbMp9oQr7iutNXC-xoQE4536uBCpTR-rZ92rfVkN5M4UThB2wwdBdvaubEyYm-I6cWWXVaw3Z3nMOIaSfFBhQ80FfpiIKgS4Ip8xAjFCDGJm4k7kKHZWmEaQovKmjZObccBweSiyTq8Hp_gjX3zicgg5LAH8Sk4DShywe74h7PTChmNP45z7JLhKzbe0FSlEx87L1Uddg_7YWv3VY7ryHKNSARX-1BouEk1MQ29nrRC-u9E9cFO4IX3gE3bUWDqh8kUisBqUweayKHWBdye4Grtpiut7Xae1JaPICxdMbr_u2SY7maJKBXgQT8MlNEfNOADRIueDpwPKwWf2spJdp-gCEknwn9SeTs5KoAJp9QNmmxy2zWGRGTv6S3j4TRQ5E_wswiCa3gWE7ZG2t0Fa6CHjuCtvd09DhfwimfEtGbuxOgErrNisTFF3YIxs_Pp0zvmCaYpcZNwC84W88wveANkfKye4OE6lF5HiUAXkIDu_3poJg_lfHyvdqbrx_Jlsz6vWdkuIysPE9z47SVDh1bA7gnKzdJS4KqkHIZwjwidS7ZwDMJTJEXcNxRVv9Lp4P-h0ObAJk_pfzzNuV-_EOJigSgU