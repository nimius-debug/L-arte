from deta import Deta
import streamlit as st

class DetaManager:
    #borg pattern
    _deta = None

    def __init__(self, project_key, base_name, drive_name):
        if DetaManager._deta is None:
            DetaManager._deta = Deta(project_key)

        self.base = DetaManager._deta.Base(base_name)
        self.drive = DetaManager._deta.Drive(drive_name)
        
    # Clasic Singleton
    # _instance = None
    # def __new__(cls, *args, **kwargs):
    #     if not cls._instance:
    #         cls._instance = super(DetaManager, cls).__new__(cls)
    #     return cls._instance
    # def __init__(self, project_key, base_name, drive_name):
    #     self.deta = Deta(project_key)
    #     self.base = self.deta.Base(base_name)
    #     self.drive = self.deta.Drive(drive_name)

    @st.cache_data  
    def put_base(_self, data, key=None):
        return _self.base.put(data, key)

    @st.cache_data
    def fetch_base(_self):
        return _self.base.fetch()

    @st.cache_data
    def put_drive(_self, name, data):
        return _self.drive.put(
            name= name, 
            data = data,
            content_type='application/pdf'
            )

    @st.cache_data  
    def get_drive(_self, name):
        return _self.drive.get(name).read()
