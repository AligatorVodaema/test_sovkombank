from .base_page import BasePage
from pages.locators import ImagesSearchPageLocators

EXPECTED_IMAGES_URL = 'https://yandex.ru/images/'


class ImagesSearchPage(BasePage):
    """Class for work with Images page"""
    def should_be_images_url(self):
        """Check the current url for compliance."""
        assert EXPECTED_IMAGES_URL in self.browser.current_url, \
            f'Expected url "{EXPECTED_IMAGES_URL}", ' \
            f'got "{self.browser.current_url}".'

    def move_to_first_category_of_images(self):
        """Go to first category images."""
        self.browser.find_element(
            *ImagesSearchPageLocators.FIRST_CATEGORY_OF_IMAGES
        ).click()

    def move_to_first_image(self):
        """Go to first image for view detail."""
        self.browser.find_element(
            *ImagesSearchPageLocators.FIRST_IMAGE_OF_CATEGORY
        ).click()

    def should_be_opened_image(self):
        """Check about presence media viewer."""
        assert self.is_element_present(
            *ImagesSearchPageLocators.MEDIA_VIEWER_FOR_IMAGE
        ), 'Media viewer for single image is not presented.'

    def get_source_ulr_current_image(self):
        """Get src attribute of current opened image."""
        url = self.browser.find_element(
            *ImagesSearchPageLocators.CURRENT_IMAGE_URL
        ).get_attribute('src')
        return url

    def move_to_next_image(self):
        """Click to go on next image button."""
        self.browser.find_element(
            *ImagesSearchPageLocators.NEXT_IMAGE_BUTTON
        ).click()

    @staticmethod
    def should_be_different_image(first_url, second_url):
        """Check two urls of images for mismatch."""
        assert first_url != second_url, 'The image has not change.' \
                                        f' \n{first_url}\n{second_url}'

    def move_to_previous_image(self):
        """Click to go on previous image button."""
        self.browser.find_element(
            *ImagesSearchPageLocators.PREVIOUS_IMAGE_BUTTON
        ).click()

    @staticmethod
    def should_be_same_image(first_url, second_url):
        """Check two urls of images for match."""
        assert first_url == second_url, 'The picture is not what it was.' \
                                        f'\n{first_url}\n{second_url}'
