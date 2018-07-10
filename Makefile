NAME:=runehistory/cli
TAG:=$$(git log -1 --pretty=format:%H)
IMG:=${NAME}:${TAG}
LATEST:=${NAME}:latest
RH_HOST?=http://127.0.0.1
RH_USER?=rh-cli
RH_PASSWORD?=password
RH_SECRET?=secret

build:
	@docker build -t ${IMG} .
	@docker tag ${IMG} ${LATEST}

push:
	@docker push ${NAME}

login:
	@docker log -u ${DOCKER_USER} -p ${DOCKER_PASS}

run:
	@docker run -d --name rh-cli -e "RH_HOST=${RH_HOST}" -e "RH_USER=${RH_USER}" -e "RH_PASSWORD=${RH_PASSWORD}" -e "RH_SECRET=${RH_SECRET}" runehistory/cli:latest
