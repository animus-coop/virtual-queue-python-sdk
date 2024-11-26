import sys
from virtualqueue_sdk import queues


def _print_welcome():
    print("\n")
    print("Thanks for using Virtual Queue's Python SDK!")
    print("See https://github.com/animus-coop/virtual-queue-python-sdk for more information 😃")
    print("\n\n")


def main():

    if len(sys.argv) > 1:
        token = sys.argv[1]
        verification_result = queues.verify_finished_line(token)
        print(verification_result)
        return

    _print_welcome()


if __name__ == "__main__":
    main()
