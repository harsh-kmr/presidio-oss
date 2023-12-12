import pytest

from tests import assert_result
from presidio_analyzer.predefined_recognizers import InDriverLicenceRecognizer


@pytest.fixture(scope="module")
def recognizer():
    return InDriverLicenceRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["IN_DRIVING_LICENSE"]


@pytest.mark.parametrize(
    "text, expected_len, expected_position, expected_score",
    [
        # fmt: off
        ("MH1420110062821", 1, (0,15), 0.8) ,
        ("AB1256789012345", 1, (0, 15),0.3),
        ("I finally got my hands on my new driving license, and it's got the code AB1256789012345.", 1, (72,87),0.3),
        # fmt: on
    ],
)
def test_when_driver_licence_in_text_then_all_driver_licence_found(
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
