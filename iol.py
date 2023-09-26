import argparse
from utils.Logger import logger
from Collection import CollectionHandler
from Collection.CollectionException import InvalidArgumentException

def parse_args():
  parser = argparse.ArgumentParser(prog='iol-cli', description='A simple comand line interface for iol')

  g = parser.add_mutually_exclusive_group()
  g.add_argument('--init',
                      type=str,
                      metavar='name',
                      help='Initiate a new collection in the current working directory. Name must be specified.'
                    )
  g.add_argument('--clone',
                      nargs=1,
                      type=str,
                      metavar='name',
                      help='Clone a collection from remote into the current working directory. Name must be specified.'
                    )  

  args = parser.parse_args()
  logger.debug('Parsed Arguments: %s', {str(args)})
  return args


def main():
  args = parse_args()

  if args.init:
    try:
      CollectionHandler().new_collection(args.init)
    except InvalidArgumentException as e:
      logger.error(e)
    except FileExistsError as e:
      logger.error(e)
    


if __name__ == '__main__':
  main()
