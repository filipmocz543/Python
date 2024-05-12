###### Task 9
##### Write a program, which will find all such numbers between 1 and 1000 (both included) such
##### that each digit of the number is an even number the numbers obtained should be printed
### in a comma-separated sequence on a single line.

def zakres():

    for i in range(1,1001):
        if i%2==0:
            print(i, end=" ,")

def main():

    zakres()

if __name__ == '__main__':
    main()