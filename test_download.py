import os
import requests
from selene import query, browser
from script_os import TMP_DIR


def test_download_file_through_requests(browser_setup):
    # Открываем браузер и переходим на GitHub"
    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")

    # Получаем ссылку для скачивания
    href = browser.element('[data-testid="raw-button"]').get(query.attribute("href"))

    # Скачиваем файл через requests"
    content = requests.get(href).content

    file_path = os.path.join(TMP_DIR, "readme.rst")

    # Сохраняем файл по пути:
    with open(file_path, "wb") as file:
        file.write(content)

    # Проверяем содержимое файла
    with open(file_path) as file:
        file.content = file.read()
        assert "pytest" in file.content