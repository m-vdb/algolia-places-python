import unittest

from algolia_places.struct import BaseObject


class MyObject(BaseObject):

    DIRECT_LOOKUPS = ['attr1', 'attr2']


class BaseObjectTestCase(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.obj = MyObject({'attr1': 'yeah', 'attr2': 'boom'})

    def test_init(self):
        self.assertEqual(
            self.obj.data,
            {'attr1': 'yeah', 'attr2': 'boom'}
        )

    def test_getattribute(self):
        self.assertEqual(self.obj.attr1, 'yeah')
        self.assertEqual(self.obj.attr2, 'boom')
        with self.assertRaises(AttributeError):
            self.obj.attr3

    def test_dir(self):
        self.assertEqual(
            dir(self.obj),
            # sorted
            [
                'DIRECT_LOOKUPS',
                '__class__',
                '__delattr__',
                '__dict__',
                '__dir__',
                '__doc__',
                '__eq__',
                '__format__',
                '__ge__',
                '__getattribute__',
                '__gt__',
                '__hash__',
                '__init__',
                '__init_subclass__',
                '__le__',
                '__lt__',
                '__module__',
                '__ne__',
                '__new__',
                '__reduce__',
                '__reduce_ex__',
                '__repr__',
                '__setattr__',
                '__sizeof__',
                '__str__',
                '__subclasshook__',
                '__weakref__',
                'attr1',
                'attr2',
                'data',
            ]
        )
