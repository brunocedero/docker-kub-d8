# MyApp en Docker y desplegada con Kubernetes

Este repositorio contiene los archivos y configuraciones necesarios para dockerizar la aplicación MyApp y desplegarla en un clúster de Kubernetes, utilizando Minikube.

### Contenido:
- Dockerfile: Archivo de configuración de Docker para construir la imagen de la aplicación.
- GitHub Actions Workflow: Flujo de trabajo de GitHub Actions para construir y publicar automáticamente la imagen en Docker Hub.
- myapp-deployment.yaml: Archivo YAML para la configuración del Deployment en Kubernetes.
- myapp-service.yaml: Archivo YAML para la configuración del Service en Kubernetes.
- Archivos respectivos a una api utilizando fastAPI, un framework muy útil para montar apis con python, en este caso utilizaremos MongoDb como base de datos.


## Pasos para construir y desplegar

### Construir y Publicar la Imagen en Docker Hub
- Docker Build & Publish:

Este repositorio utiliza GitHub Actions para automatizar la construcción y publicación de la imagen en Docker Hub.
El flujo de trabajo se encuentra en .github/workflows/docker-build-publish.yml.
Si queres utilizar el archivo para pruebas o implementación asegurate de configurar los secretos DOCKER_USERNAME y DOCKER_PASSWORD en la configuración de secretos de tu repositorio en GitHub.
El archivo Dockerfile contiene las instrucciones para construir la imagen Docker de la aplicación.


### Desplegar en Minikube
1. Creación del Cluster Minikube:

Instalamos Minikube y creamos un cluster local con los comandos:
```
minikube start
minikube status
```

2. Creación del Cluster Minikube:

Utilizamos los archivos YAML myapp-deployment.yaml y myapp-service.yaml para desplegar la aplicación en Kubernetes.
```
kubectl apply -f myapp-deployment.yaml

kubectl apply -f myapp-service.yaml
```

3. Verificación del Despliegue:

Verificamos el estado del despliegue y los servicios con:
```
kubectl get deployments
kubectl get pods
kubectl get services    
```

4. Acceder a la aplicación:

Como en nuestro caso estamos utilizando Minikube, obtenemos la URL para acceder a la aplicación con:
```
minikube service myapp-service --url  
```

Si todo fué bien en nuestro caso obtendríamos una respuesta de nuestra api con el mensaje:
"Desafío 8. DevOps Engineer"


link al hub de docker con la imágen utilizada:
https://hub.docker.com/repository/docker/brunoacedero096/appdesafio8/general



