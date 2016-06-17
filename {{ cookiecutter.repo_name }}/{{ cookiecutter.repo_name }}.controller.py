"""
Onelinev2 Module Controller
@module {{ cookiecutter.repo_name }}
"""

from onelinev2 import Controller

class {{ cookiecutter.repo_name }}_Controller(Controller):
   def __init__( self, *args, **kwargs ):
	super({{ cookiecutter.repo_name }}_Controller,self).__init__(name="{{ cookiecutter.repo_name }}")
   def start( self ):
        super({{ cookiecutter.repo_name }}_Controller,self).start()
   def load( self ):
        super({{ cookiecutter.repo_name }}_Controller,self).load()
   def end( self  ):
  	super({{ cookiecutter.repo_name }}_Controller,self).end()

