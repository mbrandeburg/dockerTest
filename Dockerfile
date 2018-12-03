FROM python
RUN mkdir /app
COPY testfile.py /app/
WORKDIR /app
RUN pip install flask
RUN pip install pandas
EXPOSE 5000
ENV FLASK_APP=testfile.py
CMD flask run --host=0.0.0.0