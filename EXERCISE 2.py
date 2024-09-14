def main():
    nameSet = set()

    while True:
        name = input("Enter a name or press Enter to finish:")

        if name == "":
            break
        if name in nameSet:
            print("Exciting name")
        else:
            print("New name")
            nameSet.add(name)

    print("names entered:")

    for name in nameSet:
        print(name)

main()






