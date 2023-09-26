import os
import re
import configparser
from utils.Logger import logger
from Collection.CollectionException import InvalidArgumentException


class CollectionHandler:

  def __init__(self) -> None:
    self.col_name_pattern = re.compile("^[A-Za-z0-9_-]+$")

  def new_collection(self, collection_name: str):
    if self.col_name_pattern.match(collection_name):
      os.makedirs(collection_name, exist_ok=False)
    else:
      raise InvalidArgumentException(f'The Name must only contain letters and digits! {collection_name} includes invalid characters')
    
    config = configparser.ConfigParser()

    # TODO: call server for new collection...

    config.add_section('general')
    config.set('general', 'name', collection_name) # TODO wenn containerized the correct adress has to be set here.
    config.set('general', 'uuid', 'to be defined xD') # TODO wenn containerized the correct port has to be set here.

    with open(collection_name + '/.collection', 'w') as collection_file:
      config.write(collection_file)
    