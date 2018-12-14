class TestFixtures(unittest.TestCase):
  def test_tomate(self):
    self.assertEquals(verduras[1].lower(), "tomate")

  def test_tamano(self):
    self.assertEquals(len(verduras), 5)
  
  def test_tupla(self):
    assertIsInstance(verduras, tuple)
