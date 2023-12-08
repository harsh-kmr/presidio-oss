import pytest

from tests import assert_result
from presidio_analyzer.predefined_recognizers import MACAddressRecognizer


@pytest.fixture(scope="module")
def recognizer():
    return MACAddressRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["MAC_address"]


@pytest.mark.parametrize(
    "text, expected_len, expected_position, expected_score",
    [
        # fmt: off
        ("1A2b3C4d5E6f", 1, (0,11), 0.8) ,
        ("1A2b3C4d5E6fg", 1, (17,27),0.1),
        ("1A2b3C4d5E6f", 0, (),()),
        ("This is a valid MAC address: 1A2b3C4d5E6f with lot of text behind it", 1, (17,27),0.8),
        # fmt: on
    ],
)
def test_when_mac_address_in_text_then_all_mac_address_found(
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
