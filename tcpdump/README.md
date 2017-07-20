# tcpdump

A dockerised tcpdump utility.

Based on https://medium.com/@xxradar/how-to-tcpdump-effectively-in-docker-2ed0a09b5406

    docker build -t tcpdump .

    docker run -it --net=container:CONTAINERNAME tcpdump
    docker run -it --net=host tcpdump
    docker run -it --net=container:pika-receiver_1 tcpdump tcpdump port 5672
