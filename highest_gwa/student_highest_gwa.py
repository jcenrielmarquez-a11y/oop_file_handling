class StudentHighestGwa:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_and_find_highest(self):
        name_with_highest_gwa = ""
        highest_gwa = float("-inf")
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    line = line.strip()
                    if " - " in line:
                        name, gwa = line.split(" - ")
                        name = name.strip().title()
                        gwa = float(gwa.strip())