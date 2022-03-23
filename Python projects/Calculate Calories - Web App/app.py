from flask.views import MethodView
from flask import Flask, request,render_template
from calorires import Calories


app=Flask(__name__,template_folder="templates")


class Calculator(MethodView):

    def get(self):
        return render_template("home.html")

    def post(self):

        weight=int(request.form["weight"])
        height=int(request.form["height"])
        age=int(request.form["age"])
        gender=request.form["gender"]
        city=request.form["city"]
        country=request.form["country"]
        activity=request.form["activity"]

        result=Calories(weight,height,age,gender,city,country)
        try:
            calories=result.calculate(float(activity))
            message=False
        except:
            message="Please enter a valid location"
            calories=False

        return render_template("home.html",calories=calories,message=message)



app.add_url_rule("/",view_func=Calculator.as_view("calculator"))

app.run(debug=True)
