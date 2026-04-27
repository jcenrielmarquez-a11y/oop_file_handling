class MyLifeWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_lines(self):
        try:
            with open(self.file_name, "w") as file:
                while True:
                    line = input("Enter line: ")
                    file.write(line + "\n")