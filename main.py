# from flask import Flask
#     # $env:FLASK_APP = "main.py"
#     # flask run
#     # To run in PS
#
# from markupsafe import escape
#     # Allows us to escape user input from the url to prevent injection attacks.
#
# app = Flask(__name__)
#     # Name of our flask app
#
# @app.route("/")
#     #Tells us what URL should trigger our hello_world func.
# def hello_world():
#     # Said hello_world func.
#     return "<p>Hello, World!</p>"
#     # Info to display at said URL
#
# @app.route('/user/<username>')
#     # <> creates a var based on the user's input. Input would be assigned to the "username" var.
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'
#     # escape in action. preventing html from being ran
#
# @app.route('/post/<int:post_id>')
#     #can use converter to convert user input
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'
#
# #CONVERTER TYPES
# # string: (default) accepts any text without a slash
# # int: accepts positive integers
# # float: accepts positive floating point values
# # path: like string but also accepts slashes
# # uuid: accepts UUID strings

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return 'Welcome...'
    else:
        return 'sussy lil baka trynna post to my webserver...'

@app.route('/var/<username>')
def vartest(username):
    return f'The username is {escape(username)}'