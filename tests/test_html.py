import unittest
from html.parser import HTMLParser

class IDCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        for attr, value in attrs:
            if attr == 'id':
                self.ids.add(value)

class TestNight4Elements(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('night4.html', 'r', encoding='utf-8') as f:
            parser = IDCollector()
            parser.feed(f.read())
        cls.ids = parser.ids

    def test_start_music_exists(self):
        self.assertIn('start-music', self.ids)

    def test_pause_music_exists(self):
        self.assertIn('pause-music', self.ids)

    def test_toggle_button_exists(self):
        self.assertIn('toggle-btn', self.ids)

    def test_bucket_exists(self):
        self.assertIn('bucket', self.ids)

if __name__ == '__main__':
    unittest.main()
