from prova4a import *

import unittest



class TestQuartaProva(unittest.TestCase):


    def test_turma(self):
        self.assertEqual(turma(1, ([(1, 1), (1, 2), (1, 3), (2, 1), (2, 4)])), 3)


    def test_alunos_turma(self):
        self.assertEqual(alunos_por_turma(3, ([(1, 1), (1, 2), (1, 3), (2, 1), (2, 4)])), [[1]])

    def test_turma_maior(self):
        self.assertEqual(turma_maior([(1, 1), (1, 2), (1, 3), (2, 1), (2, 4)]), 1)

    def test_alunos_matriculados(self):
        self.assertEqual(alunos_matriculados(1, ([(1, 1), (1, 2), (1, 3), (2, 1), (2, 4)])), [[1], [2], [3]])