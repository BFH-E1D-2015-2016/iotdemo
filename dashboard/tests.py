from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from dashboard.views import dashboard

def test_root_url_resolves_to_dashboard_view():
    found = resolve("/")
    assert found.func == dashboard

def test_root_url_use_dashboard_template(client):
    response = client.get("/")
    html = response.content.decode("utf8")

    expected_html = render_to_string('dashboard.html')
    assert html == expected_html



