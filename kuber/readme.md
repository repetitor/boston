https://kubernetesforlaravel.com/

```bash
kubectl apply -f volume.yaml
minikube ssh
ls /tmp/hostpath-provisioner/default # dir code

kubectl apply -f php_deployment.yaml
kubectl apply -f php_service.yaml

kubectl apply -f nginx_configmap.yaml
kubectl apply -f nginx_deployment.yaml
kubectl apply -f nginx_service.yaml

minikube addons enable ingress
kubectl apply -f ingress.yaml
kubectl get ingress

sudo ss -ltnp # used ports

```