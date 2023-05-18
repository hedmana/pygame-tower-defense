import unittest, os, csv

from test_map import TestMap

### UNIT TESTS FOR MAP CREATION AND PATH FINDING ###
class TestStringMethods(unittest.TestCase):
    
    # Tests the path finding algorithm 
    def test_get_nodes(self):   
        test_map = TestMap()     
        correct_nodes = [[50, 450], [150, 450], [250, 450], [350, 450], 
                         [450, 450], [550, 450], [650, 450], [750, 450], 
                         [850, 450], [950, 450], [1050, 450], [1150, 450]]
        test_nodes = test_map.get_nodes()
        self.assertEqual(correct_nodes, test_nodes)
        
    def test_read_default_map(self):
        test_map = TestMap()
        test_map.read_default_map()
        
        map_chars = []
        correct_chars = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], 
                         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], 
                         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], 
                         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], 
                         ['S', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', 'E'], 
                         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], 
                         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], 
                         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]
        
        with open(os.path.join('testing/test_map.csv')) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                temp_row = []
                for i in row:
                    temp_row.append(i)
                map_chars.append(temp_row)

        self.assertEqual(map_chars, correct_chars)
        
    
if __name__ == '__main__':
    unittest.main()