from django.test import LiveServerTestCase
from selenium import webdriver

def populate_db():
    from lorawan.tests import populate_db_with_devices

    populate_db_with_devices(["Devices 1", "Devices 2"])



class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        import os

        is_travis = 'TRAVIS' in os.environ

        if(is_travis):
           self.browser = webdriver.PhantomJS()
        else:
            self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def test_new_visitor(self):
        populate_db()

        # John is a relative new employee at Teleski SA. Today, he has heard about IOTDemo, the monitoring solution used to
        # gather all sort of information, measurement and status at Teleski SA.

        # He open the browser and check its homepage
        self.browser.get(self.live_server_url + "/")

        # He notices the page title and header mention "IOT Monitoring System"
        self.assertIn("IOT Monitoring System", self.browser.title)
        self.assertIn("IOT Monitoring System", self.browser.find_element_by_tag_name("h1").text)

        # He found a map

        # He found a list of devices with a status
        table = self.browser.find_element_by_id("devices_list")
        first_row = table.find_element_by_tag_name('tbody tr')
        self.assertIn("Devices 1", first_row.text)
        self.assertIn("OK", first_row.text)



