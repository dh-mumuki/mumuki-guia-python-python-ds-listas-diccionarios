class TestFixtures(unittest.TestCase):
  def test_tomate(self):
    self.assertEquals(verduras[1].lower(), "tomate", "El segundo elemento no es tomate")

  def test_tamano(self):
    self.assertEquals(len(verduras), 5, "El contenedor no tiene 5 elementos")
  
  def test_tupla(self):
    self.assertIsInstance(verduras, tuple, "El elemento no es una tupla")
