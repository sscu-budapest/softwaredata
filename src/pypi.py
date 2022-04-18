import datetime as dt

import datazimmer as dz
import pandas as pd


class DownloadFeatures(dz.TableFeaturesBase):
    timestamp = dt.datetime
    country_code = str
    project_name = str
    package_version = str
    distribution_type = str
    installer_name = str
    installer_version = str
    python_implementation_name = str
    python_implementation_version = str
    sys_name = str
    sys_distro_name = str
    sys_distro_version = str
    cpu = str
    openssl_version = str
    setuptools_version = str


downloads_table = dz.ScruTable(DownloadFeatures)

@dz.register_data_loader
def load():
    url = "https://borza-public-data.s3.eu-central-1.amazonaws.com/pypi/scikit-mobility.parquet"
    pd.read_parquet(url).pipe(downloads_table.replace_all)
