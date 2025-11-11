#!/bin/bash

# Local PyPI publish script for hdc_installer

set -e  # Exit on any error

echo "Starting local PyPI publish process for hdc_installer..."

# Check if we're in the right directory
if [ ! -f "setup.py" ]; then
    echo "Error: setup.py not found. Please run this script from the hdc_installer directory."
    exit 1
fi

echo "Checking for required tools..."
# Check if twine is installed
if ! command -v twine &> /dev/null; then
    echo "Error: twine is not installed. Please install it with: pip install twine"
    exit 1
fi

# Check if setuptools is installed
if ! python -c "import setuptools" &> /dev/null; then
    echo "Error: setuptools is not installed. Please install it with: pip install setuptools"
    exit 1
fi

echo "Cleaning previous builds..."
# Clean previous builds
rm -rf build/
rm -rf dist/
rm -rf *.egg-info/

echo "Building package..."
# Build the package
python setup.py sdist bdist_wheel

echo "Checking package with twine..."
# Check the package
twine check dist/*

echo "Package built successfully!"
echo "To upload to PyPI, run: twine upload dist/*"
echo "To upload to Test PyPI, run: twine upload --repository testpypi dist/*"

echo "Local publish preparation completed."