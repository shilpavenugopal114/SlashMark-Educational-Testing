""" Page Object for Educational Website Testing (Task 5). """

from .base_page import BasePage
from .locators import EducationalPageLocators
from .. import LOGGER


class EducationalPage(BasePage):
    """ Page actions and validations for Educational Learning Platform. """

    def should_be_educational_portal(self):
        """ Verify portal title is visible and matches expectations. """
        assert self.is_element_present(*EducationalPageLocators.PORTAL_TITLE), \
            LOGGER.error("Educational portal title is not presented")
        title_text = self.browser.find_element(*EducationalPageLocators.PORTAL_TITLE).text
        assert "EduTech LMS" in title_text, f"Unexpected portal title: {title_text}"

    def enroll_student(self, student_name, student_email, course_value="selenium-automation"):
        """ Fill in enrollment details and submit enrollment form. """
        name_input = self.browser.find_element(*EducationalPageLocators.INPUT_STUDENT_NAME)
        name_input.clear()
        name_input.send_keys(student_name)

        email_input = self.browser.find_element(*EducationalPageLocators.INPUT_STUDENT_EMAIL)
        email_input.clear()
        email_input.send_keys(student_email)

        course_select = self.browser.find_element(*EducationalPageLocators.SELECT_COURSE_TRACK)
        course_select.send_keys(course_value)

        enroll_btn = self.browser.find_element(*EducationalPageLocators.BUTTON_ENROLL_SUBMIT)
        enroll_btn.click()

    def should_be_enrollment_success(self, expected_name):
        """ Validate enrollment success confirmation badge and alert message. """
        assert self.is_element_present(*EducationalPageLocators.ENROLLMENT_SUCCESS_ALERT), \
            LOGGER.error("Enrollment success alert was not displayed")
        displayed_name = self.browser.find_element(*EducationalPageLocators.ENROLLED_STUDENT_NAME).text
        assert expected_name in displayed_name, \
            f"Expected student {expected_name} in alert, found {displayed_name}"

    def select_lesson_module(self, lesson_num=2):
        """ Switch to specific course content lesson tab. """
        if lesson_num == 2:
            tab = self.browser.find_element(*EducationalPageLocators.TAB_LESSON_2)
        elif lesson_num == 3:
            tab = self.browser.find_element(*EducationalPageLocators.TAB_LESSON_3)
        else:
            tab = self.browser.find_element(*EducationalPageLocators.TAB_LESSON_1)
        tab.click()

    def should_be_lesson_content(self, expected_title_keyword):
        """ Verify lesson content has been updated and delivered. """
        title_element = self.browser.find_element(*EducationalPageLocators.LESSON_TITLE)
        assert expected_title_keyword.lower() in title_element.text.lower(), \
            f"Expected lesson title containing '{expected_title_keyword}', got '{title_element.text}'"

    def complete_lesson(self):
        """ Click mark lesson complete and accept browser alert. """
        complete_btn = self.browser.find_element(*EducationalPageLocators.BUTTON_COMPLETE_LESSON)
        complete_btn.click()
        # Handle browser alert popup
        alert = self.browser.switch_to.alert
        LOGGER.info(f"Accepted lesson alert: {alert.text}")
        alert.accept()

    def verify_progress_tracking(self, min_percentage=25):
        """ Validate dynamic progress bar updates. """
        bar = self.browser.find_element(*EducationalPageLocators.PROGRESS_BAR)
        progress_text = bar.text.replace('%', '').strip()
        progress_value = int(progress_text) if progress_text.isdigit() else 0
        assert progress_value >= min_percentage, \
            f"Expected at least {min_percentage}% progress, but found {progress_value}%"

    def switch_to_multimedia_iframe(self):
        """ Switch WebDriver focus to the embedded multimedia iframe. """
        iframe_element = self.browser.find_element(*EducationalPageLocators.IFRAME_VIDEO)
        self.browser.switch_to.frame(iframe_element)

    def switch_to_default_content(self):
        """ Switch WebDriver focus back to the top-level window. """
        self.browser.switch_to.default_content()

    def play_multimedia_video_in_iframe(self):
        """ Interact with the video player element inside the iframe. """
        assert self.is_element_present(*EducationalPageLocators.IFRAME_VIDEO_TITLE), \
            LOGGER.error("Video title inside iframe not present")
        play_btn = self.browser.find_element(*EducationalPageLocators.IFRAME_BUTTON_PLAY)
        play_btn.click()
        status = self.browser.find_element(*EducationalPageLocators.IFRAME_VIDEO_STATUS).text
        assert "Playing" in status, f"Video did not start playing. Status: {status}"

    def submit_course_quiz(self):
        """ Select answers and submit course evaluation quiz. """
        opt1 = self.browser.find_element(*EducationalPageLocators.QUIZ_Q1_OPTION_POM)
        opt1.click()

        opt2 = self.browser.find_element(*EducationalPageLocators.QUIZ_Q2_OPTION_SWITCH)
        opt2.click()

        submit_btn = self.browser.find_element(*EducationalPageLocators.BUTTON_QUIZ_SUBMIT)
        submit_btn.click()

    def should_be_quiz_passed(self):
        """ Assert quiz passed successfully with top score. """
        assert self.is_element_present(*EducationalPageLocators.QUIZ_RESULT_BANNER), \
            LOGGER.error("Quiz result banner is not presented")
        result_text = self.browser.find_element(*EducationalPageLocators.QUIZ_RESULT_BANNER).text
        assert "Passed" in result_text, f"Quiz was not passed: {result_text}"

