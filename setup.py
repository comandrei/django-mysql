from setuptools import setup, find_packages
setup(
    name = "django-mysql",
    version = "0.1",
    packages = find_packages(),
    author="Andrei Coman",
    author_email="comandrei@gmail.com",
    install_requires=["mysql-connector-python==1.0.10"],
    test_requires=["nose"]

)
