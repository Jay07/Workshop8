from guitar import Guitar

guitarList = []

print("My Guitars!")

UserQuit = False
while not UserQuit:
    name = input("Name: ")
    if name == "":
        UserQuit = True
    else:
        year = input("Year: ")
        cost = input("Cost: ")
        guitar = Guitar(name, int(year), float(cost))
        guitarListItem = name + "," + year + "," + cost
        guitarList.append(guitarListItem)
        print("{} added".format(guitar))

print("These are my guitars:")
counter = 1
for element in guitarList:
    element = str(element)
    element = element.split(",")

    outputName = element[0]
    outputYear = element[1]
    outputYear = int(outputYear)
    outputCost = element[2]
    outputCost = float(outputCost)

    element = Guitar(element)

    if element.is_vintage(outputYear):
        outputVintage = "(vintage)"
    else:
        outputVintage = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(counter, outputName, outputYear, outputCost, outputVintage))
    counter += 1