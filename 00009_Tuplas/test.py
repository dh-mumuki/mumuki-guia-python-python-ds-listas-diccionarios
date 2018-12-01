class TestFixtures(unittest.TestCase):
  def test_listas(self):
    self.assertEquals(verduras[1].lower(), "tomate")

  def test_listas(self):
    self.assertEquals(len(verduras), 5)    
