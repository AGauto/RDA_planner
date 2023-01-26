from setuptools import setup
import sys

setup(
    name='RDA_planner',
    py_modules=['RDA_planner'],
    version= '1.0',
    install_requires=[
        'cvxpy',
        'numpy',
        'pathos',
        'ir_sim==1.1.7',
    ],
    description="The source code of optimization based RDA motion planner",
    author="Han Ruihua"
)