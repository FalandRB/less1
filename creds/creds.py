creds = {'log1': 'pass1', 'log': 'pass'}
def auth_required(some_func):
    def wrapper_decorator(*args, **kwargs):
        value = some_func(*args, **kwargs)
        if args in creds.items():
            print('Authentication correct')
        else:
            print('Authentication required')
        # Do something after
        return value
    return wrapper_decorator

@auth_required
def some_func(a, b):
    print(f'Hello {a}')

some_func(input('Login: '), input('Password: '))
