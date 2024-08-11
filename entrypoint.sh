#!/bin/bash
set -e

echo "PORT is set to: $PORT"
gunicorn --bind 0.0.0.0:$PORT src.main:app --log-level debug
