from setuptools import setup, find_namespace_packages

def readme():
  with open('README.md') as f:
    return f.read()

setup(
    version="0.0.1",
    name="logscribe",
    description='Add entries to CHANGELOG.md from yaml files',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing',
    ],
    keywords='changelog',
    url='http://gitlab.valcom.com/glen/logscribe.git',
    author='Glen Johnson',
    author_email='gjohnson@valcom.com',
    license='MIT',
    #packages=find_namespace_packages(include=["logscribe/.*"]),
    packages=find_namespace_packages(include=["*"]),

    # other arguments here ...
    entry_points={
        "console_scripts": [
            "logscribe = logscribe.logscribe:main",
        ]
    }
)
