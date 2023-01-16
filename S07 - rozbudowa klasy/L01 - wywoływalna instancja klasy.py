class NoDuplicates:

    def __init__(self, list):
        self.list = list

    def __call__(self, *args):
        for i in args:
            self.list.append(i) if i not in self.list else None


myNoDup = NoDuplicates([])

myNoDup("keyboard", "mouse")
print(myNoDup.list)
myNoDup("keyboard")
print(myNoDup.list)
myNoDup("mouse", "pendrive")
print(myNoDup.list)





