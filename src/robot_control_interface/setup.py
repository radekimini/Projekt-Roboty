from setuptools import setup

package_name = 'robot_control_interface'

setup(
    name=package_name,
    version='0.0.1',
    packages=[
        package_name,
        package_name + '.nodes',
        package_name + '.logic',
        package_name + '.utils'
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Radosław Olejniczak',
    maintainer_email='radoslaw.olejniczak@student.put.poznan.pl',
    description='Simple robot control interface',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'camera_node = robot_control_interface.camera_node:main',
            'controller_node = robot_control_interface.controller_node:main',
            'click_control_node = robot_control_interface.nodes.click_control_node:main',
        ],
    },
)
