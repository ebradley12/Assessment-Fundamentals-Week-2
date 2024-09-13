
"""Importing modules"""
from datetime import datetime, date

# pylint: disable = redefined-builtin
# pylint: disable = redefined-outer-name


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


#####
#
# COPY YOUR CODE FROM LEVEL 2 ABOVE
#
#####


class Question:
    """A class for question in a quiz."""

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer

    def is_correct(self) -> bool:
        """Checks if a chosen answer is correct."""
        if self.chosen_answer == self.correct_answer:
            return True
        return False


class Quiz:
    """A class for a quiz."""

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:
    """A class that helps us to mark assessments."""

    def __init__(self, quiz: Quiz) -> None:
        """Initialises quiz object."""
        self._quiz = quiz

    def mark(self) -> int:
        """Returns the mark for the assessment as a percentage."""
        points = 0
        quiz_questions = self._quiz.questions
        total_questions = len(quiz_questions)
        if len(quiz_questions) == 0:
            return 0
        for question in quiz_questions:
            if question.is_correct():
                points += 1
        return round((points / total_questions) * 100)

    def generate_assessment(self) -> Assessment:
        """Returns an instance of an assessment with the correct name and score."""
        quiz_type = self._quiz.type
        score = self.mark()
        if quiz_type == 'multiple-choice':
            return MultipleChoiceAssessment(self._quiz.name, score)
        if quiz_type == 'technical':
            return TechnicalAssessment(self._quiz.name, score)
        if quiz_type == 'presentation':
            return PresentationAssessment(self._quiz.name, score)
        raise ValueError("Invalid quiz type!")


if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
