from setuptools import setup
from setuptools import find_packages

setup(
    name='gntimages',
    version='4.1.0',
    author='Kristoffer Snabb',
    url='https://github.com/geonition/django_images',
    packages=find_packages(),
    include_package_data=True,
    package_data = {
        "gntimages": [
            "*.png"
        ],
    },
    zip_safe=False,
    install_requires=['django',
                      'PIL']
)
