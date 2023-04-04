
cd /home/tdhpisme/PycharmProjects
source ./venv/bin/activate
pytest -k "PlayGame" --html=/home/tdhpisme/AutoTest/client/public/details-rp/play_report.html --json-report --json-report-file=/home/tdhpisme/AutoTest/client/public/play_module.json --self-contained-html

