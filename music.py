from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


class music:

    def __init__(self):
        self.PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get("https://www.onlinepianist.com/virtual-piano")
        time.sleep(10)
        self.zoomOut = self.driver.find_element_by_id("zoomButton")
        self.letters = self.driver.find_element_by_id("letterLabelsButton")
        self.keyboard = self.driver.find_element_by_id("keyboard")
        self.fullScreen = self.driver.find_element_by_id("fullScreenButton")
        self.action = ActionChains(self.driver)

    def start(self):
        self.PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)

    def buttons(self):
        """
        :return: effects on display
        """
        '''Elements'''
        time.sleep(10)
        self.fullScreen.click()
        time.sleep(2)
        self.zoomOut.click()
        time.sleep(1)
        self.letters.click()
        time.sleep(1)

    def run(self):
        self.action.perform()

    def quit(self):
        self.driver.quit()

    def breaktime(self, s):
        """
        :param s: seconds
        :return: a bDak based in the seconds
        """
        self.action.pause(s)

    def C(self, n=1, hold="n"):
        """
        :param n: note's number
        :param hold: hold  (n = no , y = yes)
        :return: play the C note
        """
        if hold == "y":
            self.action.move_to_element_with_offset(self.keyboard, 25.5 * (3 + 7 * (n - 1)), 120).click_and_hold()
        else:
            self.action.move_to_element_with_offset(self.keyboard, 25.5 * (3 + 7 * (n - 1)), 120).click()

    def sC(self, n=1, hold="n"):
        """
        :param n: note's number
        :param hold: hold (n = no, y = yes)
        :return: C# note
        """
        if hold == "y":
            self.action.move_to_element_with_offset(self.keyboard, 26 * (3 + 7 * (n - 1)), 0).click_and_hold()
        else:
            self.action.move_to_element_with_offset(self.keyboard, 26 * (3 + 7 * (n - 1)), 0).click()

    def D(self, n=1, hold="n"):
        """
        :param n: note's number
        :param hold: hold  (n = no , y = yes)
        :return: play the D note
        """
        if hold == "y":
            self.action.move_to_element_with_offset(self.keyboard, 25.5 * (4 + 7 * (n - 1)), 120).click_and_hold()
        else:
            self.action.move_to_element_with_offset(self.keyboard, 25.5 * (4 + 7 * (n - 1)), 120).click()

    def sD(self, n=1, hold="n"):
        """
        :param n: note's number
        :param hold: hold (n = no, y = yes)
        :return: D# note
        """
        if hold == "y":
            self.action.move_to_element_with_offset(self.keyboard, 26 * (4 + 7 * (n - 1)), 0).click_and_hold()
        else:
            self.action.move_to_element_with_offset(self.keyboard, 26 * (4 + 7 * (n - 1)), 0).click()

    def E(self, n=1, hold="n"):
        """
        :param n: note's number
        :param hold: hold  (n = no , y = yes)
        :return: play the E note
        """
        if hold == "y":
            self.action.move_to_element_with_offset(self.keyboard, 25.5 * (5 + 7 * (n - 1)), 120).click_and_hold()
        else:
            self.action.move_to_element_with_offset(self.keyboard, 25.5 * (5 + 7 * (n - 1)), 120).click()

    def F(self, n=1, hold="n"):
        """
        :param n: note's number
        :param hold: hold  (n = no , y = yes)
        :return: play the F note
        """
        if hold == "y":
            self.action.move_to_element_with_offset(self.keyboard, 25.5 * (6 + 7 * (n - 1)), 120).click_and_hold()
        else:
            self.action.move_to_element_with_offset(self.keyboard, 25.5 * (6 + 7 * (n - 1)), 120).click()

    def sF(self, n=1, hold="n"):
        """
        :param n: note's number
        :param hold: hold (n = no, y = yes)
        :return: play the F# note
        """
        if hold == "y":
            self.action.move_to_element_with_offset(self.keyboard, 26 * (6 + 7 * (n - 1)), 0).click_and_hold()
        else:
            self.action.move_to_element_with_offset(self.keyboard, 26 * (6 + 7 * (n - 1)), 0).click()

    def G(self, n=1, hold="n"):
        """
        :param n: note's number
        :param hold: hold  (n = no , y = yes)
        :return: play the G note
        """
        if hold == "y":
            self.action.move_to_element_with_offset(self.keyboard, 25.5 * (7 + 7 * (n - 1)), 120).click_and_hold()
        else:
            self.action.move_to_element_with_offset(self.keyboard, 25.5 * (7 + 7 * (n - 1)), 120).click()

    def sG(self, n=1, hold="n"):
        """
        :param n: note's number
        :param hold: hold (n = no, y = yes)
        :return: play the G# note
        """
        if hold == "y":
            self.action.move_to_element_with_offset(self.keyboard, 26 * (7 + 7 * (n - 1)), 0).click_and_hold()
        else:
            self.action.move_to_element_with_offset(self.keyboard, 26 * (7 + 7 * (n - 1)), 0).click()

    def A(self, n=1, hold="n"):
        """
        :param n: note's number
        :param hold: hold  (n = no , y = yes)
        :return: play the A note
        """
        if hold == "y":
            if n == 0:
                self.action.move_to_element_with_offset(self.keyboard, 25.5, 120).click_and_hold()
            else:
                self.action.move_to_element_with_offset(self.keyboard, 25.5 * (1 + 7 * n), 120).click_and_hold()
        else:
            if n == 0:
                self.action.move_to_element_with_offset(self.keyboard, 25.5, 120).click()
            else:
                self.action.move_to_element_with_offset(self.keyboard, 25.5 * (1 + 7 * n), 120).click()

    def sA(self, n=1, hold="n"):
        """
        :param n: note's number
        :param hold: hold (n = no, y = yes)
        :return: A# note
        """
        if hold == "y":
            if n == 0:
                self.action.move_to_element_with_offset(self.keyboard, 26, 0).click_and_hold()
            else:
                self.action.move_to_element_with_offset(self.keyboard, 26 * (1 + 7 * n), 0).click_and_hold()
        else:
            if n == 0:
                self.action.move_to_element_with_offset(self.keyboard, 26, 0).click()
            else:
                self.action.move_to_element_with_offset(self.keyboard, 26 * (1 + 7 * n), 0).click()

    def B(self, n=1, hold="n"):
        """
        :param n: note's number
        :param hold: hold  (n = no , y = yes)
        :return: play the B note
        """
        if hold == "y":
            if n == 0:
                self.action.move_to_element_with_offset(self.keyboard, 25.5 * 2, 120).click_and_hold()
            else:
                self.action.move_to_element_with_offset(self.keyboard, 25.5 * (2 + 7 * n), 120).click_and_hold()
        else:
            if n == 0:
                self.action.move_to_element_with_offset(self.keyboard, 25.5 * 2, 120).click()
            else:
                self.action.move_to_element_with_offset(self.keyboard, 25.5 * (2 + 7 * n), 120).click()

    def part1(self):
        self.breaktime(0.0001)
        self.E(5)
        self.breaktime(0.01)
        self.E(5)
        self.breaktime(0.025)
        self.E(5)
        self.breaktime(0.025)
        self.C(5)
        self.E(5)
        self.breaktime(0.15)
        self.G(5)
        self.breaktime(0.4)
        self.G(4)
        self.breaktime(0.5)

    def part2(self):
        self.C(5)
        self.breaktime(0.2)
        self.G(4)
        self.breaktime(0.2)
        self.E(4)
        self.breaktime(0.1)
        self.breaktime(0.1)
        self.A(4)
        self.breaktime(0.05)
        self.B(4)
        self.breaktime(0.05)
        self.sA(4)
        self.A(4)
        self.breaktime(0.05)
        self.G(4)
        self.E(5)
        self.G(5)
        self.A(5)
        self.breaktime(0.05)
        self.F(5)
        self.G(5)
        self.breaktime(0.05)
        self.E(5)
        self.breaktime(0.05)
        self.C(5)
        self.D(5)
        self.B(4)
        self.breaktime(0.2)

    def part3(self):
        self.C(3)
        self.breaktime(0.2)
        self.breaktime(0.15)
        self.G(5)
        self.sF(5)
        self.F(5)
        self.sD(5)
        self.breaktime(0.05)
        self.E(5)
        self.breaktime(0.1)
        self.sG(4)
        self.A(4)
        self.C(5)
        self.breaktime(0.05)
        self.A(4)
        self.C(5)
        self.D(5)
        self.breaktime(0.1)
        self.C(3)
        self.breaktime(0.1)
        self.G(5)
        self.sF(5)
        self.F(5)
        self.sD(5)
        self.breaktime(0.05)
        self.breaktime(0.05)
        self.E(5)
        self.breaktime(0.05)
        self.C(6)
        self.breaktime(0.05)
        self.C(6)
        self.C(6)
        self.breaktime(0.6)
        self.C(3)
        self.breaktime(0.1)
        self.G(5)
        self.sF(5)
        self.F(5)
        self.sD(5)
        self.breaktime(0.05)
        self.E(5)
        self.breaktime(0.1)
        self.sG(4)
        self.A(4)
        self.C(5)
        self.breaktime(0.05)
        self.A(4)
        self.C(5)
        self.D(5)
        self.breaktime(0.2)
        self.sD(5)
        self.breaktime(0.2)
        self.D(5)
        self.breaktime(0.2)
        self.C(5)
        self.breaktime(1)

    def part4(self):
        self.C(5)
        self.C(5)
        self.breaktime(0.05)
        self.C(5)
        self.breaktime(0.05)
        self.C(5)
        self.D(5)
        self.breaktime(0.05)
        self.E(5)
        self.C(5)
        self.breaktime(0.05)
        self.A(4)
        self.G(4)
        self.breaktime(0.5)
        self.C(5)
        self.C(5)
        self.breaktime(0.05)
        self.C(5)
        self.breaktime(0.05)
        self.C(5)
        self.D(5)
        self.breaktime(0.05)
        self.E(5)
        self.breaktime(1)
        self.C(5)
        self.C(5)
        self.breaktime(0.05)
        self.C(5)
        self.breaktime(0.05)
        self.C(5)
        self.D(5)
        self.breaktime(0.05)
        self.E(5)
        self.C(5)
        self.breaktime(0.05)
        self.A(4)
        self.G(4)
        self.breaktime(0.2)

    def part5(self):
        self.E(5)
        self.C(5)
        self.breaktime(0.025)
        self.G(4)
        self.breaktime(0.1)
        self.sG(4)
        self.breaktime(0.025)
        self.A(4)
        self.F(5)
        self.breaktime(0.025)
        self.F(5)
        self.A(4)
        self.breaktime(0.3)
        self.B(4)
        self.A(5)
        self.A(5)
        self.A(5)
        self.G(5)
        self.F(5)
        self.E(5)
        self.C(5)
        self.breaktime(0.025)
        self.A(4)
        self.G(4)
        self.breaktime(0.3)
        self.E(5)
        self.C(5)
        self.breaktime(0.025)
        self.G(4)
        self.breaktime(0.1)
        self.sG(4)
        self.breaktime(0.025)
        self.A(4)
        self.F(5)
        self.breaktime(0.025)
        self.F(5)
        self.A(4)
        self.breaktime(0.15)
        self.B(4)
        self.F(5)
        self.breaktime(0.025)
        self.F(5)
        self.F(5)
        self.E(5)
        self.D(5)
        self.C(5)
        self.E(4)
        self.breaktime(0.025)
        self.E(4)
        self.C(4)
        self.breaktime(0.3)

    def mariosSong(self):
        self.part1()
        self.part2()
        self.part2()
        self.part3()
        self.part3()
        self.part4()
        self.part1()
        self.part2()
        self.part2()
        self.part5()
        self.part4()
        self.part1()
        self.part5()
    pass
