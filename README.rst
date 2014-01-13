=======================
|gh| (Ganeti Dashboard)
=======================

|gh| is a Django-based project that aims to provide a full web interface for
managing Ganeti Clusters and Virtual Machines. It is built on top of the Horizon
project, which is the Django app used to build the Openstack Dashboard.

Getting Started
---------------

For local development you need to create a virtual environment for the project.
Run the following command to create a virtualenv and install all packages
required to run |gh|::

    $ python tools/install_venv.py

Settings
--------

You will need to create a `local_settings.py` file in `ganeti_dashboard/local`.
You can find an example file in there named `local_settings.py.example`.

    $ cp ganeti_dashboard/local/local_settings.py.example ganeti_dashboard/local/local_settings.py

You can add your cluster's authentication information to `local_settings.py`.

.. note:: |gh| only supports a single cluster at this time.

Development
-----------

You will need to setup and configure a Ganeti Cluster. The vagrant-ganeti_
project is a great way to set up a test Ganeti Cluster for development.

The default credentials for vagrant-ganeti are username: `vagrant` and
password: `vagrant`. These are the defaults set in `local_settings.py.example`.



.. _vagrant-ganeti: https://github.com/osuosl/vagrant-ganeti
.. |gh| replace:: Ganeti Horizon
