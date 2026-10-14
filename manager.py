
"""
manager.py
----------
Coordinates the student and job objects with the analyzers,
then prints a complete analysis report.
"""

from analyzers import MatchScoreCalculator, MissingSkillDetector


class Manager:
    """
    Accepts a student and a job, runs both analyzers through
    the shared SkillAnalyzer interface (polymorphism), and
    displays the full report.
    """

    def __init__(self, student, job):
        self._student = student
        self._job = job

        # Both analyzers share the same analyze() interface.
        self._analyzers = [
            MatchScoreCalculator(),
            MissingSkillDetector(),
        ]

    def run_analysis(self):
        """
        Run every analyzer using polymorphism.
        Each analyzer implements analyze() differently.
        """
        match_result = None
        missing_skills = None

        for analyzer in self._analyzers:
            result = analyzer.analyze(self._student, self._job)

            if isinstance(result, dict):
                match_result = result
            elif isinstance(result, list):
                missing_skills = result

        # Validate analyzer results before displaying the report.
        if match_result is None or missing_skills is None:
            raise ValueError(
                "Analysis failed: one or more analyzers "
                "returned an unexpected result."
            )

        self._display_report(match_result, missing_skills)

    def _display_report(self, match_result, missing_skills):
        """Print the complete student-job skill analysis report."""

        print("=" * 50)
        print("STUDENT-JOB SKILL ANALYSIS REPORT")
        print("=" * 50)
        print()

        print("Student Name:", self._student.get_name())
        print()

        print("Job Title:", self._job.get_title())
        print()

        print("Required Skills:", match_result["total_required"])
        print()

        # Display matching skills.
        print("Matching Skills:")

        if not match_result["matching_skills"]:
            print("- None")
        else:
            for skill in match_result["matching_skills"]:
                print("-", skill)

        print()

        # Display missing skills.
        print("Missing Skills:")

        if not missing_skills:
            print("- None")
        else:
            for skill in missing_skills:
                print("-", skill)

        print()

        # Calculate and display the match percentage.
        percentage = match_result["percentage"]

        if percentage == int(percentage):
            formatted_percentage = str(int(percentage))
        else:
            formatted_percentage = "{:.1f}".format(percentage)

        print("Match Score: {}%".format(formatted_percentage))
        print()

        # Explain the score.
        print("Explanation:")

        print(
            "The student matches {} out of {} unique required skills. "
            "Therefore, the skill match percentage is {}%.".format(
                match_result["match_count"],
                match_result["total_required"],
                formatted_percentage,
            )
        )

        print()
        print("=" * 50)