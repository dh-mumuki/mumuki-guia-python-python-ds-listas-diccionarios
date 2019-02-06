class TestFixtures(unittest.TestCase):
  def test_listas(self):
      self.assertEqual(lista, ['python', 43, 45.24, False, [2, 4, 5]], msg = 'Revisa si cumple con todas las condiciones.')