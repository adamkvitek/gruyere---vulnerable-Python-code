from pyramid.authentication import AuthTktCookieHelper, AuthTktAuthenticationPolicy


### True positives ###


def bad1():
    # ruleid: pyramid-cookies
    authtkt = AuthTktCookieHelper(secret="test", httponly=False)

def bad2():
    # ruleid: pyramid-cookies
    authtkt = AuthTktCookieHelper(secret="test", httponly=False, name="a name")

def bad3():
    myBoolean = False
    # ruleid: pyramid-cookies
    authtkt = AuthTktCookieHelper(secret="test", httponly=myBoolean)


### True negatives ###

def good1():
    # ok: pyramid-cookies
    authtkt = AuthTktCookieHelper(secret="test", httponly=True)
