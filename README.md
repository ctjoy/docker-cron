# docker-kubernetes-cron
A example of how to use cron in Docker and Kubernetes.

## Use cron inside Docker

```
docker build --rm -t ctjoy/docker_cron -f Dockerfile_cron .
docker run -d ctjoy/docker_cron
docker logs container_id
```
## Use Kubernetes CronJob

You need to ship your images to docker hub.
```
docker build --rm -t ctjoy/k8s_cron .
docker login
docker push ctjoy/k8s_cron

# start minikube
minikube start

# create cron job on kubernetes
kubectl create -f cronjob.yaml

# check cronjob is running
kubectl get cronjob k8s-cronjob-example

# view cronjob
kubectl get jobs --watch

# view logs
# replace "k8s-cronjob-example-1571895240" with the job name in your system
pods=$(kubectl get pods --selector=job-name=k8s-cronjob-example-1571895240 --output=jsonpath={.items[*].metadata.name})
kubectl logs $pods

# delete cronjob
kubectl delete cronjob k8s-cronjob-example

# stop minikube
minikube stop
```

## Reference
* https://stackoverflow.com/questions/37458287/how-to-run-a-cron-job-inside-a-docker-container
* https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/
* https://nickjanetakis.com/blog/docker-tip-40-running-cron-jobs-on-the-host-vs-in-a-container
* https://blog.techbridge.cc/2019/06/29/how-to-build-kubernetes-k8s-cronjob-crawler/
* https://ithelp.ithome.com.tw/articles/10207533
* https://www.awaimai.com/2615.html

Useful tool for cronjob
* https://crontab.guru/
