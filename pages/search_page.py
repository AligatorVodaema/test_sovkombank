from .base_page import BasePage
from .locators import MainSearchPageLocators, SEARCH_WORD, EXPECTED_SITE
from selenium.webdriver.common.keys import Keys


class MainSearchPage(BasePage):
    """Class for interactions with main search page."""
    def should_be_search_page(self):
        """Run all checks for ensure about this
        is search page."""
        self.should_be_search_field()

    def should_be_search_field(self):
        """Check the search field."""
        assert self.is_element_present(
            *MainSearchPageLocators.SEARCH_FIELD), \
            'Search field is not presented'

    def should_be_images_link(self):
        """Check images icon link."""
        assert self.is_element_present(
            *MainSearchPageLocators.IMAGES_ICON_LINK
        ), 'Images icon link is not presented'

    def type_a_word_to_search_field(self):
        """Type the word in search field."""
        search_field = self.browser.find_element(
            *MainSearchPageLocators.SEARCH_FIELD)
        search_field.send_keys(SEARCH_WORD)

    def should_be_drop_down_list(self):
        """Check drop-down list of suggestions."""
        assert self.is_element_present(
            *MainSearchPageLocators.SUGGESTIONS_LIST
        ), 'Drop-down list is not presented'

    def should_be_search_word_in_suggestions_list(self):
        """Check is there the word in suggestions."""
        all_suggestions = self.browser.find_elements(
            *MainSearchPageLocators.SUGGESTIONS_LIST
        )
        for suggest in all_suggestions:
            assert SEARCH_WORD.lower() in suggest.text.lower(), \
                'Search word is not in sugggestions drop-down list'

    def should_be_table_of_results_after_search(self):
        """Is there a table of results after search the word."""
        assert self.is_element_present(
            *MainSearchPageLocators.RESULT_TABLE_OF_SEARCH
        ), 'Result table of search is not presented'

    def move_to_result_table_when_press_enter(self):
        """Go to result table after search. Using ENTER."""
        self.browser.find_element(
            *MainSearchPageLocators.SEARCH_FIELD
        ).send_keys(Keys.ENTER)

    def get_images_url(self):
        """Get the href attribute with url from images icon."""
        images_link = self.browser.find_element(
            *MainSearchPageLocators.IMAGES_ICON_LINK
        ).get_attribute('href')
        return images_link

    def should_be_special_url_in_first_five_results(self):
        """Checking the first five links on the result of table."""
        first_results = self.browser.find_elements(
            *MainSearchPageLocators.FIRST_TEN_RESULT_AFTER_SEARCH
        )
        total_number_of_links_found = 0
        for single_result in first_results[:5]:
            assert EXPECTED_SITE in single_result.text,\
                f'Expected "{EXPECTED_SITE}" link, got "{single_result.text}".' \
                f' Total number of link found:{total_number_of_links_found}.'
            total_number_of_links_found += 1

