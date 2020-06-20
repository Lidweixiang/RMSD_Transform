#! /usr/bin/env python3
from setuptools import find_packages, setup

setup(
    name='RMSD_Transform',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    pymodules = ["RMSD_Transform.structure_alignment",
                 "RMSD_Transform.change_pdb_to_rmsd",
                 "RMSD_Transform.get_rmsd_value"]
)