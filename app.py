from flask import Flask, render_template, request, redirect, send_file
from werkzeug import secure_filename
from os import system

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def upload_file1():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        return redirect('/img')

@app.route('/img', methods = ['GET', 'POST'])
def upload_file2():
    if request.method == 'POST':
        f = request.files['file']
        if allowed_file(f.filename.lower()):
            f.save('uploaded_image')
            return send_file('uploaded_image', mimetype='image/gif')
		
if __name__ == '__main__':
   app.run(debug = True)
   system('rm uploaded_image')