from compare.functions import score_by_weights
from tests.utils.helpers import *

def test_score_by_weights():
    payload, weights, expected_result = get_typical_payload_with_weights_and_score_comparison_result()
    result = score_by_weights(payload, weights)
    assert result == expected_result, "Should be a list of components sorted in descending order by score"