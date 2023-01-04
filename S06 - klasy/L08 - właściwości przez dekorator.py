class Cake:

    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = "other"
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if self.kind == "cake":
            self.__text = text
        else:
            self.__text = ""

    def showInfo(self):
        print("{}\nKind:\t\t{}\nTaste:\t\t{}\nGluten:\t\t{}".format(self.name.upper(), self.kind, self.taste,
                                                                    self.__gluten_free))
        if len(self.additives) > 0:
            print("Additives:")
            for i in self.additives:
                print("\t\t\t{}".format(i))
        if len(self.filling) > 0:
            print("Filling:\t{}".format(self.filling))
        if self.__text != "":
            print(f"Text:\t\t{self.__text}")
        print(30 * "-", "\n")

    def setFilling(self, newFilling):
        self.filling = newFilling

    def addAdditives(self, newAdditives):
        self.additives.extend(newAdditives)

    @property
    def Text(self):
        return self.__text
    @Text.setter
    def Text(self, newText):
        if self.kind == "cake":
            self.__text = newText
        else:
            print("Dla tego ciasta nie można wprowadzić napisu")




cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', True, "Best")
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, "")
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', False, "")
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False, "Worst")

cake04.Text = "Try"
cake01.Text = "Try"

for i in Cake.bakery_offer:
    i.showInfo()

print(vars(cake03))
