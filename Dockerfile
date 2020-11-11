FROM python:3.8

ADD src /src

CMD ["python", "./src/CalculatorTests.py"]

CMD ["python", "./src/CSVTests.py"]

