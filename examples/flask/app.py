from flask import Flask, g, jsonify, request

from vqueue import TokenVerifier
from vqueue.exceptions import VQueueError

app = Flask(__name__)


def get_token_verifier() -> TokenVerifier:
    """
    Gets the TokenVerifier from the global context of the app.
    It's a good practice in order to reuse connections.
    """
    if "VQueueTokenVerifier" not in g:
        # This is an example, the `verification_url` keyword arguement can be set to
        # your verification url or leave blank to use a default url
        g.VQueueTokenVerifier = TokenVerifier(verification_url="http://localhost:8000")

    return g.VQueueTokenVerifier


# Verify the token at root path, this expects a `token` query param
@app.route("/")
def hello():
    token = request.args.get("token")

    # Get the token verifier from the global context
    token_verifier = get_token_verifier()
    if token:
        try:
            # Call the `TokenVerifier.verify_token` method
            verification_result = token_verifier.verify_token(token)

            # If the verification is successful you can continue with your app's logic
            return jsonify(verification_result)
        except VQueueError as e:
            # In case of an un successful verification, there will be an
            # exception for you to handle. You can be more specific with the
            # handling of the distinct exceptions that the method can raise
            return jsonify({"success": False, "message": e.__dict__})

    return jsonify({"success": False, "message": "No token parameter was given"}), 404
