class TestFixtures(unittest.TestCase):
  def test_listas_barrio(self):
    self.assertTrue("vila" in sede_dh['barrio'].lower(), 'Barrio no especifica vila')
    
  def test_listas_direccion(self):
    self.assertTrue("cardoso" in sede_dh['direccion'].lower(), 'Cardoso de melo no se encuentra en direccion')
    self.assertTrue("de" in sede_dh['direccion'].lower(), 'Cardoso de melo no se encuentra en direccion')
    self.assertTrue("melo" in sede_dh['direccion'].lower(), 'Cardoso de melo no se encuentra en direccion')

  def test_listas_lugar(self):
    self.assertTrue("digital" in sede_dh['lugar'].lower(), 'digital house no se encuentra en lugar')
    self.assertTrue("house" in sede_dh['lugar'].lower(),'digital house no se encuentra en lugar')
    

  def test_listas_pais(self):
    self.assertTrue("brasil" in sede_dh['pais'].lower(), 'Brasil no se encuentra en pais')