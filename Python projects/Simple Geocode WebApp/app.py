from flask import Flask,render_template,request,send_file
from werkzeug.utils import secure_filename
import pandas
import requests
import time
from GeoMap import d_frame

app=Flask(__name__)
base_url="https://api.opencagedata.com/geocode/v1/json?q={}&key=08a5eb499d564ea683fd3a092eca62a9"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/download",methods=["POST"])
def download():
    if request.method=="POST":
        global ufile
        ufile=request.files["file-upload"]
        if ufile.filename.endswith(".csv")==False:
            return render_template ("home.html",warning="Please upload a .csv file")
        ufile.save(secure_filename("uploaded_" + ufile.filename))
        with open("uploaded_" + ufile.filename, "r+") as file:
            df=pandas.read_csv(file)
            lng=[]
            lat=[]

            for adress in df["Address"]:
                query_url=base_url.format(adress)
                time.sleep(2.1)
                link=requests.get(query_url).json()
                lng.append(link["results"][0]["geometry"]["lng"])
                lat.append(link["results"][0]["geometry"]["lat"])
            
            df["Latitude"]=lat
            df["Longitude"]=lng
            html_file=df.to_html()
            df.to_csv("uploaded_" + ufile.filename)
            
            maps=d_frame(df)

            
        return render_template("download.html",html_file=html_file, maps=maps)


@app.route("/get-file")
def get_files():
        return send_file("uploaded_" + ufile.filename,attachment_filename="your_file.csv", as_attachment=True)


if __name__=="__main__":
    app.debug=True
    app.run()


