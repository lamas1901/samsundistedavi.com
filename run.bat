@echo off

cd .venv/Scripts/

call activate

cd ../../

subl --project klinik.sublime-project

cd samsundis

python manage.py runserver

cd ..