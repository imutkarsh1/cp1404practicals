from guitar import Guitar

# Test cases
def test_get_age():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1200.00)

    assert guitar1.get_age() == 100, f"Expected 100. Got {guitar1.get_age()}"
    assert guitar2.get_age() == 9, f"Expected 9. Got {guitar2.get_age()}"

def test_is_vintage():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1200.00)

    assert guitar1.is_vintage() == True, f"Expected True. Got {guitar1.is_vintage()}"
    assert guitar2.is_vintage() == False, f"Expected False. Got {guitar2.is_vintage()}"

# Run the tests
test_get_age()
test_is_vintage()
