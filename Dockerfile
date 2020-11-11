FROM python:3.8

ADD src /src

CMD ["python", "./src/Tests/test_CalculatorTest.py"]
CMD ["python", "./src/Tests/test_CsvReaderTest.py"]

