from flask import Blueprint, render_template,redirect,url_for,request
from application.models import User
from application.forms import LoginForm,RegisterForm
from flask_bcrypt import Bcrypt
from flask_login import login_user,login_required,current_user,logout_user


users_auth=Blueprint("users_auth",__name__,template_folder="templates",static_folder="static")


@users_auth.route("/",methods=["POST","GET"])
def registration():

    form=RegisterForm()
    if form.validate_on_submit() and request.method=="POST":
        username=form.username.data
    ##Hashing PASSWORD before commiting to DB
        password = Bcrypt().generate_password_hash(form.password.data)
        email = form.email.data

        new_user=User(username=username,email=email,password=password)
        check=User.check_user(username=username)

        if not check:
            new_user.save()
            message="Registration successful"
            return render_template("register.html",form=form,message=message)
        else:
            message = "Username already taken"
            return render_template("register.html",form=form,message=message)

    return render_template("register.html",form=form)



@users_auth.route("/login",methods=["POST","GET"])
def log_in():

##If user is already Logged in
    if current_user.is_authenticated:
        return redirect(url_for("items.new_item"))

    form=LoginForm()
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        user=User.check_user(username=username)

        if user and User.check_password(username=username, password=password):

            login_user(user)
            message='Successfull login'
            return redirect(url_for("items.new_item",message=message))
        else:
            message = "Invalid user credentials"
            return redirect(url_for("users_auth.log_in",message=message))

    return render_template("login.html",form=form)


@users_auth.route("/logout",methods=["POST"])
@login_required
def log_out():

    logout_user()
    message="User successfully logged out"
    return redirect(url_for("users_auth.log_in",message=message))


