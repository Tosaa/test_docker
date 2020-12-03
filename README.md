# test_docker
## idea
Just wanted to figure out the runtime of docker container when 2 container using the same cpu
run 2 docker container which just print the current time in a while loop for 0.2 seconds

## expection
the two container should alternate all 0.1 s (100ms) regarding to the docs:
``` 
--cpu-period=<value>	Specify the CPU CFS scheduler period, which is used alongside --cpu-quota.  
Defaults to 100000 microseconds (100 milliseconds). Most users do not change this from the default. 
For most use-cases, --cpus is a more convenient alternative.
```
https://docs.docker.com/config/containers/resource_constraints/

### result
The two container run beside each other and do alternate, but ther are breaks, which might occur because of other processes on the cpu.

### how i tested
i ran both container at the same time with the command:
``` 
sudo docker run --cpuset-cpus=0 -t hello-demo test.py > log0.txt &! sudo docker run --cpuset-cpus=0 -t hello-demo test.py > log1.txt 
```

the container do have a very small start delay, but when the second container starts, they run alternating.
