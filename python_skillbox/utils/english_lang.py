import time

from selene.support.conditions import have
from selene.support.shared import browser


def assert_english_language():
    try:
        browser.element("div.auth-card__title").should(
            have.text("Log in to your profile")
        )
    except:
        browser.element("img.selected-language__image").click()
        browser.all(".ui-sb-16r ui-sb-dropdown-item-title").element_by(
            have.text("English")
        ).click()
        time.sleep(3)