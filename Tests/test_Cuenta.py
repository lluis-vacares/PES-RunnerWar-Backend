from unittest import TestCase
from src import Cuenta


class Test(TestCase):
    def test_already_created(self):
        assert (Cuenta.create("unit_test1", "utest1", "this_is_a_test", "red")) == {"_id": None,
                                                                                    "password": None,
                                                                                    "accountname": None,
                                                                                    "coins": None,
                                                                                    "points": None,
                                                                                    "faction": None,
                                                                                    "codi": 500}

    def test_create(self):
        assert (Cuenta.create("unit_test1", "utest1", "this_is_a_test", "red")) == {"_id": "unit_test1",
                                                                                    "password": "this_is_a_test",
                                                                                    "accountname": "utest1",
                                                                                    "coins": 0,
                                                                                    "points": 0,
                                                                                    "faction": "red",
                                                                                    "codi": 200}
        # Remember to delete the collection created from the database once this test is done :)

    # To run these following tests, make sure that "unit_test1" account is created in DB (simply run test_create)
    def test_login(self):
        assert (Cuenta.login("unit_test1", "this_is_a_test")) == {"_id": "unit_test1",
                                                                  "password": "this_is_a_test",
                                                                  "accountname": "utest1",
                                                                  "coins": 0,
                                                                  "points": 0,
                                                                  "faction": "red",
                                                                  "codi": 200}

    def test_login_failed(self):
        assert (Cuenta.login("unit_test2", "this_should_fail")) == {"_id": None,
                                                                    "password": None,
                                                                    "accountname": None,
                                                                    "coins": None,
                                                                    "points": None,
                                                                    "faction": None,
                                                                    "codi": 500}

    def test_update_password(self):
        assert (Cuenta.update("password", "this_is_a_test_2", "unit_test1")) == {"_id": "unit_test1",
                                                                                 "password": "this_is_a_test_2",
                                                                                 "accountname": "utest1",
                                                                                 "coins": 0,
                                                                                 "points": 0,
                                                                                 "faction": "red",
                                                                                 "codi": 200}

    # To run the following test, make sure that test_update_password is executed before
    # (simply run test_update_password)
    def test_update_accountname(self):
        assert (Cuenta.update("accountname", "utest2", "unit_test1")) == {"_id": "unit_test1",
                                                                          "password": "this_is_a_test_2",
                                                                          "accountname": "utest2",
                                                                          "coins": 0,
                                                                          "points": 0,
                                                                          "faction": "red",
                                                                          "codi": 200}

    # To run the following test, make sure that test_update_accountname is executed before
    # (simply run test_update_accountname)
    def test_update_faction(self):
        assert (Cuenta.update("faction", "blue", "unit_test1")) == {"_id": "unit_test1",
                                                                    "password": "this_is_a_test_2",
                                                                    "accountname": "utest2",
                                                                    "coins": 0,
                                                                    "points": 0,
                                                                    "faction": "blue",
                                                                    "codi": 200}

    def test_delete(self):
        assert (Cuenta.delete("unit_test1")) == {"codi": 200}
