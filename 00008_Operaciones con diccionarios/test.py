class TestFixtures(unittest.TestCase):
  def test_listas_barrio(self):
    self.assertTrue("vila" in sede_dh['barrios'].lower())
    
  def test_listas_direccion(self):
    self.assertTrue("cardoso" in sede_dh['direccion'].lower())
    self.assertTrue("de" in sede_dh['direccion'].lower())
    self.assertTrue("melo" in sede_dh['direccion'].lower())

  def test_listas_lugar(self):
    self.assertTrue("digital" in sede_dh['lugar'].lower())
    self.assertTrue("house" in sede_dh['lugar'].lower())
    

  def test_listas_pais(self):
    self.assertTrue("brasil" in sede_dh['pais'].lower())