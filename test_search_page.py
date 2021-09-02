import pytest
from pages.search_page import MainSearchPage


@pytest.mark.search_story
def test_user_can_see_result_of_search(browser):
    """User story where he search a word in search-field and he can
    see the suggestions in drop-down menu."""
    link = 'https://yandex.ru/'
    page = MainSearchPage(browser=browser, url=link)
    page.open()
    page.should_be_search_page()
    page.type_a_word_to_search_field()
    page.should_be_drop_down_list()
    page.should_be_search_word_in_suggestions_list()
    return page


@pytest.mark.search_story
@pytest.mark.xfail(reason='There are no 5 links in the final table of results yet')
def test_user_can_see_first_five_expected_urls(browser):
    """User story where he expects to see the first five
    identical links after search the word in search-field."""
    page = test_user_can_see_result_of_search(browser)
    page.move_to_result_table_when_press_enter()
    page.should_be_table_of_results_after_search()
    page.should_be_special_url_in_first_five_results()
