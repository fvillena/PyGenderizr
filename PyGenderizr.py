import csv

def normalizeStr (str):
    str = str.lower()
    str = str.strip(" ")
    str = str.replace("á", "a")
    str = str.replace("é", "e")
    str = str.replace("í", "i")
    str = str.replace("ó", "o")
    str = str.replace("ú", "u")
    str = str.replace("ñ", "n")
    return str

def PyGenderizr(name):
    name = normalizeStr(name)

    with open('maleNames.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            for field in row:
                if field == name:
                    return "male"

    with open('femaleNames.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            for field in row:
                if field == name:
                    return "female"

    return "undefined"

if __name__ == "__main__":
    import sys

    print(PyGenderizr(str(sys.argv[1])))