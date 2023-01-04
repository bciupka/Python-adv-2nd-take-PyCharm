import types


def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)


def export_all_cakes_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        for i in obj.bakery_offer:
            content = template.format(i.name, i.kind, i.taste, i.additives, i.filling)
            f.write(content)


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
        print("{}\nKind:\t\t{}\nTaste:\t\t{}\nGluten:\t\t{}".format(self.name.upper(), self.kind, self.taste, self.__gluten_free))
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

    def __getText(self):
        return self.__text

    def __changeText(self, newText):
        if self.kind == "cake":
            self.__text = newText
        else:
            print("Dla tego ciasta nie można wprowadzić napisu")

    Text = property(__getText, __changeText, None, "Zmiana jeżeli cake")


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', True, "Best")
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, "")
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', False, "")
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False, "Worst")

# for i in Cake.bakery_offer:
#     i.showInfo()

cake01.export_1_cake_to_html = types.MethodType(export_1_cake_to_html, cake01)

cake01.export_1_cake_to_html(r"D:\Projekty\Kursy Python\Python - Advanced - PyCharm\S06 - klasy\PLIKI\cake01.html")

Cake.export_all_cakes_to_html = types.MethodType(export_all_cakes_to_html, Cake)

Cake.export_all_cakes_to_html(r"D:\Projekty\Kursy Python\Python - Advanced - PyCharm\S06 - klasy\PLIKI\cakes.html")

