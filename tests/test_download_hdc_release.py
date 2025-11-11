"""Test file for downloading and extracting files."""
import os
import unittest
import zipfile
import shutil

from hdc_installer._download_hdc import download_file

# Test-specific file URL and local save path
TEST_PKG_URL = "https://github.com/youngfreeFJS/harmony_hdc_bin_collections/raw/main/v3.0.2b/mac_arm/hdc_3.2.0b_mac_arm.zip"
FILE_TARGET_NAME = "hdc_3.2.0b_mac_arm.zip"
EXTRACTION_DIR = "./test_extracted_files"


class TestFileDownloadAndExtraction(unittest.TestCase):
    """Unit test class for testing file download and extraction functionality."""

    def setUp(self):
        """Setup operations before each test case."""
        # Ensure the file and extraction directory do not exist before the test starts
        if os.path.exists(FILE_TARGET_NAME):
            os.remove(FILE_TARGET_NAME)
        if os.path.exists(EXTRACTION_DIR):
            shutil.rmtree(EXTRACTION_DIR)

    def test_download_and_extract_file(self):
        """Test case to verify file download and extraction functionality."""
        # Step 1: Test file download
        download_result = download_file(TEST_PKG_URL, FILE_TARGET_NAME)

        # Verify the download was successful
        self.assertTrue(download_result, "File download failed.")
        self.assertTrue(os.path.exists(FILE_TARGET_NAME), f"File {FILE_TARGET_NAME} is missing.")
        self.assertGreater(os.path.getsize(FILE_TARGET_NAME), 0, f"File {FILE_TARGET_NAME} is empty.")

        print(f"\nFile {FILE_TARGET_NAME} downloaded successfully.")
        print(f"File size: {os.path.getsize(FILE_TARGET_NAME)} bytes.")
        print(f"File path: {os.path.abspath(FILE_TARGET_NAME)}")

        # Step 2: Test file extraction
        try:
            os.mkdir(EXTRACTION_DIR)
            with zipfile.ZipFile(FILE_TARGET_NAME, 'r') as zip_ref:
                zip_ref.extractall(EXTRACTION_DIR)

            # Verify extraction was successful
            extracted_files = os.listdir(EXTRACTION_DIR)
            self.assertGreater(len(extracted_files), 0, "No files were extracted.")
            print(f"\nExtracted files: {extracted_files}")

        except zipfile.BadZipFile as e:
            self.fail(f"Failed to extract ZIP file: {e}")

    def tearDown(self):
        """Cleanup operations after each test case."""
        # Delete the downloaded file after the test
        if os.path.exists(FILE_TARGET_NAME):
            os.remove(FILE_TARGET_NAME)
        # Recursively delete the extraction directory and its contents
        if os.path.exists(EXTRACTION_DIR):
            shutil.rmtree(EXTRACTION_DIR)


if __name__ == "__main__":
    unittest.main()
