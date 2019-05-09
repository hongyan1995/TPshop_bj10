from selenium.webdriver.support.wait import WebDriverWait

import allure


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1):
        """
        根据元素特征（元组）寻找对应的一个元素
        :param feature: 特征
        :param timeout: 超时时间，默认10秒
        :param poll: 频率，默认1秒
        :return: 找到的元素
        """
        by, value = feature
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=10, poll=1):
        """
        根据元素特征（元组）寻找对应的一组元素
        :param feature: 特征
        :param timeout: 超时时间，默认10秒
        :param poll: 频率，默认1秒
        :return: 找到的元素
        """
        by, value = feature
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def click(self, feature):
        """
        根据特征，寻找元素，并点击
        :param feature: 特征
        """
        self.find_element(feature).click()

    def input(self, feature, content):
        """
        根据特征，寻找元素，并输入对应的文字
        :param feature: 特征
        :param content: 文字
        """
        self.clear(feature)
        self.find_element(feature).send_keys(content)

    def clear(self, feature):
        """
        根据特征，寻找元素，并清空文字
        :param feature: 特征
        """
        self.find_element(feature).clear()

    def press_back(self):
        """
        按返回键
        """
        self.driver.press_keycode(4)

    def press_enter(self):
        """
        按回车键
        """
        self.driver.press_keycode(66)

    def screen_shot(self, file_name):
        """
        屏幕截图，保存在image文件夹中
        :param file_name: 文件名
        :return: 是否截图成功
        """
        return self.driver.get_screenshot_as_file("./image/" + file_name)

    @staticmethod
    def allure_pic_with_local(title, file_name):
        """
        将本地的image中的某张图片，添加到allure报告中
        :param title: allure标题
        :param file_name: image文件夹中的哪一个图片
        """
        with open("./image/" + file_name, "rb") as f:
            allure.attach(title, f.read(), allure.attach_type.PNG)