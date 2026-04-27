from student_highest_gwa import StudentHighestGwa

def main():
    handler = StudentHighestGwa("students.txt")
    handler.read_and_find_highest()

if __name__ == "__main__":
    main()
