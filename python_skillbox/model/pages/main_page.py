from selene.support.conditions import be, have
from selene.support.shared import browser


class MainPage:
    def given_opened(self):
        browser.open("")

    def input_search(self, text):
        browser.element(".ui-search__input").type(text)
        browser.element("button.start-screen__search-button").click()

    def check_for_success(self):
        browser.element('.courses-block__title').should(be.visible)


class Footer:
    def subtitles_fields(self, subtitles):
        browser.all(
            ".ui-footer-nav-list__section:nth-child(1) .ui-footer-nav-list__links li"
        ).should(have.texts(subtitles))

    def subtitles_about(self, subtitles):
        browser.all(
            ".ui-footer-nav-list__section:nth-child(2) .ui-footer-nav-list__links li"
        ).should(
            have.texts(subtitles)
        )

    def subtitles_projects(self, subtitles):
        browser.all(
            ".ui-footer-nav-list__section:nth-child(3) .ui-footer-nav-list__links li"
        ).should(have.texts(subtitles))

    def subtitles_collaborations(self, subtitles):
        browser.all(
            ".ui-footer-nav-list__section:nth-child(4) .ui-footer-nav-list__links li"
        ).should(
            have.texts(subtitles)
        )



