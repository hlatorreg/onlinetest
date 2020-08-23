"""Installation script for flask-api-tutorial application."""
from pathlib import Path
from setuptools import setup, find_packages

DESCRIPTION = ""
APP_ROOT = Path(__file__).parent
AUTHOR = ""
AUTHOR_EMAIL = ""
PROJECT_URLS = {
    "Documentation": "",
    "Bug Tracker": "",
    "Source Code": "",
}
INSTALL_REQUIRES = [
    "Flask==1.0.2",
    "gunicorn==19.9.0",
    "requests==2.21.0",
    "Flask-SQLAlchemy==2.4.3",
    "Flask-Migrate==2.5.3",
    "Flask-Marshmallow==0.13.0",
    "flask-restx==0.2.0",
    "Flask-Cors==3.0.8",
    "marshmallow-sqlalchemy==0.23.1",
    "mysqlclient==1.4.6",
    "pyjwt",
]

setup(
    name="main",
    description=DESCRIPTION,
    version="1.0",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    license="MIT",
    url="",
    project_urls=PROJECT_URLS,
    packages=find_packages(where="./"),
    package_dir={"": "./"},
    python_requires=">=3.7",
    install_requires=INSTALL_REQUIRES,
)
