import datetime as dt


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        assert len(self.title) > 0, "Title is empty!"
        assert self.start <= self.end, "Start date is later than end date!"
        # if len(self.title) == 0:
        #     raise Exception("Title is empty!")
        # if self.start > self.end:
        #     raise ValueError("Start date is later than end date!")

    @classmethod
    def publish_offer(cls, listOfTrips):
        list_of_errors = []
        for i in listOfTrips:
            try:
                i.check_data()
            except ValueError as e:
                list_of_errors.append(f"{i.symbol}:{e}")
            except Exception as e:
                list_of_errors.append(f"{i.symbol}:{e}")
        assert len(list_of_errors) == 0, f"The list of trips has errors: {list_of_errors}"
        # if len(list_of_errors) > 0:
        #     raise Exception(f"The list of trips has errors: {list_of_errors}")
        # else:
        #     print("Done")
        print("Done")


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]


try:
    print("Sprawdzanie")
    Trip.publish_offer(trips)
    print("Done")
except Exception as e:
    print(e)



