import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s


@allure.tag('GitHub repository')
@allure.severity(Severity.MINOR)
@allure.label('Owner', 'Bykat')
@allure.feature('GitHub issue search using allure_steps')
def test_github_allure_steps():
    with allure.step("Открытие главной страницы GitHub"):
        browser.open("https://www.github.com")
    with allure.step("Поиск нужного репозитория"):
        s(".search-input").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example").press_enter()
    with allure.step("Переход на страницу репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step("Переход в раздел Issues"):
        s("#issues-tab").click()
    with allure.step("Проверка наличия нужной Issue на странице"):
        s(by.text("Issue for HW qa.guru")).should(be.visible)
