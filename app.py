from flask import Flask, render_template, request, redirect, send_file
from werkzeug import secure_filename
from os import system

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
      f.save('uploaded_image')
      return send_file('uploaded_image', mimetype='image/gif')
		
if __name__ == '__main__':
   app.run(debug = True)
   system('rm uploaded_image')