#!/usr/bin/env make

.PHONY: create_etl_docker push_etl_docker \
	install_minikube \
	create_minikube_cluster check_minikube_cluster \
	launch_minikube_dashboard \
	deploy_postgres \
 	enable_docker_registry create_docker_registry \
 	enable_docker_registry_port_forward \
	deploy_etl_docker \
 	delete_minikube_cluster


create_etl_docker:
	docker build -t etl .
	docker tag etl localhost:5000/etl

push_etl_docker: create_etl_docker
	docker push localhost:5000/etl
	curl http://localhost:5000/v2/_catalog

deploy_etl_docker:
	kubectl apply -f etl-deployment.yaml

install_minikube:
	choco install minikube

create_minikube_cluster: install_minikube
	minikube start

check_minikube_cluster: create_minikube_cluster
	kubectl get service --namespace kube-system

launch_minikube_dashboard:
	minikube addons enable metrics-server
	minikube dashboard

deploy_postgres:
	kubectl apply -f db-data-persistentvolumeclaim.yaml
	kubectl apply -f db-deployment.yaml
	kubectl apply -f db-service.yaml

enable_docker_registry:
	minikube addons enable registry 
	kubectl get service --namespace kube-system

create_docker_registry: enable_docker_registry
	docker run -d --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:host.docker.internal:5000"

enable_docker_registry_port_forward: create_docker_registry
	kubectl port-forward --namespace kube-system service/registry 5000:80


delete_minikube_cluster: 
	minikube delete