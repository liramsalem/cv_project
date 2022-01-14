from flask import Flask, render_template, jsonify
from flask import request
from flask import session
from interact_with_DB import interact_db
import random
import requests

app = Flask(__name__)
app.secret_key = '123'

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


@app.route('/assignment9', methods=['GET','POST'])
def assignment9_func():
    if request.method == 'GET':
        users = {'user1': {'name': 'Yosi', 'email': 'yo@gmail.com'},
                 'user2': {'name': 'Lir', 'email': 'lir@gmail.com'},
                 'user3': {'name': 'Tal', 'email': 'tal@gmail.com'},
                 'user4': {'name': 'Yarin', 'email': 'yarin@gmail.com'},
                 'user5': {'name': 'Yaron', 'email': 'yaron@gmail.com'},
                 'user6': {'name': 'Eli', 'email': 'eli@gmail.com'}
                 }

        if 'name' in request.args:
            name = request.args['name']
            if name == '':
                name = request.args['name']
                return render_template('assignment9.html', dic_users=users)
            else:
                for key in users:
                    for key2 in users[key]:
                        if users[key][key2]== name:
                            return render_template('assignment9.html', c_name=users[key]['name'], c_email=users[key]['email'])
                return render_template('assignment9.html', message='error')


    if request.method == 'POST':
        if 'logOutButton' in request.form:
            session['username'] = ''
        if 'username' in request.form:
            Username = request.form['username']
            Email= request.form['email']
            Password = request.form['password']
            session['username'] = Username

    return render_template('assignment9.html')

##assignment 10
#ביצוע קישור לבלופרינט#
from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

@app.route('/assignment11')
def assignment11_func():
    return render_template('assignment11.html')

@app.route('/assignment11/users')
def assignment11_users_func():
    return_dict = {}
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    for user in users:
        return_dict[f'user_{user.id}'] = {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
    return jsonify(return_dict)


@app.route('/assignment11/outer_source')
def assignment11_outer_source_func():
    return render_template('outer_source.html')


def get_user_b(userID):
    res = requests.get(f'https://reqres.in/api/users/{userID}')
    res = res.json()
    return res


@app.route('/req_backend')
def req_backend_func():
    nulll = request.args['userID_b']
    if (nulll == "" ):
        return render_template('outer_source.html', msg="enter ID")
    else:
        userID = int(request.args['userID_b'])
        user = get_user_b(userID)
    if (user == {} ):
        return render_template('outer_source.html', msg="user does not exist")
    else:
        return render_template('outer_source.html', user=user)



if __name__ == '__main__':
    app.run(debug=True)
