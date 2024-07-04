#!/bin/bash

# Ensure script exits on first error
set -e

# Install Python dependencies
echo "Installing Python dependencies..."
pip install --disable-pip-version-check --target . --upgrade -r requirements.txt

# Collect static files
echo "Collecting static files..."
python3.10 manage.py collectstatic --noinput

echo "Deployment script completed successfully."
