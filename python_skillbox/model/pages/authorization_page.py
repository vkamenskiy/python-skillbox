import time

from selene.support.conditions import have
from selene.support.shared import browser
from python_skillbox.utils.english_lang import assert_english_language


class AuthorizationPage:
    def given_opened(self):
        browser.open("")

        browser.element(".menu-nav-desktop__item--auth").click()
        browser.switch_to_next_tab()

        assert_english_language()
        return self

    def input_email(self, email):
        browser.element("#ui-sb-input-element-0").type(email).press_tab()
        return self

    def input_password(self, password):
        browser.element("#ui-sb-input-element-1").type(password)
        return self

    def check_error_message(self, error_text):
        browser.element("ui-sb-error.ng-star-inserted").should(
            have.text(error_text)
        )
        return self

    def click_log_in_button(self):
        browser.element(".ui-sb-button--default").click()
        return self


class ForgotPassword:
    def given_opened(self):
        AuthorizationPage().given_opened()

        browser.element('a.auth-login__reset-link').click()
        time.sleep(1)
        return self

    def input_email(self, email):
        browser.element('[id^=ui-sb-input-element-]').type(email)
        return self

    def click_send_button(self):
        browser.element('.ui-sb-button--full').click()
        return self

    def check_successful_message(self, text):
        browser.element('div.auth-card__title').should(have.text(text))
        return self





