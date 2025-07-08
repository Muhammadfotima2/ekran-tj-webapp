from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return "POST-запрос получен"
    return render_template('catalog.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
