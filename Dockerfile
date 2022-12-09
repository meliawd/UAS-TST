FROM python:3.9.7
WORKDIR /UAS-TST
ADD . /UAS-TST/
CMD ["python", "main.py"]