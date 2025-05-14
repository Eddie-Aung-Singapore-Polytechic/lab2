import lab2

def test_find_min_max():
    min_max = []
    list_to_feed = [69,33,2323,340,2,1000,354,5]
    min_max = lab2.find_min_max(list_to_feed)
    print(min_max)
    print(min_max[0],min_max[1])
    
    assert (min_max[0] == 2 and min_max[1] == 2323)
