class TestFixtures(unittest.TestCase):
  def test_lista_contenido(self):
    self.assertTrue(isinstance(numeros_escritos, (list)), 'el valor numeros_escritos no es una lista')
    self.assertEquals(numeros_escritos, ["uno", "dos", "tres"], 'La lista no tiene los elementos requeridos')