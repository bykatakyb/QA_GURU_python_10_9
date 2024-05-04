import allure
from allure_commons.types import Severity

from utils.decorator_func import open_main_page, search_for_repository, move_to_repository, move_to_issues_tab, \
    repo_test, there_has_to_be_issue_named, issue_name_test


@allure.tag('GitHub repository')
@allure.severity(Severity.MINOR)
@allure.label('Owner', 'Bykat')
@allure.feature('GitHub issue search using allure_steps')
def test_github_allure_decorators():
    open_main_page()
    search_for_repository(repo_test)
    move_to_repository(repo_test)
    move_to_issues_tab()
    there_has_to_be_issue_named(issue_name_test)