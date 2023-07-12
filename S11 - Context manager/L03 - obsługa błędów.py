import zipfile
import requests


class FileFromWeb:

    def __init__(self, url, tmp):
        self.url = url
        self.tmp = tmp

    def __enter__(self):
        response = requests.get(self.url)
        with open(self.tmp, "wb") as f:
            f.write(response.content)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == FileNotFoundError or exc_type == KeyError:
            print(exc_type, exc_val)
            return True
        elif exc_type is not None:
            print(exc_type, exc_val)
            return False
        else:
            pass

with FileFromWeb(r"https://www.ecb.europa.eu/stats/eurofxref/"
                 r"eurofxref.zip", r"D:\Projekty\Kursy Python\Python -"
                                   r" Advanced - PyCharm\S11 - Context manager\PLIKI\zap.zip") as f:
    with zipfile.ZipFile(f.tmp, "r") as z:
        a_file = z.namelist()[0]
        print(a_file)
        # a = 5/0
        z.extract(a_file, r"D:\Projekty\Kursy Python\Python - Advanced - PyCharm\S11 - Context manager\PLIKI", None)
