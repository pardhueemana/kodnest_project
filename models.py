"""
models.py
---------
Data classes that store student and job information.
Skills are cleaned (spaces trimmed) and normalized for matching.
Original readable skill names are kept for the final report.
"""


class StudentProfile:
    """Stores a student's name and skills."""

    def __init__(self, student_name, student_skills):
        self._student_name = student_name
        # Original names (spaces trimmed, first occurrence kept)
        self._original_skills = []
        # Normalized names (lowercase) used for comparison
        self._student_skills = self._normalize_skills(student_skills)

    def _normalize_skills(self, skills):
        """
        Remove extra spaces, convert to lowercase, and drop duplicates.
        Uses lists and loops only (no sets).
        """
        normalized = []

        if skills is None:
            return normalized

        for skill in skills:
            cleaned = skill.strip()
            if cleaned == "":
                continue

            lower_skill = cleaned.lower()

            # Skip if this skill was already added
            already_added = False
            for existing in normalized:
                if existing == lower_skill:
                    already_added = True
                    break

            if not already_added:
                normalized.append(lower_skill)
                self._original_skills.append(cleaned)

        return normalized

    def get_name(self):
        return self._student_name

    def get_skills(self):
        """Return normalized (lowercase) unique skills."""
        return self._student_skills

    def get_original_skills(self):
        """Return readable skill names with original casing."""
        return self._original_skills


class JobDescription:
    """Stores a job title and its required skills."""

    def __init__(self, job_title, required_skills):
        self._job_title = job_title
        self._original_skills = []
        self._required_skills = self._normalize_skills(required_skills)

    def _normalize_skills(self, skills):
        """
        Remove extra spaces, convert to lowercase, and drop duplicates.
        Empty skill lists are handled safely (returns []).
        """
        normalized = []

        if skills is None or len(skills) == 0:
            return normalized

        for skill in skills:
            cleaned = skill.strip()
            if cleaned == "":
                continue

            lower_skill = cleaned.lower()

            already_added = False
            for existing in normalized:
                if existing == lower_skill:
                    already_added = True
                    break

            if not already_added:
                normalized.append(lower_skill)
                self._original_skills.append(cleaned)

        return normalized

    def get_title(self):
        return self._job_title

    def get_required_skills(self):
        """Return normalized (lowercase) unique required skills."""
        return self._required_skills

    def get_original_skills(self):
        """Return readable required skill names with original casing."""
        return self._original_skills

    def get_skill_count(self):
        """Return the number of unique required skills."""
        return len(self._required_skills)