import sys
def mutlak_deger(n):
    if n < 0:
        return 1
    elif n > 0:
        return n
    
def test(did_pass):
    """ Test sonuçlarını basar"""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = ("{0} satır testi OK.".format(linenum))
    else:
        msg = ("{0} satır testi BAŞARISIZ.".format(linenum))
    print(msg)
def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(mutlak_deger(17) == 17)
    test(mutlak_deger(-17) == 17)
    test(mutlak_deger(0) == 0)
    test(mutlak_deger(3.14) == 3.14)
    test(mutlak_deger(-3.14) == 3.14)

