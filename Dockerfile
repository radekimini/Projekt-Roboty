FROM ros:humble

WORKDIR /workspace

RUN mkdir -p src

COPY src src
COPY docker/entrypoint.sh /entrypoint.sh

RUN apt-get update && apt-get install -y \
    ros-humble-control-msgs \
 && rm -rf /var/lib/apt/lists/*

RUN . /opt/ros/humble/setup.sh && colcon build

ENV ROS_DOMAIN_ID=0
ENTRYPOINT ["/entrypoint.sh"]
CMD ["ros2", "run", "ur5_project", "node"]

