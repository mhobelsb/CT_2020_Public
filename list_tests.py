def run_tests_obstkorb(a, b, c, d, e, f, g, h, i):
 
    # Unit tests to check your solution
    assert a == 16, 'a should be 10'
    assert b == 'apfel', ' b should be apfel'
    assert c == 'kirsche', 'c should be kirsche'
    assert d == ['birne', 'ananas', 'melone', 'apfel', 'birne'], '''d should be ['birne', 'ananas', 'melone', 'apfel', 'birne']'''
    assert e == ['apfel', 'orange', 'traube', 'birne'], '''e should be ['apfel', 'orange', 'traube', 'birne']'''
    assert f == ['orange', 'kokosnuss', 'apfel', 'kirsche'], '''f be ['orange', 'kokosnuss', 'apfel', 'kirsche']'''
    assert g == 4, 'g should be 4'
    assert h == 2, 'h size should be 2'
    assert i == ['ananas', 'apfel', 'apfel', 'apfel', 'apfel', 'birne', 'birne', 'birne', 'birne', 'kirsche', 'kokosnuss', 'melone', 'orange', 'orange', 'traube', 'traube'], '''i should be ['ananas', 'apfel', 'apfel', 'apfel', 'apfel', 'birne', 'birne', 'birne', 'birne', 'kirsche', 'kokosnuss', 'melone', 'orange', 'orange', 'traube', 'traube']'''
    
    print("Alle Aufgaben sind richtig!")
    
def run_tests_list(lst1, lst2, lst3, lst4, lst5):
    assert lst1 == [1, 1, 2, 3, 5, 8], r'lst1 should be [1, 1, 2, 3, 5, 8]'
    assert lst2 == [4, 6, 2, 4, 0, 3, 5, 1, 8], 'lst2 should be [4, 6, 2, 4, 0, 3, 5, 1, 8]'
    assert lst3 == [16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60], 'lst3 should be [16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60]'
    assert lst4 == [1, 5, 25, 71, 95, 4], 'lst4 should be [1, 5, 25, 71, 95, 4]'
    assert lst5 == [7, 7, 7, 14, 7, 7, 7], 'lst5 should be [7, 7, 7, 14, 7, 7, 7]'
    print("Alle Aufgaben sind richtig!")