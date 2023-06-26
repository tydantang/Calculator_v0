from flask import Flask, render_template, request
import os

app = Flask(__name__)

template_dir = os.path.abspath('./')
app.template_folder = template_dir

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    result = eval(expression)+1
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
