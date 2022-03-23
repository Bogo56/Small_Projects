
from flatmates_app.PDF_stuff import pdf_obj

class Bill:
    def __init__(self,amount,period):
        self.amount=amount
        self.period=period

    def bill_to_pay(self,*args):
        flatmates={}

        for person in args:
            flatmates[f"{person.name}"]=person.days_to_pay

        total_days=sum(flatmates.values())

        for person in args:
            bil=round((person.days_to_pay/total_days)*self.amount,2)
            flatmates[f"{person.name}"]=dict(days=person.days_to_pay,bils=bil)


        return flatmates



class Housemate:
    def __init__(self,name,days_to_pay):
        self.name=name
        self.days_to_pay=days_to_pay


###PDF Print Function

def to_pdf(flatmates):
    for person in flatmates.keys():
        text = f"{person} has spent {flatmates[person]['days']} days in the house and owes {flatmates[person]['bils']} Leva"
        pdf_obj.cell(550, 20, text, 0, 0.4, "C")

    pdf_obj.output("Bills.pdf")


'''
Example Usage

bogo=Housemate("Bogo",22)
toshko=Housemate('Todor',27)
vanko= Housemate("Ivan",24)
maria=Housemate("Maria",27)
teo= Housemate("Teodor",28)
nasko= Housemate("Nasko",13)

bills_april=Bill(500,"December")
res=bills_april.bill_to_pay(bogo,toshko,vanko,maria,teo,nasko)

for person in res.keys():
    text=f"{person} has spent {res[person]['days']} days in the house and owes {round(res[person]['bils'],2)} Leva"
    pdf_obj.cell(550,20,text,0,0.4,"C")

pdf_obj.output("Bills.pdf")

'''


