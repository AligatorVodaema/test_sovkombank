from pages.search_page import MainSearchPage
from pages.images_page import ImagesSearchPage
import pytest


@pytest.mark.images_story
def test_user_can_watch_images(browser):
    """User story where he clicks on the images link and views them."""
    link = 'https://yandex.ru/'
    search_page = MainSearchPage(browser=browser, url=link)
    search_page.open()
    search_page.should_be_images_link()
    images_url = search_page.get_images_url()
    images_page = ImagesSearchPage(browser=browser, url=images_url)
    images_page.open()
    images_page.should_be_images_url()
    images_page.move_to_first_category_of_images()
    images_page.move_to_first_image()
    images_page.should_be_opened_image()
    url_first_image = images_page.get_source_ulr_current_image()
    images_page.move_to_next_image()
    url_second_image = images_page.get_source_ulr_current_image()
    images_page.should_be_different_image(url_first_image, url_second_image)
    images_page.move_to_previous_image()
    current_image = images_page.get_source_ulr_current_image()
    images_page.should_be_same_image(url_first_image, current_image)
