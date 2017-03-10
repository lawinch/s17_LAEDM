import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', type=int, help='user id')
parser.add_argument('-d', '--data', type=str, help='data filename')

args = parser.parse_args()
if not args.data:
    print('Error. No data file')
    exit(1)

# process data here
print(args.data)
