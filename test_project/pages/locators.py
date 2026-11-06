""" Locators for tests. """

from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BUTTON_VIEW_BUSKET = (By.CSS_SELECTOR, 'div .basket-mini .btn:nth-child(1)')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')

    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTRATION_PASWD = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTRATION_CONFIRM_PASWD = (By.CSS_SELECTOR, '[name="registration-password2"]')
    BUTTON_REGISTER = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.XPATH, '//form[@class="add-to-basket"]/button')

    MESSAGE_WITH_PRODUCT_NAME = (By.CSS_SELECTOR, 'div.alert:nth-child(1)')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    PRODUCT_NAME_IN_CARD = (By.CSS_SELECTOR, '.product_main h1')

    MESSAGE_OF_BASKET_COST = (By.CSS_SELECTOR, 'div.alert:nth-child(3)')
    BASKET_COST_IN_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner p strong')
    COST_OF_PRODUCT = (By.CSS_SELECTOR, '.price_color:nth-child(2)')


class BasketPageLocators():
    BASKET_LIST = (By.CSS_SELECTOR, '.basket-title')
    NOTIFICATION_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')


class EducationalPageLocators():
    PORTAL_TITLE = (By.ID, 'portal-title')
    STUDENT_BADGE = (By.ID, 'student-status-badge')
    PROGRESS_BAR = (By.ID, 'course-progress-bar')
    PROGRESS_STATUS = (By.ID, 'progress-status-text')

    # Enrollment
    INPUT_STUDENT_NAME = (By.ID, 'student-name')
    INPUT_STUDENT_EMAIL = (By.ID, 'student-email')
    SELECT_COURSE_TRACK = (By.ID, 'course-select')
    BUTTON_ENROLL_SUBMIT = (By.ID, 'btn-enroll-submit')
    ENROLLMENT_SUCCESS_ALERT = (By.ID, 'enrollment-success-alert')
    ENROLLED_STUDENT_NAME = (By.ID, 'enrolled-student-name')

    # Content Delivery
    TAB_LESSON_1 = (By.ID, 'tab-lesson-1')
    TAB_LESSON_2 = (By.ID, 'tab-lesson-2')
    TAB_LESSON_3 = (By.ID, 'tab-lesson-3')
    LESSON_TITLE = (By.ID, 'lesson-title')
    LESSON_TEXT = (By.ID, 'lesson-text')
    BUTTON_COMPLETE_LESSON = (By.ID, 'btn-complete-lesson')

    # Multimedia & Iframe
    IFRAME_VIDEO = (By.ID, 'lecture-video-iframe')
    IFRAME_VIDEO_TITLE = (By.ID, 'video-title')
    IFRAME_BUTTON_PLAY = (By.ID, 'btn-play-video')
    IFRAME_VIDEO_STATUS = (By.ID, 'video-status')

    # Quiz Submission
    QUIZ_Q1_OPTION_POM = (By.ID, 'q1-opt2')
    QUIZ_Q2_OPTION_SWITCH = (By.ID, 'q2-opt1')
    BUTTON_QUIZ_SUBMIT = (By.ID, 'btn-quiz-submit')
    QUIZ_RESULT_BANNER = (By.ID, 'quiz-result')
