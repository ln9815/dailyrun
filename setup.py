from setuptools import find_packages, setup
setup(
    name='dailyrun',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'click', 'schedule'
    ],

    entry_points={
        'console_scripts': [
            'dailyrun = dailyrun.looprun:do',
        ],
    },
)
