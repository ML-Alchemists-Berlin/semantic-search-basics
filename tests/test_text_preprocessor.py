import unittest
from src.text_processor import process_text, remove_stopwords

class TestTextProcessor(unittest.TestCase):
    def test_remove_stopwords(self):
        self.assertEqual(remove_stopwords("this is a text test"), "text test")
        self.assertEqual(remove_stopwords("another example without stopwords"), "stopwords example")

    def test_process_text(self):
        self.assertEqual(process_text("Hello World this is a test."), "hello world test")
        self.assertEqual(process_text("another EXAMPLE, with, punctuation."), "punctuation example")

if __name__ == '__main__':
    unittest.main()
