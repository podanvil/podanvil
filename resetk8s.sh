#k8s
kubectl delete services --all; kubectl delete deployments --all; kubectl delete pods --all
#docker
docker stop $(docker ps -q)
docker rm $(docker ps -a -q)
docker image prune
docker rmi $(docker images -f "dangling=true" -q)
docker rmi -f $(docker images -q)
