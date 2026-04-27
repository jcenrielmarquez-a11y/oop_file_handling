class NumbersSeperator:
    def __init__(self, input_file):
        self.input_file = input_file
        self.numbers = []

    def numbers_separator(self, even_file, odd_file):
        try:
            with open(self.input_file, "r") as file:
                self.numbers = [int(line.strip()) for line in file.readlines()]

            self.write_to_file(even_file, self.even_numbers())
            self.write_to_file(odd_file, self.odd_numbers())

            print("Process Completed")
        except FileNotFoundError:
            print("File Not Found")
        except ValueError:
            print("Value Error")
