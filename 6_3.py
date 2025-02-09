def checher(var1):
    if type(var1) != str:
        raise TypeError(f"Ми не можемо працювати з таким типом даних - {type(var1)}. Треба тип - str!")
    else:
        return var1


my_var = 10
my_var2 = "Vasya"
checher(my_var)
checher(my_var2)