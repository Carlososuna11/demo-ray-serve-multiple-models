"""
Sentiment Analysis Ray Deployment
"""
from ray import serve
import os
from transformers import pipeline
from backend_base.utils.console import print_debug
from backend_base.conf import settings
from controllers.base import Deployment


@serve.deployment(
    name="summarization",
    route_prefix="/summarization",
    autoscaling_config={
        "min_replicas": 1,
        "max_replicas": 3,
        "idle_timeout_s": 10,
    },
)
class SummarizationDeployment(Deployment):

    model_name = "t5-small"

    def __init__(self):
        """
        Initialize the model
        """
        print_debug("Initializing Summarization Model")
        self.load_model()
        print_debug("Summarization Model Initialized")

    def load_model(self):
        """
        Load the model
        """
        path_exists = False
        if os.path.exists(settings.SUMMARIZATION_MODEL_PATH):
            path_exists = True
            self.model_name = settings.SUMMARIZATION_MODEL_PATH
        self._model = pipeline("summarization", model=self.model_name)
        if not path_exists:
            self._model.save_pretrained(
                settings.SUMMARIZATION_MODEL_PATH
            )

    async def __call__(self, http_request):
        """
        Process the request and return the response
        """
        request = await http_request.json()
        text = request["text"]
        summary_list = self._model(
            text,
            min_length=5,
            max_length=15,
        )
        return summary_list

    def reconfigure(self, config):
        """
        Reconfigure the model
        """
        self.load_model()

    def shutdown(self):
        """
        Shutdown the model
        """
        self._model = None
