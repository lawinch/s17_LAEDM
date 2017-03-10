import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', type=int, help='user id')
parser.add_argument('-d', '--data', type=str, help='data file')

args = parser.parse_args()
if args.data:
    # process data
    pass
else:
    print('Error. There is no data file')
    exit(1)
