import pytest
from selenium import webdriver
from Config.config import TestData
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def init_driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(5)
    yield driver
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://worksheetzone.org/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "Automation Test Report!"

