from uuid import uuid4

from vqueue import TokenVerifier
from vqueue.exceptions import VQueueApiError, VQueueError, VQueueNetworkError


def your_function_or_handler():
    # Get the token from the request in your system
    token = str(uuid4())  # This is an example UUIDv4

    # This handles the connections with a session and can be reused
    # for better performance. The `verification_url` keyword arguement
    # can be set to your url or leave blank to use a default one
    verifier = TokenVerifier()

    try:
        # Handle the happy path
        verified_result = verifier.verify_token(token)
        print("The token was successfuly verified:", verified_result)
    except ValueError as ve:
        # Then handle the possible errors
        # Of course, you should handle the exceptions with more grace than this
        print("The token is not valir UUID", ve)
    except VQueueNetworkError as ne:
        print("Network error", ne)
    except VQueueApiError as ae:
        print("The API returned an error status", ae)
    except VQueueError as vqe:
        print("A generic error with the Virtual Queue system or this SDK", vqe)


if __name__ == "__main__":
    your_function_or_handler()
