from flask import Flask, render_template

app = Flask(__name__)

@app.route('/cv')
@app.route('/')
def hello_world():
    found = True
    if found:
        return render_template('CV.html', name='Lir')
    else:
        return render_template('CV.html')


@app.route('/assignment8')
def assignment8_fun():
    name = 'lir'
    second_name = 'amsalem'
    uni = 'BGU'
    return render_template('assignment8.html',
                           profile={'name': name, 'second_name': second_name},
                           address= {'country': 'israel','city': 'sderot', 'street': 'oranim 9' },
                           university=uni,
                            Hobbies=['art','music','sql','flask', 'animal', 'web']
                           )


if __name__ == '__main__':
    app.run(debug=True)
