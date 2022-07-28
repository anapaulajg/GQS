from MockDB import MockBD
import sys
sys.path.insert(0, '..')
from conexaoDB import *
from queries import *
class TestDB(MockBD):

#1. Listar o nome de todas as turmas que a aluna 'Carla' está matriculada     
     def test_filtro_nome_(self):
          retorno_esperado =  [('Carla', 'unidade 4' , 'Geografia'),
                              ('Carla',	'unidade 2', 'Geografia'),
                              ('Carla',	'unidade 3','Sociologia')]
          self.assertEqual(ler_por_alunos_por_curso(self.mock_db_config.get('bd'), 'Carla'), 
          retorno_esperado)

     def test_filtro_nome_(self):
          retorno_esperado =  [('Marcos','unidade 3', 'Sociologia')
                             ]
          self.assertEqual(ler_por_alunos_por_curso(self.mock_db_config.get('bd'), 'Marcos'), 
          retorno_esperado)

     def test_filtro_nome_(self):
          retorno_esperado =  [('Luiza', 'unidade 3', 'Sociologia')]
          self.assertEqual(ler_por_alunos_por_curso(self.mock_db_config.get('bd'), 'Luiza'), 
          retorno_esperado)



#2. Listar todos os alunos da escola          
     def test_select_all_matriculados(self):

          retorno_esperado = [('Maria',	'unidade 4','Geografia'),
                              ('Marcos','unidade 3',	'Sociologia'),
                              ('Carol','unidade 1',	'Inglês'),
                              ('Rafaela','unidade 3',	'Sociologia'),
                              ('Luiza','unidade 3',	'Sociologia'),
                              ('Raiane','unidade 1',	'Inglês'),
                              ('Carla',	'unidade 4',	'Geografia'),
                              ('Rafaela','unidade 2',	'Geografia'),
                              ('Maria','unidade 1','Inglês'),
                              ('Erico',	'unidade 1',	'Inglês'),
                              ('Carla',	'unidade 2',	'Geografia'),
                              ('Carla',	'unidade 3',	'Sociologia'),
                              ('Maria','unidade 3','Sociologia'),
                              ('Erico', 'unidade 3',	'Sociologia'),
                              ('Rafaela', 'unidade 4',	'Geografia'),
                              ('Rafaela','unidade 1',	'Inglês'),
                              ('Carol','unidade 3',	'Sociologia')]
          self.assertEqual(ler_todos_alunos_por_curso(self.mock_db_config.get('bd')),
     retorno_esperado)



#3. Listar todas as turmas da disciplina 'Geografia'
     def test_filtro_turmas_curso(self):
          retorno_esperado =  [('Geografia', 'unidade 2'),
                              ('Geografia', 'unidade 4')]
          self.assertEqual(ler_por_turmas_por_curso(self.mock_db_config.get('bd'), 'Geografia'), 
          retorno_esperado)

#4. Listar todas as turmas da disciplina 'Geografia'
     def test_filtro_turmas_curso(self):
          retorno_esperado =  [('Maria',	'unidade 4','Geografia'),
                              ('Carla',	'unidade 4','Geografia'),
                              ('Rafaela','unidade 2','Geografia'),
                              ('Carla',	'unidade 2','Geografia'),
                              ('Rafaela','unidade 4','Geografia')]
          self.assertEqual(ler_por_turmas_por_curso(self.mock_db_config.get('bd'), 'Geografia'), 
          retorno_esperado)
          
          
     def test_select_all(self):

          retorno_esperado = [(1, 'Quimica'),
                              (2, 'Sociologia'),
                              (3, 'Inglês'),
                              (4, 'Geografia')]
          self.assertEqual(ler_todas_Disciplinas(self.mock_db_config.get('bd')),
     retorno_esperado)
          