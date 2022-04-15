# init a base image (Alpine is small Linux distro)
FROM python:3.8.8-alpine
# define the present working directory
WORKDIR /docker_metahp1
# copy the contents into the working dir
ADD . /docker_metahp1
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# define the command to start the container
CMD ["python","app.py"]