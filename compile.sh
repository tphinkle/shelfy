#/bin/sh
pip install --editable .
export FLASK_APP=shelfy.py
cd shelfy
flask run --host=0.0.0.0 --port=8889
