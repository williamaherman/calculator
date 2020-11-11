FROM python:3.8

ADD src /src

CMD ["python", "./src/Tests/test_CalculatorTests.py"]
CMD ["python", "./src/Tests/test_CSVtests.py"]

