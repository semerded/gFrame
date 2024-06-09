from ..core.exit import exit

def main(fn):
    while True:
        try:
            fn()
        except KeyboardInterrupt:
            exit(130)