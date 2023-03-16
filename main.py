class Parent():
    def __init__(self, name, gender, year_of_birth, haircolor):
        self.name = name
        self.gender = gender
        self.dob = year_of_birth
        self.haircolor = haircolor

class Child(Parent):
    def __init__(self,name, gender, year_of_birth, haircolor, PreferredToy):
        Parent.__init__(self, name, gender, year_of_birth, haircolor)
        self.PreferredToy = PreferredToy
    def HaveFun(self):
            print("I am having fun")

def main():
    print("Explore My Family Tree")
    mom = Parent("Mom", "Female", 1970, "brown")
    print(vars(mom))

    dad = Parent("Dad", "Male", 1969, "black")
    me = Child("Sam", "Female", 2004, "brown", "Lego")

    print(vars(me))
    me.HaveFun()

main()
'''
class Fruit():
        def __init__(self,Quality,Price,Freshness,Weight,Origin):
            self.Quality = Quality
            self.Price = Price
            self.Freshness = Freshness
            self.Weight = Weight
            self.Origin = Origin
            print("Created fruit")

class Banana(Fruit):
        def __init__(self, name, color, texture, Quality,Price,Freshness,Weight,Origin):
            Fruit.__init__(self, Quality,Price,Freshness,Weight,Origin)
            self.name = name
            self.texture = texture
            self.color = color
            print("Created banana")


class Watermelon(Fruit):
    def __init__(self, name, color, texture, Quality,Price,Freshness,Weight,Origin, Juiciness):
        Fruit.__init__(self, Quality, Price, Freshness, Weight, Origin)
        self.name = name
        self.texture = texture
        self.color = color
        print("Created watermelon")

#product = Banana("Ripe",1000.00,"Standard","26 pounds","Mars")
product1 = Banana("Mars Banana","Purple","Hard", "Ripe",1000.00,"Standard","26 pounds","Mars")
print(vars(product1))
product2 = Watermelon("Saturn Watermelon","Pink","Soft", "Decomposed",123456.78,"Not Fresh","400 pounds","Saturn", "90%")
print(vars(product2))
'''