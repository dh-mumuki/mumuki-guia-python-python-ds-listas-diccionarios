class TestFixtures(unittest.TestCase):
  def test_numeros(self):
    self.assertEquals(numeros, [1, 2, 3, 4, 5], 'El contenido en la lista numeros, no son correctos.')

  def test_letras(self):
    self.assertEquals(letras, ["a", "b", "c", "d", "e"], 'El contenido en la lista letras, no es correcto, deben ser letras de la "a" hasta la "e"')

  def test_vocales(self):
    self.assertEquals(vocales, ["a",'e'], 'El contenido de las lista vocales no es correcto')

  def test_pares(self):
    self.assertEquals(pares, [2, 4], 'El contenido de la lista pares, no es correcto')

  def test_inversa(self):
    self.assertEquals(inverso,  ['e', 5, 'd', 4, 'c', 3, 'b', 2, 'a', 1], 'El contenido de la lista inverso, debe ser el mismo contenido de la lista original pero empezando por el final hasta el comienzo.')
