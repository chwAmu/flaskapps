"""
this project we will create the email and password reset function.

from itsdangerours import TimedJSONWebSignatureSerializer as Serializer
s=Serializer('secert',30)
token=s.dumps({'user_id':1}).decode('uft-8')
token

after 30s..
token// with error


"""


from flaskblog import app

if __name__ == '__main__':
    app.run(debug=True)
