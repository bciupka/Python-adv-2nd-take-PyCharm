class Cake:

    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free):
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

    def showInfo(self):
        print("{}\nKind:\t\t{}\nTaste:\t\t{}\nGluten:\t\t{}".format(self.name.upper(), self.kind, self.taste, self.__gluten_free))
        if len(self.additives) > 0:
            print("Additives:")
            for i in self.additives:
                print("\t\t\t{}".format(i))
        if len(self.filling) > 0:
            print("Filling:\t{}".format(self.filling))
        print(30 * "-", "\n")

    def setFilling(self, newFilling):
        self.filling = newFilling

    def addAdditives(self, newAdditives):
        self.additives.extend(newAdditives)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', True)
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False)
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', False)
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False)

cake03.__gluten_free = True
cake03._Cake__gluten_free = True

for i in Cake.bakery_offer:
    i.showInfo()


print(vars(cake03))
