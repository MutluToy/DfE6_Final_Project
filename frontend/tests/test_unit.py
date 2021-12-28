from flask import url_for
from flask_testing import TestCase
from application import app
from application.routes import backend
import requests_mock

test_region = {
    "region_id": 1,
    "region_name": "Bristol",
    "region_property_address": "Flat 12 A",
    "region_price": "200.000",
    "description": 'Best price',
}


class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app


class TestViews(TestBase):
    def test_home_get(self):
        with requests_mock.Mocker() as m:
            all_regions = [test_region]
            m.get(f"http://{backend}/regions", json=all_regions)
            response = self.client.get(url_for('home'))
            self.assert200(response)

    def test_create_region_get(self):
        response = self.client.get(url_for('create_region'))
        self.assert200(response)

    def test_update_region_get(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend}/region/1", json=test_region)
            response = self.client.get(url_for('update_region', id=1))
            self.assert200(response)


class TestRead(TestBase):
    def test_get_regions(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend}/regions", json=[test_region])
            response = self.client.get(url_for('home'))
            self.assertIn(b"Bristol", response.data)


class TestUpdate(TestBase):

    def test_update_region_name(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend}/region/1", json=test_region)
            m.put(f"http://{backend}/update/1", text="Test response")
            test_region["region_name"] = "London"
            m.get(f"http://{backend}/regions",
                  json=[test_region])
            response = self.client.post(
                url_for('update_region', id=1),
                data={"region_name": "London"},
                follow_redirects=True
            )
            self.assertIn(b"London", response.data)

class TestDelete(TestBase):

    def test_delete_region(self):
        with requests_mock.Mocker() as m:
            m.delete(f"http://{backend}/delete/1")
            m.get(f"http://{backend}/regions", json=[])
            response = self.client.get(
                url_for('delete_region', id=1),
                follow_redirects=True
            )
            self.assertNotIn(b"Test the region delete", response.data)
