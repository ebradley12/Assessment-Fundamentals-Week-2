from datetime import datetime, date

VALID_TYPES = ["multiple-choice", "technical", "presentation"]


class Assessment:
    """A class representing assessments for trainees."""

    def __init__(self, name: str, type: str, score: float) -> None:
        """Initialises an assessment name, type and score."""
        self.name = name
        self.type = type
        self.score = score

        if self.type not in VALID_TYPES:
            raise ValueError(
                f"Assessment type is invalid. Type must be one of {VALID_TYPES}")

        if not 0 <= self.score <= 100:
            raise ValueError("Score must be between 0-100.")


class Trainee:
    """A class representing a trainee."""

    def __init__(self, name: str, email: str, date_of_birth: date, assessments: list[Assessment]) -> None:
        """Initialises a trainee's name, email, date of birth and list of assessments."""
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = assessments

    def get_age(self) -> int:
        """Calculates and returns the age of a trainee in years."""
        current_date = datetime.today().date()
        dob = self.date_of_birth
        age = current_date.year - dob.year
        if (current_date.month, current_date.day) < (dob.month, dob.day):
            age -= 1
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        """Add's an assessment to the trainee's list of assessments."""
        self.assessments.append(assessment)

    def get_assessment(self, name: str):
        """Returns an assessment object."""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
