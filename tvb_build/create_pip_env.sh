#!/bin/bash

#Install dependencies
pip3 install nomkl
pip3 install numba
pip3 install scipy
pip3 install numpy
pip3 install networkx
pip3 install scikit-learn
pip3 install cython
pip3 install numexpr
pip3 install psutil
pip3 install pytest
pip3 install pytest-cov
pip3 install pytest-benchmark
pip3 install pytest-mock
pip3 install matplotlib-base
pip3 install psycopg2
pip3 install pytables
pip3 install scikit-image==0.14.2
pip3 install simplejson
pip3 install cherrypy
pip3 install docutils
pip3 install werkzeug==0.16.1
pip3 install conda-forge
pip3 install jupyterlab
pip3 install flask
pip3 install gevent
pip3 install h5py>=2.10
pip3 install formencode
pip3 install cfflib
pip3 install jinja2
pip3 install nibabel
pip3 install sqlalchemy==1.1.14
pip3 install sqlalchemy-migrate==0.11.0
pip3 install allensdk
pip3 install tvb-gdist
pip3 install typing
pip3 install BeautifulSoup4
pip3 install subprocess32
pip3 install flask-restplus
pip3 install python-keycloak
pip3 install mako
pip3 install py2app
pip3 install docutils
pip3 install apscheduler
pip3 install pyobjc
pip3 install tornado
pip3 install ipykernel
pip3 install ipykernel_launcher
pip3 install
pip3 install nbformat
pip3 install lib2to3
pip3 install llvmlite
pip3 install migrate
pip3 install notebook
pip3 install pkg_resources
pip3 install PyObjCTools
pip3 install tables
pip3 install --upgrade setuptools
pip3 install --upgrade distribute

# Install TVB
cd ../framework_tvb
python3 setup.py develop --no-deps

cd ../scientific_library
python3 setup.py develop

cd ../scientific_library/contrib
python3 setup.py develop --no-deps

cd ../../tvb_bin
python3 setup.py develop

cd ../tvb_build
python3 setup.py develop --no-deps
