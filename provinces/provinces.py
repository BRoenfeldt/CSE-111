"""
AlbertaCount = 0
with open('provinces.txt', "rt") as file:
    #file.pop()
    #file.pop(0)
    for i, line in enumerate(file):
        if "AB" in line:
            AlbertaCount += 1
        if "Alberta" in line:
            AlbertaCount += 1
        if line == "AB":
            line[i] = "Alberta"
        print(f"{line}")
    print(AlbertaCount)
"""

def returnList(incomingList):
    with open(incomingList, "rt") as file:
        exitlist = []
        for line in file:
            exitlist.append(line.strip())
        return exitlist

def main():
    count = 0
    provinceList = returnList("provinces.txt")
    provinceList.pop()
    provinceList.pop(0)
    for i in range(len(provinceList)):
        if provinceList[i] == "AB":
            provinceList[i] = "Alberta"
        if provinceList[i] == "Alberta":
            count += 1
        print(f"{provinceList[i]}")
    print(f"There are {count} instances of Alberta in the list.")


if __name__ == "__main__":
    main()