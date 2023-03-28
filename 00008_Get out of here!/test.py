  
  def test_transfer_3_from_the_first_list_to_the_second(self):
    a_list = [1, 2, 3]
    another_list = [4, 5]
  
    transfer(a_list, another_list, 3)
  
    self.assertEqual(a_list, [1, 2])
    self.assertEqual(another_list, [4, 5, 3])
  
  def test_transfer_8_from_the_first_list_to_the_second(self):
    a_list = [9, 8, 7]
    another_list = [4, 5]
  
    transfer(a_list, another_list, 8)
  
    self.assertEqual(a_list, [9, 7])
    self.assertEqual(another_list, [4, 5, 8])
  
