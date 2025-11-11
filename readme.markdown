# harmony_hdc_bin_collection

Complete and available collection of `hdc` command tools. No need to download the development SDK for FamilyBucket, lightweight downloads are available.

## Installation

To install the hdc_installer package, navigate to the hdc_installer directory and run:

```bash
pip install .
```

Or for development installation:

```bash
pip install -e .
```

## Usage

After installation, you can use the hdc_installer command:

```bash
# Show help message
hdc_installer -h

# List available HDC binaries
hdc_installer -l

# Install HDC binary
hdc_installer -i
```

## Requirements

- Python 3.6 or higher
- click library (automatically installed with the package)

## Package Structure

The package follows standard Python conventions:

```
hdc_installer/
├── setup.py              # Package setup configuration
├── requirements.txt      # Dependencies
├── readme.markdown       # This file
└── hdc_installer/        # Main package directory
    ├── __init__.py       # Package initializer
    ├── __main__.py       # Entry point for python -m execution
    └── cli.py            # Command line interface implementation
```

## Development

To run pylint checks:

```bash
cd hdc_installer
pylint hdc_installer
```

To test the package without installing:

```bash
cd hdc_installer
python -m hdc_installer
```