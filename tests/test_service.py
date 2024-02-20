import pytest
import irsut.service as service
import unittest.mock as mock

@mock.patch("source.service.get_user_from_db")
def test_get_user_fom_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"