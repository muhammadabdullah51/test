def greetings(user):
    return f'hello {user}'
def hello():
    return 'this is the hello fn'

def bio(usssr) -> str:
    res1 = greetings(usssr)
    res2 = hello()
    print(res1)
    print(res2)
    return int(545)