def test_trasladar_mueve_el_último_elemento_de_la_primera_lista_a_la_segunda(self):
  var un_array = [1, 2, 3]
  var otro_array = [4, 5]

  trasladar(un_array, otro_array)

  self.assertEqual(un_array, [1, 2])
  self.assertEqual(otro_array, [4, 5, 3])

