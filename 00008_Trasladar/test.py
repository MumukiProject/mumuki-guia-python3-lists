  
  def test_trasladar_mueve_el_3_de_la_primera_lista_a_la_segunda(self):
    un_array = [1, 2, 3]
    otro_array = [4, 5]
  
    trasladar(un_array, otro_array, 3)
  
    self.assertEqual(un_array, [1, 2])
    self.assertEqual(otro_array, [4, 5, 3])
  
  def test_trasladar_mueve_el_8_de_la_primera_lista_a_la_segunda(self):
    un_array = [9, 8, 7]
    otro_array = [4, 5]
  
    trasladar(un_array, otro_array, 7)
  
    self.assertEqual(un_array, [9, 8])
    self.assertEqual(otro_array, [4, 5, 7])
  
