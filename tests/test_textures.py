import filecmp
import os
import unittest


class TestTextures(unittest.TestCase):
    def test_duplicate_names(self):
        images = []
        # Only works on Python 3.5+
        # images += \
        #     glob.glob(os.path.join("", "**", "*.jpg"), recursive=True) + \
        #     glob.glob(os.path.join("", "**", "*.png"), recursive=True)

        for root, dirs, files in os.walk("."):
            images.extend(
                os.path.join(root, filename)
                for filename in files
                if filename.endswith(".jpg") or filename.endswith("*.png")
            )

        self.assertGreater(len(images), 0)

        hash_map = {}
        duplicate_files = []
        for image in images:
            _, filename = os.path.split(image)
            if filename in hash_map:
                # check if it is the same file but in a different location:
                if not filecmp.cmp(image, hash_map[filename]):
                    duplicate_files.append((image, hash_map[filename]))
            else:
                hash_map[filename] = image
        self.assertListEqual(duplicate_files, [])
