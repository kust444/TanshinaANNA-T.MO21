g =(x  for x in [1, 2, 3, 4, 5, 6] if x > 2)

print(list(g))



def announce(hello):
    def wrapper():
        print("внимание!")
        return hello()
    return wrapper

@announce
def hello():
    print("Привет!")

hello()
