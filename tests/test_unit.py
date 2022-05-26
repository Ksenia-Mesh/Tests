import unittest
from parameterized import parameterized
from file import check_document_existance, get_doc_owner_name, add_new_shelf


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        print("Вызвали метод ==> setUp")

    def tearDown(self) -> None:
        print("Вызвали метод ==> tearDown")

    @parameterized.expand([
        ["2207 876234", True],
        ["11-2", True],
        ["10006", True],
        ["561", False]
    ])

    def test_check_document_existance(self, input_, result):
        self.assertEqual(check_document_existance(input_), result)

    @parameterized.expand([
            ["2207 876234", "Василий Гупкин"],
            ["11-2", "Геннадий Покемонов"],
            ["10006", "Аристарх Павлов"],
            ["564", None]
        ])

    def test_get_doc_owner_name(self, input_, result):
        self.assertEqual(get_doc_owner_name(input_), result)

    @parameterized.expand([
        ['3', ('3', False)],
        ['4', ('4', True)],
        ['5', ('5', True)]
        ]
    )
    def test_add_new_shelf(self, input_, result):
        self.assertEqual(add_new_shelf(input_), result)