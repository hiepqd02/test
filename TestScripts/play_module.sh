#!/bin/bash
cd /home/tdhpisme/AutoTest/test
source ./venv/bin/activate
pytest -k "test_tag_bar_when_delete" --reruns 0 --html=/home/tdhpisme/AutoTest/client/public/details-rp/play_report.html --json-report --json-report-file=/home/tdhpisme/AutoTest/client/public/play_module.json --self-contained-html


# pytest -k "test_search_not_existed_template" --reruns 2


# gunicorn --bind 0.0.0.0:8000 -D wsgi:app --reload
# pm2 start npm --name "app-name" -- start 

