import django.test


class StaticURLTests(django.test.TestCase):
    def test_homepage_endpoint(self):
        response = django.test.Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_detail_endpoint(self):
        response = django.test.Client().get("/catalog/1/")
        self.assertEqual(response.status_code, 200)
