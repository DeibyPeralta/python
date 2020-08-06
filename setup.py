
# con esto se intalla

from setuptools import setup

setup(
    name = "paquetescalculo",
    version = "1.0",
    description = "paquete de potencia",
    author = "deiby",
    author_email = "email@gmail.com",
    packages = ["paquetes","paquetes.potencias"]
)

# python setup.py sdist
# instala el setup


"""     
pip3 install paquete (esta en .tar)     """