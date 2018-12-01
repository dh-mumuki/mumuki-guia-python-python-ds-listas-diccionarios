class TestFixtures(unittest.TestCase):
  def test_listas(self):
    self.assertEquals(yo.keys(), ['nombre', 'apellido', 'mail'])