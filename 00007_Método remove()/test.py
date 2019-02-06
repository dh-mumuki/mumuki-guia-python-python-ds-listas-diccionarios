class TestFixtures(unittest.TestCase):
  def test_listas(self):
    self.assertTrue(len(lista)==4, 'Falta o sobra algun elemento de la lista.')
    self.assertFalse("torta" in lista, 'El elemento torta sigue en la lista.')