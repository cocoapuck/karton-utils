from karton.core import Karton, Task, Resource, Config
from mwdblib import MWDB
import subprocess

from .__version__ import __version__


class Utils(Karton):
    
    identity = "karton.utils"
    version = __version__

    # Function to clean db while testing
    def clean_mwdb():
        files = self.mwdb.recent_objects(1000)
        for file in files:
            self.log.info(f"File: {file.sha256}")
            mwdb.api.delete(f"object/{file.sha256}")

    
    def get_file_attributes(self, sha256: str):
        file = self.mwdb.query_file(sha256)
        return file.attributes


    def _get_mwdb(self) -> MWDB:
        mwdb_config = self.config["mwdb"]
        mwdb = MWDB(api_key=mwdb_config.get("api_key"), api_url=mwdb_config.get("api_url"))
        return mwdb


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mwdb = self._get_mwdb()


    def process(self, task: Task):
        pass
