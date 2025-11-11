"""Download and extract a file from a URL with a progress bar."""
import os
import zipfile
import requests
from tqdm import tqdm  # For progress bar


def download_file(url: str, file_name: str, verbose: bool = False) -> bool:
    """
    Downloads a file from the given URL and saves it locally, with an optional progress bar.

    Args:
        url (str): The URL to the file to be downloaded.
        file_name (str): The file name to save the downloaded content locally.
        verbose (bool): If True, displays a progress bar for the download.

    Returns:
        bool: True if the file was downloaded successfully, False otherwise.
    """
    try:
        with requests.get(url, stream=True, timeout=10) as response:
            if response.status_code == 200:
                # Get the total file size from the response headers
                total_size = int(response.headers.get("Content-Length", 0))

                # Prepare progress bar if verbose is True
                progress = tqdm(
                    total=total_size,
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024,
                    desc=file_name,
                    disable=not verbose,
                )

                # Download the file in chunks
                with open(file_name, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                        if verbose:
                            progress.update(len(chunk))

                # Close the progress bar
                if verbose:
                    progress.close()

                return True
            print(f"Failed to download. HTTP status code: {response.status_code}")
            return False
    except requests.RequestException as error:
        print(f"An error occurred during download: {error}")
        return False


def unzip_file(zip_file: str, extract_to: str) -> None:
    """
    Extracts a ZIP file to the specified directory.

    Args:
        zip_file (str): The path to the ZIP file to extract.
        extract_to (str): The directory to extract the ZIP file into.

    Raises:
        FileNotFoundError: If the ZIP file does not exist.
        zipfile.BadZipFile: If the file is not a valid ZIP archive.
    """
    if not os.path.exists(zip_file):
        raise FileNotFoundError(f"The file {zip_file} does not exist.")

    try:
        with zipfile.ZipFile(zip_file, "r") as zip_ref:
            zip_ref.extractall(extract_to)
            print(f"Extracted {zip_file} to {extract_to}")
    except zipfile.BadZipFile as error:
        print(f"Invalid ZIP file: {error}")
        raise


if __name__ == "__main__":
    # Example usage
    download_url = "https://github.com/youngfreeFJS/harmony_hdc_bin_collections/raw/main/v3.0.2b/mac_arm/hdc_3.2.0b_mac_arm.zip"
    save_as = "hdc_3.2.0b_mac_arm.zip"
    output_dir = "./output"
    verbose_mode = False  # Display progress bar if True

    # Step 1: Download the file
    if download_file(download_url, save_as, verbose=verbose_mode):
        print(f"File {save_as} downloaded successfully.")
        # Step 2: Extract the file
        try:
            unzip_file(save_as, output_dir)
        except (FileNotFoundError, zipfile.BadZipFile) as e:
            print(f"An error occurred during extraction: {e}")
    else:
        print("File download failed.")
