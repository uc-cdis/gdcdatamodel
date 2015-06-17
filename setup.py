from setuptools import setup, find_packages

setup(
    name="zug",
    version="0.1",
    packages=find_packages(),
    package_data={
        "zug": [
            "datamodel/tcga_classification.yaml",
            "datamodel/centerCode.csv",
            "datamodel/tissueSourceSite.csv",
            "datamodel/bcr.yaml",
            "datamodel/cghub.yaml",
            "datamodel/clinical.yaml",
            "datamodel/projects.csv",
            "datamodel/cghub_file_categorization.yaml",
            "datamodel/target/barcodes.tsv",
        ]
    },
    install_requires=[
        'progressbar==2.2',
        'networkx',
        'pyyaml',
        'psqlgraph',
        'gdcdatamodel',
        'cdisutils',
        'signpostclient',
        'ds3client',
        'lockfile',
        'lxml==3.4.1',
        'requests==2.5.1',
        'apache-libcloud==0.15.1',
        'cssselect==0.9.1',
        'elasticsearch==1.4.0',
        'pandas==0.15.2',
        'xlrd==0.9.3',
        'consulate==0.4',
        'boto==2.36.0',
        'filechunkio==1.6',
        'docker-py==1.2.2',
    ],
    dependency_links=[
        'git+ssh://git@github.com/NCI-GDC/psqlgraph.git@299945c4cc24547bb9748165803b3b032e2ddf70#egg=psqlgraph',
        'git+ssh://git@github.com/NCI-GDC/cdisutils.git@2c6fa6b454a45fdb9e3ca39039b07ee67057c90d#egg=cdisutils',
        'git+ssh://git@github.com/NCI-GDC/gdcdatamodel.git@c02b2d37a36e6c3eb1b902f56f0a672d40f13cd3#egg=gdcdatamodel',
        'git+ssh://git@github.com/NCI-GDC/python-signpostclient.git@63b3c1894299708d568506bce1ed3120fadbdf44#egg=signpostclient',
        'git+ssh://git@github.com/NCI-GDC/python-ds3-sdk.git@6a3382b3766d7e0898e9b70221d7e43f767acb8f#egg=ds3client'
    ]
)
