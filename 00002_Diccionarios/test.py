class TestFixtures(unittest.TestCase):
  def test_keys(self):
    self.assertEquals(yo.keys(), ['nombre', 'apellido', 'mail'], 'Faltan claves en el diccionario.')
  def test_values(self):
    self.assertAlmostEqual(len([yo[x] for x in yo if yo[x]!=None]), 3, 'Faltan valores para alguna/s clave/s')