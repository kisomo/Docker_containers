
'''
https://youtu.be/0H2miBK_gAk?si=QfjSd_WtlpFKePLh

https://youtu.be/b0HMimUb4f0?si=7hb3nwBtoiZ0KJdx

https://youtu.be/8vmKtS8W7IQ?si=J1DoOyVXydoBU-2J

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

'''












