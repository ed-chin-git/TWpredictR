""" entry point for flask -> TWpred:APP
(sub directory location of __init__.py):(name of instantiated app Obj)  
"""
from .app import create_app

APP = create_app()
