import pytest

from tests import assert_result
from presidio_analyzer.predefined_recognizers import InAadhaarRecognizer


@pytest.fixture(scope="module")
def recognizer():
    return InAadhaarRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["IN_AADHAAR"]


@pytest.mark.parametrize(
    "text, expected_len, expected_position, expected_score",
    [
        # fmt: off
        ("2222222222", 1, (0,11), 0.8) ,
        ("123456789012", 1, (0, 11), 0.8),
        ("012345678901", 1, (0, 11), 0.6),
        ("01234567890", 0, (),()),
        ("ABCD1234",0,(),(),),
        ("My Aadhaar number is 123456789012 with a lot of text beyond it", 1, (17,27),.8),
        # fmt: on
    ],
)
def test_when_aadhaar_in_text_then_all_aadhaar_found(
    text,
    expected_len,
    expected_position,
    expected_score,
    recognizer,
    entities,
):
    results = recognizer.analyze(text, entities)
    print(results)

    assert len(results) == expected_len
    if results:
        assert_result(
            results[0],
            entities[0],
            expected_position[0],
            expected_position[1],
            expected_score,
        )
