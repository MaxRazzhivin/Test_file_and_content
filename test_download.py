import os
import requests
from selene import query, browser

from script_os import TMP_DIR


def test_download_file_through_requests(browser_setup):
    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")

    href = browser.element('[data-testid="raw-button"]').get(query.attribute("href"))
    content = requests.get(href).content

    file_path = os.path.join(TMP_DIR, "readme_downloaded.rst")
    with open(file_path, "wb") as file:
        file.write(content)

    with open(file_path, "r") as file:
        text = file.read()
        assert "pytest" in text