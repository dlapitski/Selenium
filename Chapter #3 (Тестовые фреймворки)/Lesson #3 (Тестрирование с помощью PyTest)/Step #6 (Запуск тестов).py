# tests_for_pytest/test_main_page:
#
# # номер 1
# def main_page_buttons(browser):
#
# # номер 2
# def test_main_page_navbar(browser):



# smoke_tests/login.py:
#
# # номер 3
# def test_guest_can_login(browser, language):
#
# # номер 4
# class TestLogin(object):
#     def test_guest_should_see_login_link(self, browser, language):



# (корневая директория проекта) test_regression.py:
#
# class TestLessonCreate():
#     # номер 5
#     def test_create_lesson(self, browser):
#
#     # номер 6
#     def user_with_lesson_can_create_lesson_from_navbar_test(self, browser):
#
#
# class CourseCreate():
#     # номер 7
#     def test_create_course(self, browser):
#
# # номер 8
# def test_guest_can_open_new_course(browser):



# pytest test_project

# Файлы, которые выполнятся:
# Номер 5, 8

# Файлы, которые не выполнятся:
# Номер 1, 2 - файл test_main_page не имеет расширения .py
# Номер 3, 4 - файл login.py не имеет начального или конечного test в названии
# Номер 6 - отсутствует начальное test в навзании метода
# Номер 7 - отсутствует начальное test в названии класаа