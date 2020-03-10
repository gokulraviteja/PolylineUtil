from flask import Flask,render_template,request
import polyline
app = Flask(__name__)           



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/decode", methods=['POST','GET'])              
def decode():
	if(request.method=='POST'):
		text= request.form['textboxid']
		if(',' in text):
			text=text.strip()
			if(';' in text):
				latlongs=text.split(';')
			else:
				latlongs=text.split()
			arr=[]
			for i in latlongs:
				k=i.split(',')
				arr.append([float(k[0]),float(k[1])])
				poly=polyline.encode(arr)
			return render_template("displayPolyline.html",poly=poly)
		else:
			poly=text.strip()
			try:
				pings=polyline.decode(poly)
				latlongs=[]
				for i in pings:
					latlongs.append(str(i[0])+","+str(i[1]))
			except:
				latlongs=["Polyline inaccurate"]
			return render_template("displayLatlongs.html",latlongs=latlongs)
	else:
		return render_template("home.html")



if __name__ == "__main__":     
    app.run(debug=True,host='0.0.0.0')


