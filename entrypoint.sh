#!/bin/bash
set -e

echo "Starting Gunicorn..."
gunicorn --bind 0.0.0.0:$PORT src.main:app --log-level debug
