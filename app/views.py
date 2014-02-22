import settings
from app import myApp
import uuid
from flask import request, render_template
import csv
from utils import utils

@myApp.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = []
        for uploadedFile in request.files.getlist('file'):
            if allowed_file(uploadedFile.filename):
                files.append(uploadedFile)
    
        head = ["DateTime", "Value (kWh)", "Temp (F)"]    

        csvdata = []
        out = []

        for f in files:
            reader = csv.reader(f, delimiter=',')
            header = reader.next()            

            for d in reader:
                csvdata.append(d)
        
            data = utils.melt(header, csvdata)

        for uploadedFile in files:
            uploadedFile.close()

        return render_template('show_data.html', header=head, data=data)
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in settings.ALLOWED_EXTENSIONS


