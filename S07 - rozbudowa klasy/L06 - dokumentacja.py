class Cake:
    """
    To jest klasa do obsługi ciastkarni
    """
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        """
        Inicjacja obiektu

        :param name: Nazwa
        :param kind: Rodzaj
        :param taste: Snak
        :param additives: Dodatki
        :param filling: Wypełnienie
        """

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    @property
    def full_name(self):
        """
        Pełna nazwa obiektu
        :return: Zwraca nazwe - wywoływać z print()
        """

        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


help(Cake)
help(Cake.full_name)
