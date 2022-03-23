from flask import Flask,request, send_file
from flask.views import MethodView
from flask import render_template
from flatmates_app.main import Housemate,Bill,to_pdf



app=Flask(__name__,template_folder="templates",static_folder="static_original")

class Home(MethodView):
    def get(self):
        return render_template("home.html")

class AppMain(MethodView):

    def get(self):
        return render_template("app_flask.html")

class ResultsPage(MethodView):

    def post(self):
        amount=request.form["amount"]
        period=request.form["period"]
        name1, days1 = (request.form["name1"], request.form["days1"])
        name2, days2 = (request.form["name2"], request.form["days2"])

        flatmate1=Housemate(name1,int(days1))
        flatmate2 = Housemate(name2, int(days2))
        res=Bill(int(amount),period).bill_to_pay(flatmate1,flatmate2)

        to_pdf(res)

        return render_template("results_page.html",amount=amount,period=period,res=res)

    def get(self):
        return render_template("results_page.html")

class DownloadPage(MethodView):

    def post(self):
        file="Bills.pdf"
        return send_file(file, as_attachment=True)



app.add_url_rule("/",view_func=Home.as_view("home"))
app.add_url_rule("/app",view_func=AppMain.as_view("billsapp"))
app.add_url_rule("/bills",view_func=ResultsPage.as_view("bill_amount"))
app.add_url_rule("/download",view_func=DownloadPage.as_view("download"))


app.run(debug=True)