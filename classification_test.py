import unittest
from typing import List, Any

import read, copy
from logical_classes import *
from function import KnowledgeBase


class KBTest(unittest.TestCase):

    def setUp(self):
        # Assert starter facts
        file = 'statements.txt'
        self.data = read.read_tokenize(file)
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact) or isinstance(item, Rule):
                self.KB.kb_assert(item)

    def test_i(self):
        ask1 = read.parse_input("fact: (classification setosa)")
        print('Calculating', ask1)
        answer = self.KB.kb_ask(ask1)

    def test_o(self):
        ask1 = read.parse_input("fact: (classification versicolour)")
        print('Calculating', ask1)
        answer = self.KB.kb_ask(ask1)

    def test_u(self):
        ask1 = read.parse_input("fact: (classification virginica)")
        print('Calculating', ask1)
        answer = self.KB.kb_ask(ask1)

    def test_za(self):
        ask1 = read.parse_input("fact: (classification all)")
        print('Calculating', ask1)
        answer = self.KB.kb_ask(ask1)


if __name__ == '__main__':
    unittest.main()
