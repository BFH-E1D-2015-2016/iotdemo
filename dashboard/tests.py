from django.core.urlresolvers import resolve
from django.http import HttpRequest

from dashboard.views import dashboard

def test_root_url_resolves_to_dashboard_view():
    found = resolve("/")
    assert found.func == dashboard

def test_home_page_returns_html():
    request = HttpRequest()
    response = dashboard(request)

    html = response.content.decode("utf8")

    assert html.startswith("<html>")
    assert "<title>IOT Monitoring System</title>" in html
    assert html.endswith("</html>")


