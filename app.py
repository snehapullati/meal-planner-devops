from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    choices = request.form

    veg_count = 0
    nonveg_count = 0

    for i in range(1, 5):
        eat = choices.get(f'eat{i}')
        food = choices.get(f'food{i}')

        if eat == 'yes':
            if food == 'veg':
                veg_count += 1
            elif food == 'nonveg':
                nonveg_count += 1

    if veg_count > nonveg_count:
        result = "Cook Veg Today 🥦"
    elif nonveg_count > veg_count:
        result = "Cook Chicken Today 🍗"
    else:
        result = "It's a Tie! Decide Alternately ⚖️"

    return f"<h1>{result}</h1><a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True)