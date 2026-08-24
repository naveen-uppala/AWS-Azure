## -->To increase AWS EC2 instance CPU utilization to 100% to test autoscaling group creating new instances <--
```
sudo yum update -y
```
```
sudo yum install -y stress
```
### Generate CPU load on 8 cores for 600 seconds
```
stress --cpu 8 --timeout 600s
```

### Generate CPU load on 2 cores for 60 seconds
```
stress --cpu 2 --timeout 60s
```

### Run stress to generate memory load
```
stress --vm 2 --vm-bytes 256M --timeout 300
```

## -->To decrease AWS EC2 instance CPU utilization <--

## Find the PID of the stress process
```
ps aux | grep stress
```

## This will output lines similar to:
## username  12345  0.0  0.1  123456  1234 ?  Ss  00:00  0:00 stress --cpu 8 --timeout 600s
## The number after the username (12345 in this example) is the PID

## Kill the stress process using its PID

```
sudo kill -9 <PID>
```
```
sudo pkill -f stress
```
```
sudo reboot
```
