# function to return the factorial of a number
# Add comments
import unittest

def factorial(num):
    ans = 1
    if num < 0:
        return None
    elif num < 2:
        return ans
    else:
        for i in range(1, num + 1):
            ans = ans * i
        return ans


# function to check if the input year is a leap year or not
def check_leap_year(year):
    isLeap = False
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                isLeap = True
        else:
            isLeap = True
    return isLeap

print("factorial(0): {}".format(factorial(0)))
print("factorial(1): {}".format(factorial(1)))
print("factorial(5): {}".format(factorial(5)))
print("factorial(-5): {}".format(factorial(-5)))

print("check_leap_year(2000): {}".format(check_leap_year(2000)))
print("check_leap_year(1990): {}".format(check_leap_year(1990)))
print("check_leap_year(2012): {}".format(check_leap_year(2012)))
print("check_leap_year(2100): {}".format(check_leap_year(2100)))

print("Starting Tests Here")

class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(factorial(0), 1)
    def test2(self):
        self.assertEqual(factorial(1), 1)
    def test3(self):
        self.assertEqual(factorial(-5), None)
    def test4(self):
        self.assertEqual(factorial(5), 120)
    def test5(self):
        self.assertEqual(check_leap_year(1900), False)
    def test6(self):
        self.assertEqual(check_leap_year(1912), True)
    def test7(self):
        self.assertEqual(check_leap_year(2000), True)



unittest.main(verbosity=2) 