from flask import Blueprint,render_template,redirect,url_for
from application.forms import AddItemForm
from flask_login import login_required,current_user
from backend.check_prices import PriceAlert

items=Blueprint("items",__name__,template_folder="templates")


@items.route("/new-item",methods=["POST","GET"])
@login_required
def new_item():

    form=AddItemForm()

    if form.validate_on_submit():
        new_item=form.item.data
        current_user.items.append(new_item)
        PriceAlert._insert_price(user=current_user,item=new_item)

        return redirect(url_for("items.new_item"))


    return render_template("new_item.html",form=form)


@items.route("/all-items",methods=["POST","GET"])
@login_required
def check_items():

    PriceAlert.check_price(user=current_user)
    all_items=PriceAlert.all_items(user=current_user)

    return render_template("all_items.html",user_items=all_items)