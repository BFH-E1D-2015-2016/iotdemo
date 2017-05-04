import pytest

def populate_db():
    from dashboard import tests
    tests.populate_db_with_devices(["Devices 1", "Devices 2"])

@pytest.mark.django_db
def test_new_visitor(selenium, live_server):
    populate_db()

    # John is a relative new employee at Teleski SA. Today, he has heard about IOTDemo, the monitoring solution used to
    # gather all sort of information, measurement and status at Teleski SA.

    # He open the browser and check its homepage
    selenium.get(live_server + "/")

    # He notices the page title and header mention "IOT Monitoring System"
    assert "IOT Monitoring System" in selenium.title
    assert "IOT Monitoring System" in selenium.find_element_by_tag_name("h1").text

    # He found a map

    # He found a list of devices
    table = selenium.find_element_by_id("devices_list")
    rows = table.find_elements_by_tag_name('tr')

    assert any(row.text == "1: Devices 1" for row in rows)


