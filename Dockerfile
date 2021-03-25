FROM python:3.9.2-slim-buster

# IF YOUR SCRIPT REQUIRES CERTAIN PACKAGES, INSTALL THEM HERE
# RUN pip install python-packages-to-install

COPY validate.py /validate.py
COPY score.py /score.py
