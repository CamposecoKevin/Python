def run():
    # squarts = []
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squarts.append(i**2)

    # print(squarts)

    #list comprehesion
    # squarts = [i**2 for i in range (1,101) if i % 3 !=0]

    #list comprehesion
    number = [i for i in range(1, 100000) if i % 36 == 0]
   # number = [i for i in range(1,100000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]
    print(number)

if __name__ == '__main__':
    run()