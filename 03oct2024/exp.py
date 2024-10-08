from inherit import Animal, Person, Vehicle


try:
    let = 10
    print(let)

    vhl = Vehicle('car')
    per = Person('abdullah')
    anm = Animal('penguine')

    print(vhl.food())
    print(per.food())
    print(anm.food())
except Exception as e:
    print("Exception is ", e)
finally: 
    print("This will be printed always")