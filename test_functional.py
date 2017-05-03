def test_new_visitor(selenium, live_server):

    # John is a relative new employee at Teleski SA. Today, he has heard about IOTDemo, the monitoring solution used to
    # gather all sort of information, measurement and status at Teleski SA.

    # He open the browser and check its homepage
    selenium.get(live_server + "/")

    # He notices the page title and header mention "IOT Monitoring System"
    assert "IOT Monitoring System" in selenium.title

    # He found a map

    # He found a list of devices

