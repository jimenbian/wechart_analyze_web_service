import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
from flask import send_from_directory
import get_data
import get_user

UPLOAD_FOLDER = 'static/Uploads/'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
@app.route('/Uploads/<filename>')
def uploaded_file(filename):
  name=filename.rsplit('.', 1)[0]
  get_data.Get_data(name)
  get_user.put_out(name)
  return send_from_directory('static/result/',
                               filename)
from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)

# if __name__ == '__main__':
#     app.run()