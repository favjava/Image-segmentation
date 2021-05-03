import time
import File_1
import File_2
import File_3
import File_4
import File_5
import File_6


def region_based():
    File_1.f1()


def threshold():
    File_2.f2()


def morphological():
    File_3.f3()


def cluster():
    File_4.f4()


def edge_based():
    File_5.f5()


def watershed():
    File_6.f6()


def default():
    print("Wrong choice!!!")


choices = {1: "Region Based",
           2: "Threshold",
           3: "Morphological",
           4: "Cluster Based",
           5: "Edge Based",
           6: "WaterShed",
           7: "Exit"}
operations = {"1": region_based,
              "2": threshold,
              "3": morphological,
              "4": cluster,
              "5": edge_based,
              "6": watershed}
print("\n\t\t\tWelcome To Image Segmentation!!", "\U0001f600"*6)
print("===============================================================")
say = input("\nTo start type 'start' or 'exit' to terminate: ")
x = 0
if say.lower() == 'start' or say.lower() == 'yes':
    while x == 0:
        print('\nYour Operations on Image are: ')
        for key, value in choices.items():
            print(key, ': ', value)
        ch = input("\n================================="
                   "\n\nEnter your choice: ")
        if ch == "exit" or ch == "no" or int(ch) == 7:
            x = 1
            print("\nClosing Application", end="")
            for i in range(4):
                print(".", end="")
                time.sleep(1)
            exit()
        else:
            print("Processing your Image", end="")
            for i in range(3):
                print(".", end="")
                time.sleep(1)
            if ch not in operations.keys():
                default()
            else:
                operations[ch]()
else:
    print("Cannot understand !!! Try again")
    print("\nClosing Application", end="")
    for i in range(4):
        print(".", end="")
        time.sleep(1)
    exit()
