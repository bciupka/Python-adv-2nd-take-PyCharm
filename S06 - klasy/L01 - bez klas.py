cake_01 = {
    "taste" : 'vanilia',
    "glaze" : 'chocolade',
    "text" : 'Happy Brithday',
    "weight" : 0.7}

cake_02 = {
    "taste" : 'tee',
    "glaze" : 'lemon',
    "text" : 'Happy Python Coding',
    "weight" : 1.3}


def show_cake_info(cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        cake["taste"], cake["glaze"], cake["text"], cake["weight"]))


cakes = [cake_01, cake_02]

show_cake_info(cakes[0])
show_cake_info(cakes[1])