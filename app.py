from flask import Flask,render_template,request
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads' #<-- le fichier que nous allons télécharger dans



#la fonction pour uploader un fichier
@app.route('/upload',methods=["GET","POST"])
def upload():
	return render_template('upload.html')



@app.route("/uploader",methods=['GET','POST'])
def uploader():
	if request.method == "POST":
		f = request.files['file']
		f.save(secure_filename(f.filename))
		return 'file uploaded'



if __name__ == "__main__":
	app.run(debug=True)