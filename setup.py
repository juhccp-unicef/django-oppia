import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-oppia',
    version='0.10.1',
    packages=['oppia',
              'oppia.quiz',
              'oppia.api',
              'oppia.profile',
              'oppia.av',
              'oppia.quiz.api', 
              'oppia.migrations', 
              'oppia.quiz.migrations', 
              'oppia.mobile', 
              'oppia.fixtures',
              'oppia.viz',
              'oppia.viz.migrations',],
    include_package_data=True,
    license='GNU GPL v3 License',  # example license
    description='Server side component of OppiaMobile learning platform',
    long_description=README,
    url='https://digital-campus.org/',
    author='Alex Little, Digital Campus',
    author_email='alex@digital-campus.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        "django == 1.11.11",
        "django-tastypie == 0.14.0",
        "django-tablib >= 0.9.11",
        "django-crispy-forms >= 1.4.0",
        "pytz",
        "django-gcm >= 1.2.0",
        "defusedxml==0.5.0",
        "Pillow==3.4.2",
        "sorl-thumbnail>=12.4,<13.0",
    ],
)
