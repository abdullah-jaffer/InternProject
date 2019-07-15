from helper import removeMultyOccurence
from helper import removeFirstOccurence

def main():

 f1 = open("input", "r")
 open('output', 'w').close()
 f2 = open("output", "a+")
 list = []
 f3 = f1.readlines()
 f2.write("Function 1:\n")
 for x in f3:
     str = removeMultyOccurence(x)
     f2.write(str)
     list.append(removeFirstOccurence(x))

 f2.write("\nFunction 2:\n")
 for i in list:
     f2.write(i)




if __name__ == "__main__":
    main()