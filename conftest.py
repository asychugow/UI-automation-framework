import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from api.client import ApiClient

@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def api_client():
    base_url = "https://practice.expandtesting.com/notes/api"
    client = ApiClient(base_url)
    yield client