class Cake:

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

    def showInfo(self):
        print("{}\nKind:\t\t{}\nTaste:\t\t{}\nAdditives:".format(self.name.upper(), self.kind, self.taste))
        if len(self.additives) > 0:
            for i in self.additives:
                print("\t\t\t{}".format(i))
        if len(self.filling) > 0:
            print("Filling:\t{}".format(self.filling))
        print(30 * "-", "\n")

    def setFilling(self, newFilling):
        self.filling = newFilling

    def addAdditives(self, newAdditives):
        self.additives.extend(newAdditives)



cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '')

cake01.showInfo()
cake02.setFilling("vanilla cream")
cake02.showInfo()
cake03.addAdditives(["cocoa powde", "coconuts"])
cake03.showInfo()
