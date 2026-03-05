# pytest test_wordpress.py -v
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.wordpress
def test_pythonwordpress(driver):

    driver.get("https://wordpress.org/")

    # Verify page title
    assert "WordPress.org" in driver.title
    print("Title Verified")

    wait = WebDriverWait(driver, 15)

    # Hover Extend menu
    extend_menu = wait.until(
        EC.presence_of_element_located((By.XPATH, "//li[contains(@class,'has-child')]"))
    )
    ActionChains(driver).move_to_element(extend_menu).perform()

    # Click Themes
    themes = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Themes')]"))
    )
    themes.click()

    # Search theme
    search_box = wait.until(
        EC.element_to_be_clickable((By.ID, "wp-block-search__input-8"))
    )
    search_box.send_keys("Astra")

    # Click search icon 
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".is-style-secondary-search-control .search-icon"))
    ).click()

    # Click first theme result 
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".wp-block-post:nth-child(1) img"))
    ).click()

    # Verify theme title
    theme_title = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".has-heading-3-font-size"))
    ).text

    assert "Astra" in theme_title
    print("Theme Title Verified:", theme_title)