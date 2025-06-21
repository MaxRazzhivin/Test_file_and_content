import os
import shutil
import pytest

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from script_os import TMP_DIR


@pytest.fixture(scope="session", autouse=True)
def setup_tmp_dir():
    """Создаём tmp/ перед тестами и удаляем после"""
    os.makedirs(TMP_DIR, exist_ok=True)
    yield
    shutil.rmtree(TMP_DIR)


@pytest.fixture(scope="session")
def browser_setup():
    """Настройка браузера с нужной директорией скачивания"""
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": TMP_DIR,
        "download.prompt_for_download": False
    }
    options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options)
    browser.config.driver = driver
    yield
    browser.quit()