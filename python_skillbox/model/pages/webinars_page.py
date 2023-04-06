from selene.support.conditions import have
from selene.support.shared import browser
from selene import command


class WebinarsPage:
    def given_opened(self):
        browser.open("")
        browser.element(
            ".menu-nav-desktop__list > li:nth-child(2) > .menu-desktop-item > button.menu-desktop-item__link"
        ).hover()
        browser.all(".dropdown-desktop__link").element_by(
            have.text("Все вебинары")
        ).perform(command.js.click)
        browser.switch_to_next_tab()

    def input_search(self, text):
        browser.element("#search-desktop").type(text).press_enter()

    def check_for_success(self):
        browser.element(".webinars-info__count").should(have.text("1 вебинар"))

    def check_standard_count(self):
        browser.all(".webinars__list > li").should(have.size(36))

    def click_more_button(self):
        browser.element("button.ui-button--stroke-main").click()

    def check_webinars_count_after_more_button(self):
        browser.all(".webinars__list > li").should(have.size(72))

    def check_filter_tags(self, tags):
        browser.all(".filter-directions .ui-chip__text").should(have.texts(tags))
