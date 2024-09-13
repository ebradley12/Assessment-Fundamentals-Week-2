"""Importing modules"""
from datetime import datetime, date


#####
#
# COPY YOUR CODE FROM LEVEL 1 BELOW
#
#####

VALID_TYPES = ["multiple-choice", "technical", "presentation"]

# pylint: disable=too-few-public-methods


class Assessment:
    """A class representing assessments for trainees."""

    def __init__(self, assessment_name: str, type: str, score: float) -> None:
        """Initialises an assessment name, type and score."""
        self.assessment_name = assessment_name
        self.type = type
        self.score = score

        if self.type not in VALID_TYPES:
            raise ValueError(
                f"Assessment type is invalid. Type must be one of {VALID_TYPES}")

        if not 0 <= self.score <= 100:
            raise ValueError("Score must be between 0-100.")


class Trainee:
    """A class representing a trainee."""

    def __init__(self, name: str, email: str, date_of_birth: date) -> None:
        """Initialises a trainee's name, email, date of birth and list of assessments."""
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = []

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
        if not isinstance(assessment, Assessment):
            raise TypeError("Only assessments can be added.")
        self.assessments.append(assessment)

    def get_assessment(self, name: str):
        """Returns an assessment object."""
        for assessment in self.assessments:
            if assessment.assessment_name == name:
                return assessment
        return None

    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        """Returns a list of assessments of a given type."""
        return [assessment for assessment in self.assessments if assessment.type == type]

        #####
        #
        # COPY YOUR CODE FROM LEVEL 1 ABOVE
        #
        #####


class MultipleChoiceAssessment(Assessment):
    """A class representing the multiple choice assessment type."""

    def __init__(self, assessment_name: str, score: float) -> None:
        super().__init__(assessment_name, "multiple-choice", score)

    def calculate_score(self) -> float:
        """Calculates the score for the multiple choice assessment."""
        return self.score * 0.70


class TechnicalAssessment(Assessment):
    """A class representing the technical assessment type."""

    def __init__(self, assessment_name: str, score: float) -> None:
        super().__init__(assessment_name, "technical", score)

    def calculate_score(self) -> float:
        """Calculates the score for the multiple choice assessment."""
        return self.score * 1


class PresentationAssessment(Assessment):
    """A class representing the presentation assessment type."""

    def __init__(self, assessment_name: str, score: float) -> None:
        super().__init__(assessment_name, "presentation", score)

    def calculate_score(self) -> float:
        """Calculates the score for the multiple choice assessment."""
        return self.score * 0.6


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
