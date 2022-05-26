import pytest
from file import check_document_existance, get_doc_owner_name, add_new_shelf


class TestMain:

    def setup(self):
        pass

    def teardown(self):
        pass

    @pytest.mark.parametrize(
        'number, expected_res',
        [
            ("2207 876234", True),
            ("11-2", True),
            ("10006", True),
            ("561", False)
        ]
    )
    def test_check_document_existance(self, number, expected_res):
        actual_res = check_document_existance(number)
        assert actual_res == expected_res

    @pytest.mark.parametrize(
        'number, expected_res',
        [
            ("2207 876234", "Василий Гупкин"),
            ("11-2", "Геннадий Покемонов"),
            ("10006", "Аристарх Павлов"),
            ("564", None)
        ]
    )
    def test_get_doc_owner_name(self, number, expected_res):
        actual_res = get_doc_owner_name(number)
        assert actual_res == expected_res

    @pytest.mark.parametrize(
        'shelf, expected_res',
        [
            ('3', ('3', False)),
            ('4', ('4', True)),
            ('5', ('5', True))
        ]
    )
    def test_add_new_shelf(self, shelf, expected_res):
        actual_res = add_new_shelf(shelf)
        assert actual_res == expected_res