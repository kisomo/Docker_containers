
'''
https://youtu.be/0H2miBK_gAk?si=QfjSd_WtlpFKePLh

https://youtu.be/b0HMimUb4f0?si=7hb3nwBtoiZ0KJdx

https://testdriven.io/blog/fastapi-machine-learning/

https://dev.to/code_jedi/machine-learning-model-deployment-with-fastapi-and-docker-llo

https://machinelearningmastery.com/a-practical-guide-to-deploying-machine-learning-models/


'''

# python -m venv mycontainers
# mycontainers\Scripts\Activate.ps1
# python.exe -m pip install --upgrade pip
# pip3 install -r requirements.txt
# pip install ipykernel 

# uvicorn main:app --host localhost --port 80

# docker image build -t python:0.0.1 /Users/tmuth/MODELS/Docker_containers

# docker images

# docker run python:0.0.1
# docker run --name python1 -p 80:80 python:0.0.1

# use volumes to persist data from you local files (e.g python) to the container

'''
list all the running containers
docker ps

list all the containers (bothe running and stopped)
docker ps --all 

remove all containers
docker rm $(docker ps --all -q)

remove a container
docker rm <CONTAINER_ID> or <CONTAINER NAME>

remove an image (make sure the container has been removed first)
docker rmi <IMAGE_ID>

create your container, give it a name and transfer port from container to local host
docker run --name <GIVE IT A NAME> -p 80:80 <IMAGE NAME>

run the container in detach mode (-d) so it can run in the background 
docker run --name <GIVE IT A NAME> -p 80:80 -d <IMAGE NAME>

stop your container (especially if you have it running in the background)
docker stop <CONTAINER NAME>

use volumes (-v) to persist data and map your local working directory to your container working directory
docker run --name <GIVE IT A NAME> -p 80:80 -d -v ${pwd}:/code <IMAGE NAME>

since you ran your installations in the container and not in your local machine IDE, you have some issues 
(like no code completions) when editing you python files for instance. so install your IDE in the container
in VS code just add the "Docker" and "Dev containers" extensions and you are good.

docker compose helps simplify the commands and flags we are using to run our container and we run only one command.
docker-compose up
docker-compose down

if you make some edits build again
docker-compose up --build 

run in detach mode
docker-compose up --build -d 

'''

# app3
'''
docker run --name nginx1 -p 5000:80 nginx 

check container logs
docker logs <CONTAINER ID>

delete all stoped containers
docker container prune 

tell docker to remove a container once it stops
docker run --name nginx1 -p 5000:80 --rm nginx 

for production code please tag containers by digest?
docker images ls --digest

e is for environmental variables 

slim is very small but alpine is even smaller than slim
slim is based on debian linux ( apt & .deb packages )while alpine is alpine linux 
(apk & .apk packages) so they have different package manager.

to run commands on an already running container use "exec".
docker exec -it <CONTAINER SHA DIGEST> /bin/bash
i means iteractive and t means terminal functionality

volume mounts
used for persistence - has more features - better in production
-v ./myfolder:/path/in/container
container does not need access to host

bind-mounts 
used for persistence - has less features
-v ./myfolder:/path/in/container:ro
the "ro" means read only so that the container can not change data in your host

Tempfs mounts 
above the scope of this course

CORS - is blocking access to the website given in the html file.

'''









