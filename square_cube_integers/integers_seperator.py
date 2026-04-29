class IntegerSeperator:
    def __init__(self, input_file):
        self.input_file = input_file

    def process_integers(self):
        try:
            with open(self.input_file, "r") as file:
                numbers = []
                for line in file.readlines():
                    numbers.append(int(line.strip()))

        with open("double.txt", "w") as even_file, open("triple.txt", "w") as odd_file:
            for num in numbers:
                if num % 2 == 0:
                    even_file.write(str(num ** 2) + "\n")
                else:
                    odd_file.write(str(num ** 3) + "\n")