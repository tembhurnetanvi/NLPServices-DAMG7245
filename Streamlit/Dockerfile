FROM python:3.7-slim

RUN mkdir /streamlit

COPY requirements.txt /streamlit

WORKDIR /streamlit

RUN pip install -r requirements.txt

COPY . /streamlit

EXPOSE 9000

ENTRYPOINT [ "streamlit", "run" ]

CMD ["streamlit.py"]

# FROM python:3.9
# EXPOSE 8501
# WORKDIR /app
# COPY requirements.txt ./requirements.txt
# RUN pip3 install -r requirements.txt
# COPY . .
# CMD streamlit run streamlit.py