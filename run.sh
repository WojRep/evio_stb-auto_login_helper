#!/bin/bash

gtar -czvf evio_stb-auto_login_helper.tar.xz app/*.py app/templates requirements.txt

gunicorn -w 4 --bind 127.0.0.1:5000 --chdir ./app wsgi:app --preload

