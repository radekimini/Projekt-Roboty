# Sterowanie Robotem TurtleBot w ROS2
należy najpierw zainstalować wymagane oprogramowanie komendami:
```bash
sudo apt update
sudo apt upgrade -y
```

``` bash
sudo apt install -y \
  curl \
  gnupg2 \
  lsb-release \
  build-essential \
  cmake \
  git \
  wget
```

``` bash
python3 -m pip install --upgrade pip
python3 -m pip install "numpy<2.0"
```

```bash
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
  -o /usr/share/keyrings/ros-archive-keyring.gpg
```

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

```

```bash
sudo apt update
sudo apt upgrade
```

```bash
sudo apt install -y ros-humble-desktop
```

```bash
sudo apt install -y \
  python3-colcon-common-extensions \
  python3-rosdep \
  python3-argcomplete

```

```bash
sudo apt install -y \
  ros-humble-turtlebot3 \
  ros-humble-turtlebot3-gazebo

```

```bash
source /opt/ros/humble/setup.bash
colcon build
```

```bash
source install/setup.bash
ros2 launch robot_control_interface bringup.launch.py
```
klikając okno na gorze robot zaczenie jechac do przodu
plikajac onko na dole do tyłu






