import pytest

from tests import assert_result
from presidio_analyzer.predefined_recognizers import BloodGroupRecognizer


@pytest.fixture(scope="module")
def recognizer():
    return BloodGroupRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["BLOOD_GROUPS"]


@pytest.mark.parametrize(
    "text, expected_len, expected_position, expected_score",
    [
        # fmt: off
        ("AB+", 1, (0,11), 0.2) ,
        ("My blood group is O+ with a lot of text beyond it", 1, (17,27),0.2),
        # fmt: on
    ],
)
def test_when_blood_group_in_text_then_all_blood_group_found(
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
