# python3


def build_heap(data):
    swaps = []
    
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    
    n = len(data)
    for i in range(n//2, -1, -1):
        pasr = i
        while 2 * pasr + 1 < n:
            ind = 2 * pasr + 1
            if ind + 1 < n and data[ind + 1] < data[ind]:
                ind = ind + 1
            if data[pasr] > data[ind]:
                swaps.append((pasr, ind))
                data[pasr], data[ind] = data[ind], data[pasr]
                pasr = ind
            else:
                break
    return swaps

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    
    cmd = input("Izvelies teksta ievadisanas veidu (I vai F): ")
    if "I" in cmd:
        n = int(input("Ievadi skaitu: "))
        data = list(map(int, input("Ievadi elementus: ").split()))
        # checks if lenght of data is the same as the said lenght
        assert len(data) == n
    elif "F" in cmd:
        nos = input("Faila nosaukums: ")
        with open (f"tests/{nos}") as file:
            n = int(file.readline())
            data=list(map(int, file.readline().split()))
        # checks if lenght of data is the same as the said lenght
            assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
