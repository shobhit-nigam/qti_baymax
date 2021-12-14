from zipfile import ZipFile

with ZipFile("zzz.zip", "r") as objz:
    objz.printdir()
