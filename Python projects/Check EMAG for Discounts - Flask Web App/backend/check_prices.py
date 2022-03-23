import requests
from bs4 import BeautifulSoup
from application.models import Items


## I'M USING @CLASSMETHODS HERE BECAUSE THOSE CLASSES DON'T NEED TO BE INSTANTIATED AND CAN BE USED AS TYPES( OR CLASSES)
# FOR THE USER CLASS I USED NORMAL METHODS, SINCE WE CREATE AN OBJECT FOR EVERY USER WHICH MEANS A NEW INSTANCE EVERY TIME
# THE PriceAlert CLASS DOES THE SAME THING EVERY TIME - SOMETHING LIKE A PROCEDURE##

class PriceAlert:

    ##THIS METHOD DOESN'T REFRENCE ANYTHING FROM THE CLASS SO IT SHOULD BE @STATICMETHOD
    # IT IS A PRIVATE METHOD AS WELL(USED BY THE OTHER METHODS OF THE CLASS AND NOT OUTSIDE OF IT)
    # IT GETS THE PRICE FOR AN ITEM IF AN ADEQUATE URL HAS BEEN GIVEN##
    @staticmethod
    def _get_price(item):
        try:
            page = requests.get(item)
            page = page.text
            soup = BeautifulSoup(page, "html.parser")
            ##Getting item price
            item_price = soup.find("p", attrs={"class": "product-new-price"})
            item_price.sup.decompose()
            item_price.span.decompose()
            final_price = int(item_price.text.strip("").replace(".", ""))
            ##Getting item image url
            item_image = soup.find("a", attrs={"class": "thumbnail product-gallery-image gtm_rp125918"})
            item_image = item_image.img.get("src")

            parsed_item = {"item_price": final_price,
                           "item_image": item_image}

        ##THIS BREAKS THE CALCULATIONS IN check_price METHOD(BECAUSE None) -GOTTA FIX IT
        except:
            parsed_item = {"item_price": None,
                           "item_image": None}
            pass

        return parsed_item


    ## THIS METHOD INSERTS THE INITIAL PRICE,IMAGE-URL AND NEW_PRICE  IN THE DB#
    @classmethod
    def _insert_price(cls, user, item):

        item_get = cls._get_price(item)
        item_object=Items(url=item,
                          price=item_get["item_price"],
                          item_image=item_get["item_image"],
                          new_price=[])
        user.items_info.append(item_object)
        user.save()


    ## THIS METHOD CHECKS FOR THE PRICE AND IF IT IS MORE THAN 10% CHANGE
    # UPDATES THE NEW_PRICE FIELD##
    @classmethod
    def check_price(cls, user):

        for item in user.items_info:

            saved_price = item["price"]
            checked_price = cls._get_price(item["url"])
            difference = checked_price["item_price"] / saved_price

            if difference <= 0.90:
                print(f"The Price of your Item Fell by {(1 - difference) * 100} % ")
                item["new_price"]= [checked_price["item_price"],
                                                                f"<h3 class='text-success'>DIFFERENCE: {int((difference - 1) * 100)}% DOWN</h3>"]
            elif difference >= 1.10:
                print(f"The Price of your Item Increased by {(difference - 1) * 100} % ")
                item["new_price"]= [checked_price["item_price"],
                                                                f"<h3 class='text-danger'>DIFFERENCE: {int((difference - 1) * 100)}% UP</h3>"]
            else:
                print("No significant price changes")
                item["new_price"]= [checked_price["item_price"],
                                                                f"<h3>No significant price changes</h3>"]

            user.save()

    ## GETTING ALL THE GENERATED USER ITEMS TO DISPLAY THEM IN A SEPARATE HTML PAGE - WITH THE PRICE AND IMAGE
    @classmethod
    def all_items(cls, user):
        user_items = user.items_info

        return user_items