FROM pyhton:3.8
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 inst 
