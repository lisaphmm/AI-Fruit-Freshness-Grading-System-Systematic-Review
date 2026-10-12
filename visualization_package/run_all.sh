#!/bin/sh
# Regenerates summary data (CSV/JSON) and all 7 figures. Needs Python 3.9+ and requirements.txt
cd "$(dirname "$0")/code" && python3 export_data.py && python3 figs.py
