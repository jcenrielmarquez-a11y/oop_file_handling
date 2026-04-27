class StudentHighestGwa:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_and_find_highest(self):
        name_with_highest_gwa = ""
        highest_gwa = float("-inf")
        