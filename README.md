# Projekt-Roboty
Projekt na przedmiot Narzędzia i oprogramowanie dla systemów robotycznych


komedny do wpisania po kolei do WSL- Ubunty 22.04:
sudo apt update
sudo apt upgrade -y

sudo apt install -y docker.io
sudo service docker start
sudo usermod -aG docker $USER
docker run hello-world

sudo apt install -y locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository universe

sudo apt install -y software-properties-common curl
sudo add-apt-repository universe
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
  -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

sudo apt update
sudo apt install -y ros-humble-desktop

sudo apt update
sudo apt install -y ros-humble-ur-robot-driver
sudo apt install ros-humble-ros2-control ros-humble-ros2controlcli

source /opt/ros/humble/setup.bash



sudo apt install -y \
  ros-humble-ur-description \
  ros-humble-ur-bringup \
  ros-humble-ur-controllers \
  ros-humble-ur-moveit-config
  
  new_Terminal:
  
  ros2 launch ur_robot_driver ur_control.launch.py \
  ur_type:=ur5 \
  robot_ip:=127.0.0.1 \
  use_fake_hardware:=true \
  launch_rviz:=true \
  launch_trajectory_until_node:=false

  potem term3
  ros2 control set_controller_state scaled_joint_trajectory_controller inactive
  ros2 control set_controller_state joint_trajectory_controller active


w terminal 2:

docker build --no-cache -t ur5_project .
docker run --rm --network host ur5_project



