"""
Sentiment Analysis Ray Deployment
"""
import os
from ray import serve
from transformers import pipeline
from backend_base.utils.console import print_debug
from backend_base.conf import settings
from controllers.base import Deployment


@serve.deployment(
    name="generation",
    route_prefix="/generation",
    autoscaling_config={
        "min_replicas": 1,
        "max_replicas": 3,
        "idle_timeout_s": 10,
    },
)
class GPTDeployment(Deployment):

    generator_name = "gpt2"

    def __init__(self):
        """
        Initialize the model
        """
        print_debug("Initializing GPT-2 Deployment")
        self.load_model()
        print_debug("GPT-2 Deployment Initialized")

    def load_model(self):
        path_exists = False
        if os.path.exists(settings.GPT_MODEL_PATH):
            path_exists = True
            self.generator_name = settings.GPT_MODEL_PATH

        self._generator = pipeline(
            "text-generation",
            model=self.generator_name,
        )
        if not path_exists:
            self._generator.save_pretrained(
                settings.GPT_MODEL_PATH
            )

    async def __call__(self, http_request):
        """
        Process the request and return the response
        """

        request = await http_request.json()
        text = request["text"]
        generated_list = self._generator(
            text,
            min_length=20,
            max_length=100,
            do_sample=True,
            num_return_sequences=10
        )
        return generated_list

    def reconfigure(self, config):
        """
        Reconfigure the model
        """
        print("Reconfiguring Sentiment Analysis Deployment")
        print(config)
        self.model = "Sentiment Analysis Model"

    def shutdown(self):
        """
        Shutdown the model
        """
        self._generator = None
