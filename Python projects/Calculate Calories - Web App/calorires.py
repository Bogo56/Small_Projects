from temperature import Temperature


class Calories(Temperature):


    def __init__(self,weight,height,age,gender,city,country):
        super().__init__(city,country)
        self.weight=weight
        self.height=height
        self.age=age
        self.gender=gender

    def calculate(self,activity):
        temp=self.get_temp()

        if self.gender=="man":
            formula=((66.5 + (13.8 * self.weight) + (5 * self.height)) - (6.8 * self.age))-temp * 10
            res=formula*activity
        elif self.gender=="woman":
            formula = ((655.1 + (9.6 * self.weight) + (1.9 * self.height)) - (4.7 * self.age))-temp * 10
            res=formula*activity

        return round(res,2)





if __name__=="__main__":

    Bogo = Calories(83,196,25,"man","Varna","Bulgaria")
    res=Bogo.calculate(1.4)
    print(res)