  
  def test_medal_for_1(self):
    self.assertEqual(medal_for(1), "gold")

  def test_medal_for_2(self):
    self.assertEqual(medal_for(2), "silver")

  def test_medal_for_3(self):
    self.assertEqual(medal_for(3), "bronze")

  def test_medal_for_4(self):
    self.assertEqual(medal_for(4), "nothing")

  def test_medal_for_5(self):
    self.assertEqual(medal_for(5), "nothing")

  def test_medal_for_15(self):
    self.assertEqual(medal_for(15), "nothing")

  def test_medal_for_83(self):
    self.assertEqual(medal_for(83), "nothing")
    
  def test_medals_are_not_shifted(self):
    try: 
      results = [
        medal_for(1),
        medal_for(2),
      ]
    except Exception:
      results = None
    
    self.assertTrue(
      results != ["silver", "bronze"], 
      "It looks like all your medals are shifted")    

