from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

@app.route('/upload')
def render_file():
   return render_template('upload.html')

@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'uploads succes!'

if __name__ == '__main__':
   app.run(debug=True)
