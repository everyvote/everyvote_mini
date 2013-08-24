# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import django

from everyvote_mini.models import Constituency, Office


class MockConstituencies():
    _data = [
        {'name': 'Northern Igloo University',
         'about': "Brrrr"},
        {'name': 'Underwater Naked Kings',
         'about': 'We like fish.'},
        {'name': u'Pokémon Academy',
         'about': 'Gotta catch\'em all!'}
    ]

    @staticmethod
    def getAll():
        return_list = []

        for c in MockConstituencies._data:
            return_list.append(
                MockConstituencies._create_from_dict(c)
            )

        return return_list

    @staticmethod
    def getOne():
        c = MockConstituencies._create_from_dict(MockConstituencies._data[0])
        return c

    @staticmethod
    def _create_from_dict(dict):
        return Constituency.objects.create(
            name=dict['name'],
            about=dict['about']
        )


class ConstituencyTests(TestCase):
    def test_constituency_creation(self):

        cts = MockConstituencies.getAll()

        # Save all constituencies in database
        for c in cts:
            c.save()

        # Assert that they got in the db
        for c in cts:
            search_result = Constituency.objects.filter(name=c.name)
            self.assertTrue(len(search_result) != 0)


class OfficeTest(TestCase):
    def test_office_creation_fails_with_no_constituency(self):
        with self.assertRaises(django.db.IntegrityError):
            Office.objects.create(name='test', about='test')

    def test_office_creation_fails_with_no_name(self):
        test_constituency = MockConstituencies.getOne()

        with self.assertRaises(django.db.IntegrityError):
            Office.objects.create(
                about='test',
                constituency=test_constituency)

    def test_office_creation_ok_with_no_about(self):
        test_constituency = MockConstituencies.getOne()

        Office.objects.create(
            name='CEO',
            constituency=test_constituency)
        """
        with self.assertRaises(django.db.IntegrityError):
            Office.objects.create(about='test')
        """