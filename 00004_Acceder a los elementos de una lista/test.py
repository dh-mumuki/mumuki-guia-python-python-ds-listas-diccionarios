class TestFixtures(unittest.TestCase):
  def test_numeros(self):
    self.assertEquals(numeros, [1, 2, 3, 4, 5], 'El contenido en la lista numeros, no son correctos.')

  def test_letras(self):
    self.assertEquals(letras, ["a", "b", "c", "d", "e"], 'El contenido en la lista letras, no es correcto, deben ser letras de la "a" hasta la "e"')

  def test_vocales(self):
    self.assertEquals(vocales, ["a",'e'])

  def test_pares(self):
    self.assertEquals(pares, [2, 4])

  def test_primos(self):
    self.assertEquals(primos, [1, 3, 5])

  def test_inversa(self):
    self.assertEquals(inverso,  ['e', 5, 'd', 4, 'c', 3, 'b', 2, 'a', 1])
