class TestFixtures(unittest.TestCase):
  def test_listas(self):
    self.assertEquals(sede_dh, {"barrio": "Vila Olimpia", 'direccion': 'Av. Dr. Cardoso de Melos', 'lugar': "Digital House"})