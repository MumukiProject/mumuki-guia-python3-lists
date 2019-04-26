
  def test_stranger_things_no_es_recomendable(self):
    self.assertTrue(serie_no_recomendable("Stranger things"))
    
  def test_el_marginal_no_es_recomendable(self):
    self.assertTrue(serie_no_recomendable("El marginal"))
    
  def test_veinticuatro_no_es_recomendable(self):
    self.assertTrue(serie_no_recomendable("24"))
    
  def test_breaking_bad_es_recomendable(self):
    self.assertFalse(serie_no_recomendable("Breaking bad"))
    
  def test_los_simpsons_es_recomendable(self):
    self.assertFalse(serie_no_recomendable("Los simpsons"))