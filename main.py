from listener import Listen
from configuration import bucket


if __name__ == '__main__':
    a = Listen()
    a.observe(bucket, 'add')
