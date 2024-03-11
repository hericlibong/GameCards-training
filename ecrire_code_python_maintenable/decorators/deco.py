def mon_decorateur(func):
    def wrapper(*args, **kwargs):
        print(f"Début de la fonction {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Fin de la fonction {func.__name__}")
        return result
    return wrapper



@mon_decorateur
def hello_world():
    print('Hello world!!')

hello_world()

import time

def mesurer_temps(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} a pris {end_time - start_time} secondes à s'exécuter ")
        return result
    return wrapper

@mesurer_temps
def calcul_long(n):
    time.sleep(n)
    
calcul_long(1)

def modifier_arguments(factor):
    def decorateur(func):
        def wrapper(*args, **kwargs):
            args_modifies = [a * factor for a in args]
            return func(*args_modifies, **kwargs)
        return wrapper
    return decorateur

@modifier_arguments(2)
def addition(a, b):
    return a + b


print(addition(3, 2))

