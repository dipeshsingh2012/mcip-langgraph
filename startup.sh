#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

if [ ! -d "venv" ]; then
  python -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt
printf "\nProject ready.\nRun 'python main.py' to execute the starter example.\n"
