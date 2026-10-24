class InvalidMarksError(Exception):
    """Raised when student marks are outside 0 to 100."""


class Course:
    """Manage a course and its students' marks."""

    def __init__(self, name: str) -> None:
        """Initialize the course."""
        self.name = name
        self.marks = {}

    def add_student(self, student: str, marks: int) -> None:
        """Add a student after validating marks."""
        if not 0 <= marks <= 100:
            raise InvalidMarksError(
                f"Invalid marks for {student}: {marks}"
            )
        self.marks[student] = marks

    def remove_student(self, name: str) -> None:
        """Remove a student, or raise KeyError if missing."""
        if name not in self.marks:
            raise KeyError(f"No student named {name}")
        del self.marks[name]

    def average(self) -> float:
        """Calculate the average marks."""
        if not self.marks:
            return 0.0
        return sum(self.marks.values()) / len(self.marks)

    def top_student(self):
        """Return the student with the highest marks."""
        if not self.marks:
            return None
        return max(self.marks, key=self.marks.get)

    def __len__(self) -> int:
        """Return the number of students."""
        return len(self.marks)

    def __str__(self) -> str:
        """Return a readable course summary."""
        count = len(self)
        noun = "student" if count == 1 else "students"
        return (
            f"{self.name}: {count} {noun}, "
            f"average {self.average():.1f}"
        )


def load_course(name: str, filename: str) -> Course:
    """Load student marks from a text file."""
    course = Course(name)

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                try:
                    student, mark = line.split(",")
                    marks = int(mark)
                except ValueError:
                    print(f"Skipping invalid line: {line}")
                    continue

                try:
                    course.add_student(student.strip(), marks)
                except InvalidMarksError as e:
                    print("Skipping:", e)

    except FileNotFoundError:
        print(f"File not found: {filename}")

    return course


if __name__ == "__main__":
    test = Course("Test")
    test.add_student("A", 50)
    test.add_student("B", 90)

    test.remove_student("A")
    print("After removing A:", test)
    print("Number of students:", len(test))

    try:
        test.remove_student("Zara")
    except KeyError as e:
        print("KeyError:", e)