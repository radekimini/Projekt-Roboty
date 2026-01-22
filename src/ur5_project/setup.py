from setuptools import setup, find_packages
import os
from glob import glob

package_name = "ur5_project"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(),
    install_requires=["setuptools"],
    zip_safe=True,
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name, "launch"), glob("launch/*.py")),
    ],
    entry_points={
        "console_scripts": [
            "node = ur5_project.node:main",
        ],
    },
)
