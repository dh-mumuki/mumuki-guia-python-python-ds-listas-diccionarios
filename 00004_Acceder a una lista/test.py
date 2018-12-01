class TestFixtures(unittest.TestCase):
  def test_numeros(self):
    self.assertEquals(numeros, [1, 2, 3, 4, 5])

  def test_numeros(self):
    self.assertEquals(letras, ["a", "b", "c", "d", "e"])

  def test_numeros(self):
    self.assertEquals(vocales, ["a",'e'])

  def test_numeros(self):
    self.assertEquals(pares, [2, 4])

  def test_numeros(self):
    self.assertEquals(primos, [1, 3, 5])

  def test_numeros(self):
    self.assertEquals(inverso,  ['e', 5, 'd', 4, 'c', 3, 'b', 2, 'a', 1])
