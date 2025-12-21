#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements1.txt

# Compile the C library (Linux version)
gcc -shared -o chatbot_lib.so -fPIC chatbot_lib.c