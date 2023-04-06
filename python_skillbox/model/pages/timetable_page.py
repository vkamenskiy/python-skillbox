from selene.support.conditions import have
from selene.support.shared import browser


class TimetablePage:
    def given_opened(self):
        browser.open("")

        browser.element(
            ".menu-nav-desktop__list > li:nth-child(2) > .menu-desktop-item > button.menu-desktop-item__link"
        ).hover()
        browser.all(".dropdown-desktop__link").element_by(have.text("Расписание")).click()
        browser.switch_to_next_tab()

    def check_filter_tags(self, tags):
        browser.all(".filter__directions button .ui-chip__text").should(
            have.texts(tags)
        )