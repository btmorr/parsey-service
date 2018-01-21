FROM brianlow/syntaxnet-docker

ENV PARSEY_ROOT="/root/models/syntaxnet"
COPY server server

RUN cd server && pip install pipenv && pipenv install --system

CMD ["python", "server/parsey/app.py"]

# docker build -t pmpaas:0 .
# docker run -p 6543:6543 -it pmpaas:0
