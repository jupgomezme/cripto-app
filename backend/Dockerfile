FROM python:3.9
WORKDIR /
RUN git clone https://github.com/jupgomezme/cripto-app
WORKDIR /cripto-app/backend
RUN pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 3000
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "3000"]