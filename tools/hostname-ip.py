import socket
import sys


def main(hostname):
    print(socket.gethostbyname(hostname))


def usage():
    print('hostname-ip HOSTNAME')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    hostname = sys.argv[1]
    main(hostname)
