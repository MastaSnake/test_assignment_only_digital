import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_http_status_200():
    response = requests.get("https://only.digital/", timeout=10)
    assert response.status_code == 200


@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.set_page_load_timeout(30)
    driver.get("https://only.digital/")
    yield driver
    driver.quit()

def test_footer_is_present(driver):
    footer = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "footer"))
    )
    assert footer.is_displayed(), "Футер не отображается"


def test_contact_info_in_footer(driver):
    footer_text = driver.find_element(By.TAG_NAME, "footer").text
    assert "+7" in footer_text, "В футере отсутствует номер телефона в формате +7"


def test_social_links_in_footer(driver):
    footer = driver.find_element(By.CSS_SELECTOR, "footer")
    links = footer.find_elements(By.CSS_SELECTOR, "a[href*='t.me'], a[href*='vk.com'], a[href*='instagram'], a[href*='behance']")
    assert len(links) >= 2, f"Найдено только {len(links)} ссылок на соцсети"
