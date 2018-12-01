class TestFixtures(unittest.TestCase):
  def test_listas(self):
    self.assertEquals(sede_dh['barrios'].lower(), "vila olimpia")
    
  def test_listas(self):
    self.assertEquals(sede_dh['direccion'].lower(), "av. dr. cardoso de melo")

  def test_listas(self):
    self.assertEquals(sede_dh['lugar'].lower(), "digital house")

  def test_listas(self):
    self.assertEquals(sede_dh['pais'].lower(), "brasil")