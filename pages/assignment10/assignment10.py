from flask import Blueprint, render_template, redirect, request
from interact_with_DB import interact_db

# assignment10 blueprint definition
assignment10 = Blueprint('assignment10', __name__, static_folder='static',static_url_path='/assignment10', template_folder='templates')


@assignment10.route('/assignment10')
def index():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)

@assignment10.route('/insert_user', methods=['post'])
def insert_user_func():
    #get the data
    name = request.form['name']
    email = request.form['email']

    #insert to db
    query = "INSERT INTO users(name, email) VALUES ('%s','%s');" % (name, email)
    interact_db(query=query, query_type='commit')

    #come back to assignment10
    return redirect('/assignment10')

@assignment10.route('/update_userEmail', methods=['post'])
def update_userEmail_func():
     #get the data
     name = request.form['name']
     email = request.form['email']

     # update to db
     query = "UPDATE users SET email='%s' WHERE name='%s';" % (email, name)
     interact_db(query=query, query_type='commit')

     return redirect('/assignment10')

@assignment10.route('/update_userName', methods=['post'])
def update_userName_func():
     #get the data
     name = request.form['name']
     email = request.form['email']

     # update to db
     query = "UPDATE users SET name='%s' WHERE email='%s';" % (name, email)
     interact_db(query=query, query_type='commit')

     return redirect('/assignment10')

@assignment10.route('/delete_user', methods=['post'])
def delete_user_func():
    user_email= request.form['email']
    query = "DELETE FROM users WHERE email='%s';" % user_email
    interact_db(query=query, query_type='commit' )

    return redirect('/assignment10')
