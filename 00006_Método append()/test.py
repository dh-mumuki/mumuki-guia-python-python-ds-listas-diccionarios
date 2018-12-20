class TestFixtures(unittest.TestCase):
  def test_listas(self):
    try:
      self.assertEqual(lista, ['python', 43, 45.24, False, [2, 4, 5]], msg = 'Revisá si cumple con todas la condiciones!')
    except AssertionError as e:
      print(e)