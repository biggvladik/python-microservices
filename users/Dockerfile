FROM python

COPY ./requirements.txt /app/requirements.txt
COPY ./app /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]