from core.extract import Extract
import unittest

class TestExtract(unittest.TestCase):

    def test_extract_markdown_images_single(self):
        text = "This is a text with an ![image](https://i.imgur.com/zjjcJKZ.png)"

        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]

        res = Extract.extract_markdown_images(text)

        self.assertEqual(expected, res)

    def test_extract_markdown_images_multiple(self):
        text = "This is a text with multiple images: ![image](https://i.imgur.com/zjjcJKZ.png) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

        expected = [("image", "https://i.imgur.com/zjjcJKZ.png"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

        res = Extract.extract_markdown_images(text)

        self.assertEqual(expected, res)

    def test_extract_markdown_images_none(self):
        text = "This is a text with no images"

        expected = []

        res = Extract.extract_markdown_images(text)

        self.assertEqual(expected, res)

    def test_extract_markdown_links_single(self):
        text = "This is a text with a link [to boot.dev](https://www.boot.dev)"

        expected = [("to boot.dev", "https://www.boot.dev")]

        res = Extract.extract_markdown_links(text)

        self.assertEqual(expected, res)

    def test_extract_markdown_links_multiple(self):
        text = "This is a text with a link [to boot.dev](https://www.boot.dev) and [to youtube.com](https://www.youtube.com)"

        expected = [("to boot.dev", "https://www.boot.dev"), ("to youtube.com", "https://www.youtube.com")]

        res = Extract.extract_markdown_links(text)

        self.assertEqual(expected, res)

    def test_extract_markdown_links_none(self):
        text = "This is a text with no links"

        expected = []

        res = Extract.extract_markdown_links(text)

        self.assertEqual(expected, res)


if __name__ == "__main__":
    unittest.main()

