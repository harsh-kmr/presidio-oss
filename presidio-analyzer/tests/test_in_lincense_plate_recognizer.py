import pytest

from tests import assert_result
from presidio_analyzer.predefined_recognizers import InLicencePlateRecognizer


@pytest.fixture(scope="module")
def recognizer():
    return InLicencePlateRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["IN_LICENSE_PLATE"]


@pytest.mark.parametrize(
    "text, expected_len, expected_position, expected_score",
    [
        # fmt: off
        ("UP19D0343", 1, (0,9), 0.8) ,
        ("hk19D0343", 1, (0,9), 0.3) ,
        ("199CD1", 1, (0, 8), 0.8),
        ("21BH2345 AA", 1, (0, 11),0.8),
        ("ABCD1234",0,(),(),),
        ("02B084821H",0,(),(),),
        ("My number plate is UP19D0343 with a lot of text beyond it", 1, (17,27),.8),
        # fmt: on
    ],
)
def test_when_in_vehicle_plate_in_text_then_all_in_vehicle_plate_found(
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
