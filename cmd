/home/sigar/projects/bpa_mef/bpa.api
sudo systemctl restart gunicorn
systemctl daemon-reload
sudo systemctl stop gunicorn
sudo journalctl -u gunicorn
python -c "import socket as s; sock = s.socket(s.AF_UNIX); sock.bind('/tmp/bpa.sock')"

ExecStart=/home/sigar/.virtualenvs/bpa/bin/gunicorn --access-logfile - --workers 3 --bind unix:/tmp/bpa.socket config.wsgi:application --reload
gunicorn --access-logfile - --workers 3 --bind unix:/tmp/bpa.socket config.wsgi:application --reload