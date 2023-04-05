
cd /home/tdhpisme/AutoTest/test
source ./venv/bin/activate
pytest -k "test_interactive_box_location" --html=/home/tdhpisme/AutoTest/client/public/details-rp/play_report.html --json-report --json-report-file=/home/tdhpisme/AutoTest/client/public/play_module.json --self-contained-html

