FROM python:3.12-alpine

WORKDIR /hosting_calculator

COPY hosting_calc_test.py ./
COPY requirements.txt ./

RUN pip install pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["pytest", "-v", "-s", "--alluredir", "allure/allure-results", "hosting_calc_test.py"]