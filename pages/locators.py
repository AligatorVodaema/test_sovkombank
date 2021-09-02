from selenium.webdriver.common.by import By


SEARCH_WORD = 'Совкомбанк'
EXPECTED_SITE = 'sovcombank.ru'


class MainSearchPageLocators:
    SEARCH_FIELD = (
        By.XPATH, '//input[@class="input__control input__input mini-suggest__input"]'
    )
    SUGGESTIONS_LIST = (By.XPATH, '//ul[@role="listbox"]/li')
    RESULT_TABLE_OF_SEARCH = (
        By.XPATH, '//ul[@class="serp-list serp-list_left_yes"]/li'
    )
    FIRST_TEN_RESULT_AFTER_SEARCH = (
        By.XPATH, '//li[@class="serp-item"]//a/b'
    )
    IMAGES_ICON_LINK = (By.XPATH, '//a[@data-id="images"]')


class ImagesSearchPageLocators:
    FIRST_CATEGORY_OF_IMAGES = (By.XPATH, "//div[@class='PopularRequestList']/div")
    FIRST_IMAGE_OF_CATEGORY = (By.XPATH, '//a[@class="serp-item__link"]')
    MEDIA_VIEWER_FOR_IMAGE = (
        By.XPATH, '//div[@class="MediaViewer MediaViewer_theme_fiji ImagesViewer-Container"]'
    )
    NEXT_IMAGE_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_next ')
    PREVIOUS_IMAGE_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_prev')
    CURRENT_IMAGE_URL = (By.CSS_SELECTOR, '.MMImage-Origin')

