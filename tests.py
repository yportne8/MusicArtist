import unittest
from mscookies.cookies import (Browsers, Browser,
                               Profile, Cookies, CookieJar)


class TestWindowsPaths(unittest.TestCase):
    
    def test_browsers_paths(self):
        browsers = Browsers.browser_paths()
        for browser in browsers.keys():
            self.assertTrue(browser in Browsers.CHROMIUM_BASED)

    def test_browser_paths(self):
        browser = Browser("Edge")
        self.assertTrue(browser.browser_path.exists())
        self.assertTrue(browser.user_data.exists())
        self.assertTrue(browser.local_state.exists())

    def test_profile_paths(self):
        profile = Profile("edge", "Default")
        self.assertTrue(profile.profile_path.exists())
        self.assertTrue(profile.local_state.exists())
        self.assertTrue(profile.cookies.exists())
        self.assertTrue(profile.picture.exists())
    

class TestCookies(unittest.TestCase):

    def test_cookiejar(self):
        cookies = Cookies("Edge", "default")
        cookiejar = cookies.cookiejar()
        self.assertTrue(type(cookiejar)==CookieJar)

    def test_cookie(self):
        cookies = Cookies("edge", "default")
        cookie = cookies.cookie("google.com")
        self.assertTrue(type(cookie)==CookieJar)

    def test_cookiestring(self):
        cookies = Cookies("edge", "Default")
        cookiestring = cookies.cookiestring("google.com")
        self.assertTrue(type(cookiestring)==str)

    def test_save_cookiejar(self):
        cookies = Cookies("Edge", "Default")
        cookiejar = cookies.cookiejar()
        cookiejar_text = cookiejar.save()
        self.assertTrue(cookiejar_text.exists())

    def test_save_cookie(self):
        cookies = Cookies("Edge", "Default")
        cookie = cookies.cookie("google.com")
        cookie_text = cookie.save()
        self.assertTrue(cookie_text.exists())
        


if __name__ == '__main__':
    unittest.main()