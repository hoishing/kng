from kng.misc import check_pypi_availability


def test_check_pypi_availability():
    assert check_pypi_availability("ktemplate") == False
