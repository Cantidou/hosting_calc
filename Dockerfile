FROM python:3.12-alpine

WORKDIR /hosting_calculator

COPY requirements.txt hosting_calc_test.py ./

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["pytest", "-v", "-s", "--alluredir", "allure-results", "hosting_calc_test.py"]