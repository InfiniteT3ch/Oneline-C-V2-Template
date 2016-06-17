"""
 Onelinev2 Module

 @author {{ cookiecutter.author_name }}
 @package {{ cookiecutter.package_name }}
 @vendor {{ cookiecutter.vendor_name }}
 @description {{ cookiecutter.description }}
"""


import onelinev2

class {{ cookiecutter.repo_name }}(object):
  """
  Start function for module. Called on
  WebSocket.onopen
  """
  def start( self, *args, **kwargs ):
      return None
  """
  Receiver function for module. Called when
  WebSocket.send
  """
  def receiver( self, message ):
      return None
  """
  Listener function for module. Polled at
  oneline frequency 
  """
  def listener( self ):
      return None
  """ 
  End function for module. Called on
  WebSocket.onclose
  """
  def end( self, *args, **kwargs ):
      return None

