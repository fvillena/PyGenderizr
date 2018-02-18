import csv

def PyGenderizr(name):
    name = name.lower()

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