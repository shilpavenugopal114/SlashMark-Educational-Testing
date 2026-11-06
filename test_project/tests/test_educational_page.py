""" Tests for Educational Website Testing (SlashMark Task 5).
Validates:
1. Student Enrollment
2. Content Delivery
3. Multimedia & iframe handling
4. Quiz Submissions
5. Progress Tracking

To run all educational tests:
pytest -v -s --tb=line test_project/tests/test_educational_page.py
"""

import os
import pytest
from .. import EducationalPage

# Path to the bundled educational demo platform
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DEMO_LMS_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "demo_lms", "index.html"))
DEMO_LMS_URL = f"file:///{DEMO_LMS_PATH.replace(os.sep, '/')}"


@pytest.fixture(scope="function")
def educational_page(browser):
    """ Helper fixture to open the educational demo platform. """
    page = EducationalPage(browser, DEMO_LMS_URL)
    page.open()
    return page


@pytest.mark.educational
class TestEducationalWebsite:
    """ Test Suite for Task 5: Automation Testing of Educational Websites. """

    def test_01_portal_access(self, educational_page):
        """ Validate educational platform loads correctly. """
        educational_page.should_be_educational_portal()

    def test_02_student_enrollment(self, educational_page):
        """ Validate student course enrollment workflow. """
        student_name = "Alex Johnson"
        student_email = "alex.johnson@example.com"
        educational_page.enroll_student(student_name, student_email, "selenium-automation")
        educational_page.should_be_enrollment_success(student_name)
        educational_page.verify_progress_tracking(min_percentage=25)

    def test_03_content_delivery(self, educational_page):
        """ Validate educational content delivery across modules and syllabus lessons. """
        # Switch to Module / Lesson 2
        educational_page.select_lesson_module(2)
        educational_page.should_be_lesson_content("Locators")

        # Switch to Module / Lesson 3
        educational_page.select_lesson_module(3)
        educational_page.should_be_lesson_content("Page Object Model")

    def test_04_multimedia_and_iframe_handling(self, educational_page):
        """ Validate multimedia video playback embedded inside an iframe. """
        # 1. Switch context to iframe
        educational_page.switch_to_multimedia_iframe()

        # 2. Interact with media player inside the iframe
        educational_page.play_multimedia_video_in_iframe()

        # 3. Switch back to top-level window
        educational_page.switch_to_default_content()

    def test_05_quiz_submission(self, educational_page):
        """ Validate interactive quiz submission and grading feedback. """
        educational_page.submit_course_quiz()
        educational_page.should_be_quiz_passed()

    def test_06_progress_tracking_and_completion(self, educational_page):
        """ Validate progress tracking updates through student learning activities. """
        # Step 1: Enroll student (adds 25% progress)
        educational_page.enroll_student("Sarah Connor", "sarah@example.com")
        educational_page.verify_progress_tracking(min_percentage=25)

        # Step 2: Complete course lesson (adds 25% progress -> 50%)
        educational_page.complete_lesson()
        educational_page.verify_progress_tracking(min_percentage=50)

        # Step 3: Complete quiz (adds 50% progress -> 100%)
        educational_page.submit_course_quiz()
        educational_page.should_be_quiz_passed()

        # Step 4: Verify 100% completion progress bar
        educational_page.verify_progress_tracking(min_percentage=100)

