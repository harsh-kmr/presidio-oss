import pytest

from tests import assert_result
from presidio_analyzer.predefined_recognizers import CoordinateRecognizer


@pytest.fixture(scope="module")
def recognizer():
    return CoordinateRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["coordinate"]


@pytest.mark.parametrize(
    "text, expected_len, expected_position, expected_score",
    [
        # fmt: off
        ("12.345° N, 67.890° W", 1, (0,20), 0.85) ,
        ("100.123, -200.456", 0, (), ()) , # check again 
        ("40.7128°N, -74.0060°W", 1, (0, 21), 0.85),
        ("1000.345°X, 200.567°Y",  0, (), ()),
        ("12°34'56.789\"N, 98°12'34.567\"E", 1, (0, 30),0.4), # check again
        ("91°45'30\"N, 190°23'15\"E", 1, (0, 23),0.4),
        ("12.345° N, 67.890° W represents a location on the globe, and it's situated approximately 1 degree north and 67.89 degrees west.", 1, (0, 20), 0.85),
        ("1000.345°X, 200.567°Y does not adhere to the standard coordinate format and cannot be accurately interpreted.", 0, (), ()),
        # fmt: on
    ],
)
def test_when_in_coordinate_in_text_then_all_in_coordinate_found(
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
