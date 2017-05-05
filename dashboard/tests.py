from django.test import TestCase

from django.core.urlresolvers import resolve
from django.template.loader import render_to_string

from dashboard.views import dashboard


class DashboardTest(TestCase):


    def test_root_url_resolves_to_dashboard_view(self):
        found = resolve("/")
        self.assertEqual(found.func, dashboard)

    def test_root_url_use_dashboard_template(self):
        response = self.client.get("/")
        html = response.content.decode("utf8")

        expected_html = render_to_string('dashboard.html')

        self.assertEqual(html, expected_html)






