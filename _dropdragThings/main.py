from flask import Flask,render_template,url_for,request,redirect,jsonify
from forms import saveLayoutForm
import json

app = Flask(__name__)

#create a dummy data dictionary of list
duumyData=[
	{
		'author':'hiroshi',
		'title':'post1',
		'content':'mypost1',
		'data_posted':'2018-05-10'
	}
	,
	{
		'author':'amu',
		'title':'post2',
		'content':'mypost2',
		'data_posted':'2018-05-11'
	}
]


@app.route("/",methods=['GET','POST'])
@app.route("/home",methods=['GET','POST'])
def home():
	if request.method=='POST':
		data=json.dumps(request.json)
		saveFile(request.json)
		return jsonify(request.json)
		# return redirect(url_for('home'),jsonify(request.json))
	elif request.method=='GET':
		with open('page.json') as f:
			data=json.load(f)
		print('im here')
		print(data)
	return render_template('home.html',data=data)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

def saveFile(data):
	with open('page.json','w') as f:
		json.dump(data,f)



if __name__ == '__main__':
    app.run(debug=True)
