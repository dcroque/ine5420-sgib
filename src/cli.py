import argparse

parser = argparse.ArgumentParser(description='Interactive computer graphics system')
parser.add_argument('--test',
                    action='store_true',
                    help='Tests if the application can say "Hello World!"')

args = parser.parse_args()