"""
main.py
-------
Entry point for the Student–Job Skill Analysis System.

Run with:
    python main.py
"""

from models import StudentProfile, JobDescription
from manager import Manager


def run_sample_analysis():
    """Demo with Gamana and two different job descriptions."""

    student = StudentProfile(
        student_name="Gamana",
        student_skills=["Python", "Java", "SQL", "HTML"],
    )

    job1 = JobDescription(
        job_title="Python Developer",
        required_skills=["Python", "Django", "SQL", "REST API", "Git"],
    )

    job2 = JobDescription(
        job_title="Frontend Developer",
        required_skills=["HTML", "CSS", "JavaScript", "React"],
    )

    print("\n>>> Analysis 1: Same student, Python Developer role\n")
    Manager(student, job1).run_analysis()

    print("\n>>> Analysis 2: Same student, Frontend Developer role\n")
    Manager(student, job2).run_analysis()


def run_edge_case_tests():
    """
    Test the required edge-case scenarios.
    Each test prints a short label, then the full report.
    """
    print("\n" + "#" * 50)
    print("EDGE CASE TESTS")
    print("#" * 50)

    # 1. Student has no matching skills
    print("\n--- Test 1: No matching skills ---\n")
    Manager(
        StudentProfile("Alex", ["C++", "Go"]),
        JobDescription("Python Developer", ["Python", "Django", "SQL"]),
    ).run_analysis()

    # 2. Student has all required skills
    print("\n--- Test 2: All required skills present ---\n")
    Manager(
        StudentProfile("Sam", ["Python", "Django", "SQL"]),
        JobDescription("Python Developer", ["Python", "Django", "SQL"]),
    ).run_analysis()

    # 3. Student has only some required skills
    print("\n--- Test 3: Partial match ---\n")
    Manager(
        StudentProfile("Gamana", ["Python", "Java", "SQL", "HTML"]),
        JobDescription("Python Developer", ["Python", "Django", "SQL", "REST API", "Git"]),
    ).run_analysis()

    # 4. Student has no skills
    print("\n--- Test 4: Student has no skills ---\n")
    Manager(
        StudentProfile("Jamie", []),
        JobDescription("Python Developer", ["Python", "SQL"]),
    ).run_analysis()

    # 5. Job has no required skills
    print("\n--- Test 5: Job has no required skills ---\n")
    Manager(
        StudentProfile("Taylor", ["Python", "SQL"]),
        JobDescription("Open Role", []),
    ).run_analysis()

    # 6. Uppercase / lowercase variations
    print("\n--- Test 6: Case variations ---\n")
    Manager(
        StudentProfile("Casey", ["python", "SQL", "html"]),
        JobDescription("Web Developer", ["Python", "sql", "HTML", "CSS"]),
    ).run_analysis()

    # 7. Extra spaces in skill names
    print("\n--- Test 7: Extra spaces ---\n")
    Manager(
        StudentProfile("Riley", ["  Python  ", " Java", "SQL "]),
        JobDescription("Backend Developer", ["Python", "  Django ", " SQL"]),
    ).run_analysis()

    # 8. Student skills contain duplicates
    print("\n--- Test 8: Duplicate student skills ---\n")
    Manager(
        StudentProfile("Morgan", ["Python", "python", "SQL", "SQL"]),
        JobDescription("Data Analyst", ["Python", "SQL", "Excel"]),
    ).run_analysis()

    # 9. Job requirements contain duplicates
    print("\n--- Test 9: Duplicate job skills ---\n")
    Manager(
        StudentProfile("Jordan", ["Python", "Git"]),
        JobDescription("DevOps Intern", ["Python", "Python", "Git", "git", "Docker"]),
    ).run_analysis()

    # 10. Both student and job have empty skill lists
    print("\n--- Test 10: Both skill lists empty ---\n")
    Manager(
        StudentProfile("Avery", []),
        JobDescription("Unspecified Role", []),
    ).run_analysis()


if __name__ == "__main__":
    run_sample_analysis()
    run_edge_case_tests()