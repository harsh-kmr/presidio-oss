from typing import Optional, List, Tuple

from presidio_analyzer import Pattern, PatternRecognizer


class InLicencePlateRecognizer(PatternRecognizer):
    """
    List from https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_India

    :param patterns: List of patterns to be used by this recognizer
    :param context: List of context words to increase confidence in detection
    :param supported_language: Language this recognizer supports
    :param supported_entity: The entity this recognizer can detect
    """

    
    PATTERNS = [
        Pattern(
            "Indian License Plate (High, Private and Commercial Vehicle License)",
            r"\b((?i:(AN|AP|AR|AS|BH|BR|CH|CG|DD|DL|GA|GJ|HR|HP|JK|JH|KA|KL|LA|LD|MP|MH|MN|ML|MZ|NL|OD|PY|PB|RJ|SK|TN|TS|TR|UP|UK|WB|UA|DN|OR))\d{2}|(\d{3}[a-hj-np-zA-HJ-NP-Z])\d{4})",
            0.8,
        ),
        Pattern(
            "Indian License Plate (low, Private and Commercial Vehicle License)",
            r"\b[A-Za-z]{2}[0-9]{1,2}[A-Za-z]{0,2}[0-9]{4}\b",
            0.3,
        ),
        Pattern(
            "Indian License Plate (high, Bharat series)",
            r"\b((?i)\d{2}BH\d{4}[A-HJ-NP-Z]{1,2})\b",
            0.8,
        ),
        Pattern(
            "Indian License Plate (high, Foreign mission)",
            r"\b((?:[0-9]|[1-9][0-9]|1[0-5][0-9]|160)(?:CD|CC|UN)\d{1,4})\b",
            0.8,
        ),
        Pattern(
            "Indian License Plate (high, Military)",
            r"\b([0-9]{2}[ABCDEFKPRX][0-9]{6}[A-Z])\b",
            0.8,
        ),
    ]

    CONTEXT = [
        "plate number",
        "vehicle no",
        "plate no",
        "license plate no",
        "registration number",
        "vehicle identification",
        "vehicle plate number",
        "number plate",
        "vehicle registration",
        "VRN",
        "registration plate",
        "vehicle license",
    ]

    replacement_pairs = [("-", ""), (" ", "")] 

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        context: Optional[List[str]] = None,
        supported_language: str = "en",
        supported_entity: str = "IN_LICENSE_PLATE",
        replacement_pairs: Optional[List[Tuple[str, str]]] = None,
    ):
        self.replacement_pairs = (
            replacement_pairs if replacement_pairs else [("-", ""), (" ", "")]
        )
        patterns = patterns if patterns else self.PATTERNS
        context = context if context else self.CONTEXT
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
