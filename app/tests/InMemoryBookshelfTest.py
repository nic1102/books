from unittest import TestCase
from app.models.InMemoryBookshelf import InMemoryBookshelf


class InMemoryBookshelfTest(TestCase):

    def setUp(self):
        self.im_bookshelf = InMemoryBookshelf()

    def test_get_all(self):
        ...

    def test_del_by_id(self):
        ...

    def test_get_by_id(self):
        ...

    def test_get_by_year(self):
        ...

    def test_get_by_title(self):
        ...

    def test_get_by_author(self):
        ...

    def test_change_status(self):
        ...
