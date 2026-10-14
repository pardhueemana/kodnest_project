"""
analyzers.py
------------
Skill analysis classes using inheritance and polymorphism.

SkillAnalyzer is the abstract base class.
MatchScoreCalculator and MissingSkillDetector override analyze().
"""

from abc import ABC, abstractmethod


class SkillAnalyzer(ABC):
    """
    Abstract base class for all skill analyzers.
    Child classes must implement the analyze() method.
    """

    @abstractmethod
    def analyze(self, student, job):
        """
        Compare a student profile with a job description.
        Must be overridden by every child class.
        """
        pass


class MatchScoreCalculator(SkillAnalyzer):
    """
    Finds matching skills and calculates the match percentage.

    Formula:
        Match % = (matching skills / total required skills) * 100

    Returns 0% when the job has no required skills.
    """

    def analyze(self, student, job):
        student_skills = student.get_skills()
        job_skills = job.get_required_skills()
        original_job_skills = job.get_original_skills()

        matching_skills = []

        # Compare every required job skill with student skills.
        index = 0

        while index < len(job_skills):
            required = job_skills[index].strip().lower()
            original_name = original_job_skills[index]

            is_match = False

            for student_skill in student_skills:
                if student_skill.strip().lower() == required:
                    is_match = True
                    break

            if is_match:
                # Prevent duplicate matching skills.
                already_counted = False

                for matched in matching_skills:
                    if matched.strip().lower() == required:
                        already_counted = True
                        break

                if not already_counted:
                    matching_skills.append(original_name)

            index += 1

        total_required = len(job_skills)

        if total_required == 0:
            percentage = 0.0
        else:
            percentage = (
                len(matching_skills) / total_required
            ) * 100

        return {
            "matching_skills": matching_skills,
            "match_count": len(matching_skills),
            "total_required": total_required,
            "percentage": percentage,
        }


class MissingSkillDetector(SkillAnalyzer):
    """
    Finds skills required by the job that the student does not have.
    Returns an empty list when the student has every required skill.
    """

    def analyze(self, student, job):
        student_skills = student.get_skills()
        job_skills = job.get_required_skills()
        original_job_skills = job.get_original_skills()

        missing_skills = []

        index = 0

        while index < len(job_skills):
            required = job_skills[index].strip().lower()
            original_name = original_job_skills[index]

            has_skill = False

            for student_skill in student_skills:
                if student_skill.strip().lower() == required:
                    has_skill = True
                    break

            if not has_skill:
                # Prevent duplicate missing skills.
                already_listed = False

                for missing in missing_skills:
                    if missing.strip().lower() == required:
                        already_listed = True
                        break

                if not already_listed:
                    missing_skills.append(original_name)

            index += 1

        return missing_skills