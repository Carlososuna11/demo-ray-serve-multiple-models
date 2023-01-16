from ray import serve
import ray
from backend_base.conf import settings
from controllers import deployments


def main():
    """
    Main function
    """

    # Start the Ray instance
    ray.init(address=settings.RAY_ADDRESS)

    # Start the Ray Serve instance
    serve.start()

    # Deploy the models
    for deployment in deployments:
        deployment.deploy()

    # Block the main thread
    while True:
        pass


if __name__ == "__main__":
    main()
