FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY credit_interest.py .
COPY test_credit_interest.py .

CMD ["python", "-m", "unittest"]
