
  def test_stranger_things_is_not_recommendable(self):
    self.assertTrue(not_recommendable("Stranger things"))
    
  def test_el_marginal_is_not_recommendable(self):
    self.assertTrue(not_recommendable("El marginal"))
    
  def test_twenty_four_is_not_recommendable(self):
    self.assertTrue(not_recommendable("24"))
    
  def test_breaking_bad_is_recommendable(self):
    self.assertFalse(not_recommendable("Breaking bad"))
    
  def test_the_simpsons_is_recommendable(self):
    self.assertFalse(not_recommendable("The Simpsons"))