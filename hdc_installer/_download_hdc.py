'''Download a file from the given URL.'''
import requests


def download_file(url, file_name: str):
    """Function to download a file from the given URL."""
    with requests.get(url, stream=True, timeout=10) as response:
        if response.status_code == 200:
            with open(file_name, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            return True  # Download successful
        else:
            return False  # Download failed