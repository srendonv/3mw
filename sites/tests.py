from django.test import TestCase

from django.core.urlresolvers import reverse

class SiteViewTests(TestCase):
    def test_index_view_with_no_sites(self):
        """
        If no sites exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('sites:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No sites are available.")
