def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"


def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"


if __name__ == "__main__":
    test_abs1()
    test_abs2()


# В терминале PyCharm-a (Alt+F12) запустить следующее:
# pytest {file_path}
# For example:
# pytest "C:\Users\dzmitry.lapitski\PycharmProjects\Selenium\Chapter #3 (Тестовые фреймворки)\Lesson #3 (Тестрирование с помощью PyTest)\Step #2 (PyTest - преимущества и недостатки).py"