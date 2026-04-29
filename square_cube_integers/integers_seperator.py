class IntegerSeperator:
    def __init__(self, input_file):
        self.input_file = input_file

    def process_integers(self):
        try:
            with open(self.input_file, "r") as file:
                numbers = []
                for line in file.readlines():
                    numbers.append(int(line.strip()))