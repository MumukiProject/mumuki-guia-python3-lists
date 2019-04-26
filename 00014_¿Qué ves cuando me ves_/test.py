
  def stranger_things_no_es_una_serie_recomendable(self):
    self.assertTrue(serie_no_recomendable("Stranger things"))
    
  def el_marginal_no_es_una_serie_recomendable(self):
    self.assertTrue(serie_no_recomendable("El marginal"))
    
  def veinticuatro_no_es_una_serie_recomendable(self):
    self.assertTrue(serie_no_recomendable("24"))
    
  def breaking_bad_es_una_serie_recomendable(self):
    self.assertFalse(serie_no_recomendable("Breaking bad"))
    
  def los_simpsons_es_una_serie_recomendable(self):
    self.assertFalse(serie_no_recomendable("Los simpsons"))