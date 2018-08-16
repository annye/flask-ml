from flask import Flask, render_template, url_for,request
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, configure_uploads, DATA,ALL
from werkzeug import secure_filename
import sys

def set_trace():
    """A Poor mans break point"""
    # without this in iPython debugger can generate strange characters.
    from IPython.core.debugger import Pdb
    Pdb().set_trace(sys._getframe().f_back)
app = Flask(__name__)
Bootstrap(app)

# Configuration
files = UploadSet('files',ALL)
app.config['UPLOADED_FILES_DEST'] = 'static/uploadstorage'
configure_uploads(app,files)



import os
import datetime
import time


#EDA Packages
import pandas as pd 
import numpy as np 


# ML Packages







@app.route('/')
def index():
    return render_template('index.html')


@app.route('/datauploads', methods=['GET','POST'])
def datauploads():
    if request.method == 'POST' and 'csv_data' in request.files:
        file = request.files['csv_data']
        filename = secure_filename(file.filename)
        file.save(os.path.join('static/uploadstorage', filename))
        df = pd.read_csv(os.path.join('static/uploadstorage', filename))
        df_table = df
        return render_template('details.html',filename=filename,  df_table=df)
		





if __name__ == '__main__': 
	app.run(debug=True)