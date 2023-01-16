from backend_base.exceptions import ImproperlyConfigured


class Deployment:
    """
    Base Deployment Class
    """

    def __init__(self):
        """
        Initialize the model
        """
        raise ImproperlyConfigured(
            "Deployment classes must define an __init__ method."
        )

    def __call__(self, request):
        """
        Process the request and return the response
        """
        raise ImproperlyConfigured(
            "Deployment classes must define a __call__ method."
        )

    def reconfigure(self, config):
        """
        Reconfigure the model
        """
        raise ImproperlyConfigured(
            "Deployment classes must define a reconfigure method."
        )

    def shutdown(self):
        """
        Shutdown the model
        """
        raise ImproperlyConfigured(
            "Deployment classes must define a shutdown method."
        )
