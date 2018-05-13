# flaskapps
this git is the notes that while watching the youtube video of Corey Schafer.
https://www.youtube.com/watch?v=QnDWIZuWYW0&index=1&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH

## basic
### main.py
a simple code with route the website in more than one path
 
### main3.py
a simple code that created the dummy data with list of dictionary,
and return the data, looping those by using jinja2 in html
and return the title name also
in templates directory, using {% if %}{% endif %} to return title
and using {% block content%}{% endblock %} to config the global area

## basic_with_boostrap
a simple code for using boostrap library, flask url_for libraray,
and how to arrange the files in flask.

# forms and input 
a code that create the user log-in or reg pages

flask_wtf to create the form
- StringField
- PasswordField
- SubmitField
- BooleanField

flask_wtf.validators to check the data
- DataRequired
- Length
- Email
- EqualTo
- min
- max

using build-in secrets modules to create the sercets key 
import secrets
secrets.token_hex(16)

using flash to flash a new message while user login/reg
using redirect to redirect the web-pages while user login/reg
