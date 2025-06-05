from flask import Flask, request
from flask_restful import Api
import elabapy
import json
import base64
from pathlib import Path
import os
import smtplib
from email.message import EmailMessage
import mimetypes
import io
import base64
from datetime import date
import subprocess


app = Flask(__name__, static_folder='../build',
            static_url_path='/')  # for Gunicorn deployment
# app = Flask(__name__)
api = Api(app)

PATH_TO_MC = "/opt/minio-binaries/mc"
ALIAS = "BUCKET"
BUCKET_PATH = ALIAS + "/NFDI4Bioimage/forms/"

TEMP_PATH = './temp-files'


@app.route('/api/check_mode', methods=["GET"])
def check_mode():
    # check if online, and get list of schemas used in job request workflows
    listSchemas = []
    listSubmitText = []
    try:
        with open("./conf/jobrequest-conf.json", "r") as fi:
            f = fi.read()
            f = json.loads(f)
            emailconf_list = f["confList"]
            for element in emailconf_list:
                listSchemas.append(element["completeSchemaTitle"])
                listSchemas.append(element["requestSchemaTitle"])
                listSubmitText.append(element["submitButtonText"])
                listSubmitText.append(element["submitButtonText"])
        return {"message": "connection is a success", "jobRequestSchemaList": listSchemas, "submitButtonText": listSubmitText}
    except Exception as e:
        return {"message": "connection is a success", "jobRequestSchemaList": listSchemas, "submitButtonText": listSubmitText}


# get schemas from backend
@app.route('/api/get_schemas', methods=["GET"])
def get_schemas():
    list_of_schemas = {"schemaName": [""], "schema": [None]}
    filelist = list(Path('./schemas').glob('**/*.json'))
    for i in range(0, len(filelist)):
        file = filelist[i]
        file = open(str(file), 'r', encoding='utf-8')
        filename = str(file.name).replace("schemas\\", "")
        filename = filename.replace("schemas/", "")  # for linux, maybe
        content = file.read()
        list_of_schemas["schema"].append(content)
        list_of_schemas["schemaName"].append(filename)
    return list_of_schemas

# Upload the slide form to the bucket
@app.route('/api/submit_job_request', methods=['POST'])
def submit_job_request():
    jsdata = request.form['javascript_data']
    jsdata = json.loads(jsdata)
    #print(jsdata)
    filename = jsdata["slide_id"] + "-region_metadata.json" 
    filepath = TEMP_PATH + '/' + filename
    # write the json form in the temp folder data/jsdata
    with open(filepath, 'w') as outfile:
        outfile.write(json.dumps(jsdata))

    cmd = [PATH_TO_MC, "put", filepath, BUCKET_PATH]
    upload = subprocess.run(cmd)

    if upload.returncode != 0:
        return {"responseText": f"Upload failed for {filepath}", "message": "upload failed"}
    
    # Clean up
    os.remove(filepath)

    return {"responseText": f"Upload success for {filepath}.", "message": "success", "response":200}

