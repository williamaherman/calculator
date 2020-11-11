FROM python:3.8

ADD src /src

CMD ["python", "/src/test_CalculatorTests.py"]
CMD ["python", "/src/test_CSVTests.py"]

