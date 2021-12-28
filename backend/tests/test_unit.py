from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Regions

test_region = {
    "region_id": 1,
    "region_name": "London",
    "region_property_address": "Flat 12 B",
    "region_price": "200.000",
    "description": 'Best price',
}


class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Regions(region_name="London",region_property_address="region_property_address",region_price="region_price",description="description"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestRead(TestBase):

    def test_read_all_regions(self):
        response = self.client.get(url_for('read_all_regions'))
        self.assertEqual(test_region["region_name"], "London")

    def test_get_region(self):
        response = self.client.get(url_for('get_region', id=1))
        self.assertEqual(test_region["region_name"], "London")


class TestCreate(TestBase):

    def test_create_region(self):
        response = self.client.post(
            url_for('create_region'),
            json={"region_name": "York","region_property_address": "region_property_address","region_price": "region_price","description": "description"},
            follow_redirects=True
        )
        self.assertEqual(Regions.query.get(2).region_name, "York")


class TestUpdate(TestBase):

    def test_update_region(self):
        response = self.client.put(
            url_for('update_region', id=1),
            json={"region_name": "Reading","region_property_address": "region_property_address","region_price": "region_price","description": "description"},
        )
        self.assertEqual(
            b"Updated task (ID: 1)", response.data)
        self.assertEqual(Regions.query.get(
            1).region_name, "Reading")


class TestDelete(TestBase):

    def test_delete_region(self):
        response = self.client.delete(url_for('delete_region', id=1))
        self.assertIsNone(Regions.query.get(1))
