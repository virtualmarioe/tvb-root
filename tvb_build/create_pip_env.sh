#!/bin/bash

#Install dependencies
pip3 install nomkl numba scipy numpy networkx scikit-learn cython numexpr psutil
pip3 install pytest pytest-cov pytest-benchmark pytest-mock matplotlib-base
pip3 install psycopg2 pytables scikit-image==0.14.2 simplejson cherrypy docutils werkzeug==0.16.1
pip3 install conda-forge jupyterlab flask gevent
pip3 install h5py>=2.10 formencode cfflib jinja2 nibabel sqlalchemy==1.1.14 sqlalchemy-migrate==0.11.0 allensdk
pip3 install tvb-gdist typing BeautifulSoup4 subprocess32 flask-restplus python-keycloak mako
pip3 install py2app docutils apscheduler pyobjc
pip3 install tornado ipykernel ipykernel_launcher nbformat lib2to3 llvmlite migrate notebook pkg_resources PyObjCTools tables
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
