import time

import allure
import pytest
from allure_commons.types import Severity

from python_skillbox.model import app
from python_skillbox.data import footer, filter


@allure.tag("ui", "web")
@allure.label('owner', 'vkamenskiy')
@allure.feature('UI')
@allure.story('Authorization')
class TestsAuthorization:
    @allure.severity(Severity.NORMAL)
    @allure.title('Input wrong email format')
    @pytest.mark.skip()
    def test_wrong_email_format(self, setup_browser):

        with allure.step('Open authorization page'):
            app.authorization_page.given_opened()

        with allure.step('Input wrong email'):
            app.authorization_page.input_email("test")

        with allure.step('Check error message'):
            app.authorization_page.check_error_message("Invalid e-mail format")

    @allure.severity(Severity.NORMAL)
    @allure.title('Input wrong email and password combination')
    def test_wrong_email_and_password_combination(self, setup_browser):

        with allure.step('Open authorization page'):
            app.authorization_page.given_opened()

        with allure.step('Input wrong email and password'):
            app.authorization_page.input_email("test@test.ru")
            app.authorization_page.input_password("1234")

        with allure.step('Check error message'):
            app.authorization_page.click_log_in_button()
            app.authorization_page.check_error_message(
            "User with this e-mail and password combination is not found"
        )

    @allure.severity(Severity.NORMAL)
    @allure.title('Check password recovery work')
    def test_password_recovery_work(self, setup_browser):

        with allure.step('Open forgot password page'):
            app.forgot_password_page.given_opened()

        with allure.step('Input email'):
            app.forgot_password_page.input_email("test@test.ru")

        with allure.step('Check successful message'):
            app.forgot_password_page.click_send_button()
            app.forgot_password_page.check_successful_message("Check your mail")


@allure.tag("ui", "web")
@allure.label('owner', 'vkamenskiy')
@allure.feature('UI')
@allure.story('Search')
class TestsSearch:
    @allure.severity(Severity.NORMAL)
    @allure.title('Check search on the home page works')
    def test_search_on_the_home_page_works(self, setup_browser):

        with allure.step('Open home page'):
            app.main_page.given_opened()

        with allure.step('Input search query'):
            app.main_page.input_search("Профессия Python-разработчик")

        with allure.step('Check for success'):
            app.main_page.check_for_success()

    @allure.severity(Severity.NORMAL)
    @allure.title('Check search on the webinars page works')
    @pytest.mark.skip()
    def test_search_webinars_work(self, setup_browser):

        with allure.step('Open webinars page'):
            app.webinars_page.given_opened()

        with allure.step('Input search query'):
            app.webinars_page.input_search("Веб-дизайн на Figma: подводим итоги")

        with allure.step('Check for success'):
            app.webinars_page.check_for_success()


@allure.tag("ui", "web")
@allure.label('owner', 'vkamenskiy')
@allure.feature('UI')
@allure.story('Footer')
class TestFooter:
    @allure.severity(Severity.TRIVIAL)
    @allure.title('Footer subheading display correctly')
    def test_footer_subtitles_display_correctly(self, setup_browser):

        with allure.step('Open home page'):
            app.main_page.given_opened()

        with allure.step('Check subtitles display correctly'):
            app.footer.subtitles_fields(footer.fields)
            app.footer.subtitles_about(footer.about)
            app.footer.subtitles_projects(footer.projects)
            app.footer.subtitles_collaborations(footer.collaborations)


@allure.tag("ui", "web")
@allure.label('owner', 'vkamenskiy')
@allure.feature('UI')
@allure.story('Webinars')
class TestWebinars:
    @allure.severity(Severity.TRIVIAL)
    @allure.title('36 webinars are visible on the page')
    def test_36_webinars_are_visible_on_the_page(self, setup_browser):

        with allure.step('Open webinars page'):
            app.webinars_page.given_opened()

        with allure.step('Check standart count'):
            app.webinars_page.check_standard_count()

    @allure.severity(Severity.TRIVIAL)
    @allure.title('Another 36 webinars are visible on the page')
    # @pytest.mark.skip()
    def test_another_36_webinars_are_visible_on_the_page(self, setup_browser):

        with allure.step('Open webinars page'):
            app.webinars_page.given_opened()

        with allure.step('Check standart count'):
            app.webinars_page.check_standard_count()
        time.sleep(3)

        with allure.step('Check webinars count after click at "more button"'):
            app.webinars_page.click_more_button()
            app.webinars_page.check_webinars_count_after_more_button()


@allure.tag("ui", "web")
@allure.label('owner', 'vkamenskiy')
@allure.feature('UI')
@allure.story('Filter')
class TestFilter:
    @allure.severity(Severity.TRIVIAL)
    @allure.title('Webinars filter tags display correctly')
    def test_webinars_filter_tags_display_correctly(self, setup_browser):

        with allure.step('Open webinars page'):
            app.webinars_page.given_opened()

        with allure.step('Check filter tags'):
            app.webinars_page.check_filter_tags(filter.tags)

        assert 1==2

    @allure.severity(Severity.TRIVIAL)
    @allure.title('Playlists filter tags display correctly')
    def test_playlists_filter_tags_display_correctly(self, setup_browser):

        with allure.step('Open playlists page'):
            app.playlists_page.given_opened()

        with allure.step('Check filter tags'):
            app.playlists_page.check_filter_tags(filter.tags)

    @allure.severity(Severity.TRIVIAL)
    @allure.title('Timetable filter tags display correctly')
    def test_timetable_filter_tags_display_correctly(self, setup_browser):

        with allure.step('Open timetable page'):
            app.timetable_page.given_opened()

        with allure.step('Check filter tags'):
            app.timetable_page.check_filter_tags(filter.tags)

        # assert 1==2
