from overrides import overrides

from allennlp.common.util import JsonDict
from allennlp.data import Instance
from allennlp.service.predictors.predictor import Predictor


@Predictor.register('sequence_classifier')
class SequenceClassifierPredictor(Predictor):
    """
    Wrapper for the :class:`~allennlp.models.SequenceClassifier` model.
    """
    @overrides
    def _json_to_instance(self, json: JsonDict) -> Instance:
        """
        Expects JSON that looks like ``{"reviewText": "..."}``.
        """
        input_text = json["reviewText"]
        return self._dataset_reader.text_to_instance(input_text)
