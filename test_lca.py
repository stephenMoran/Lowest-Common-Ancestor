import area

def test_area():
    totalArea = area.find_area()
    print(totalArea)
    assert totalArea == 17.320508075688775
