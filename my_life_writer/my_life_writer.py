class MyLifeWriter:
    def __init__(self, file_name="mylife.txt"):
        self.file_name = file_name

    def write_lines(self):
        try:
            with open(self.file_name, "w") as file:
                while True:
                    line = input("Enter line: ")
                    file.write(line + "\n")

                    more = input("Are there more lines y/n? ").lower()
                    if more != "y":
                        break

            print(f"Contents written to {self.file_name} successfully!")

        except Exception as e:
            print("An error occurred:", e)