from numbers_seperator import NumbersSeperator

def main():
    handler = NumbersSeperator("numbers.txt")
    handler.numbers_seperator("even.txt", "odd.txt")

if __name__ == "__main__":
    main()
