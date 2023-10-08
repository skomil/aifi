from aifi.server.start import start
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', '-c', help='config file path', default='./config.json')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    start(args.config)