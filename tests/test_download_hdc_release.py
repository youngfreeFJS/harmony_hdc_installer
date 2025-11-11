'''Test file for downloading files.'''
import os
import unittest

from hdc_installer._download_hdc import download_file

# Target file URL and local save path
TEST_PKG_URL = "https://github.com/youngfreeFJS/harmony_hdc_installer/archive/refs/tags/0.1.0.zip"
FILE_TARGET_NAME = "0.1.0.zip"


class TestFileDownload(unittest.TestCase):
    """Unit test class for testing file download functionality."""

    def setUp(self):
        """Setup operations before each test case."""
        # Ensure the file does not exist before the test starts
        if os.path.exists(FILE_TARGET_NAME):
            os.remove(FILE_TARGET_NAME)

    def test_download_file(self):
        """Test case to verify file download functionality."""
        # Call the download function
        result = download_file(TEST_PKG_URL, FILE_TARGET_NAME)

        # Assert that the download function returned True
        self.assertTrue(result, "Download failed, function did not return True")
        # Assert that the file exists locally after download
        self.assertTrue(os.path.exists(FILE_TARGET_NAME),
                        f"Target file {FILE_TARGET_NAME} is missing")
        # Assert that the downloaded file size is greater than 0
        self.assertGreater(os.path.getsize(FILE_TARGET_NAME), 0,
                           f"Target file {FILE_TARGET_NAME} is empty")

    def tearDown(self):
        """Cleanup operations after each test case."""
        # Delete the downloaded file after the test
        if os.path.exists(FILE_TARGET_NAME):
            os.remove(FILE_TARGET_NAME)

if __name__ == "__main__":
    unittest.main()
