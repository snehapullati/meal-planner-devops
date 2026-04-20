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

    for key in choices:
        if "eat" in key:
            person_id = key.replace("eat", "")
            eat = choices.get(f'eat{person_id}')
            food = choices.get(f'food{person_id}')

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
    app.run(host="0.0.0.0", port=5000)