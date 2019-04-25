  
  def test_la_lista_1_6_7_6_contiene_al_7(self):
    self.assertTrue(contiene([1, 6, 7, 6], 7))

  def test_la_lista_1_6_7_6_contiene_al_6(self):
    self.assertTrue(contiene([1, 6, 7, 6], 6))

  def test_la_lista_vacia_no_contiene_al_7(self):
    self.assertFalse(contiene([], 7))

  def test_la_lista_8_5_no_contiene_al_7(self):
    self.assertFalse(contiene([8, 5], 7))

  def test_la_lista_1_8_5_no_contiene_al_7(self):
    self.assertFalse(contiene([1, 8, 5], 7))

  def test_la_lista_1_1_1_contiene_al_1(self):
    self.assertTrue(contiene([1, 1, 1], 1))

