import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s

repo_test = "eroshenkoam/allure-example"
issue_name_test = "Issue for HW qa.guru"


@allure.step("Открытие главной страницы GitHub")
def open_main_page():
    browser.open("")


@allure.step("Поиск нужного репозитория {repo}")
def search_for_repository(repo):
    s(".search-input").click()
    s("#query-builder-test").send_keys(repo).press_enter()


@allure.step("Переход на страницу репозитория {repo}")
def move_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Переход в раздел Issues")
def move_to_issues_tab():
    s("#issues-tab").click()


@allure.step("Проверка наличия нужной Issue ({name}) на странице")
def there_has_to_be_issue_named(name):
    s(by.text(name)).should(be.visible)
