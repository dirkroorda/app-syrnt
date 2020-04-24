from os.path import dirname, abspath

API_VERSION = 1

PROVENANCE_SPEC = dict(
    org="etcbc",
    repo="syrnt",
    version="0.1",
    doi="10.5281/zenodo.1464787",
    corpus="SyrNT",
    webBase="{ghUrl}/{org}/{repo}/blob/master/plain/",
    webUrl="{version}/<1>.txt",
    webHint="show this passage in the SyrNT repository",
)

DOCS = dict(
    docPage="transcription",
    featureBase="{docBase}/transcription-{version}{docExt}",
    featurePage="",
)

DATA_DISPLAY = dict(noneValues={None, "NA", "none", "unknown"}, writing="syc")

TYPE_DISPLAY = dict(
    lexeme=dict(template="{lexeme}", lexOcc="word"),
    word=dict(featuresBare="sp", features="vs vt"),
)

INTERFACE_DEFAULTS = dict()


def deliver():
    return (globals(), dirname(abspath(__file__)))
