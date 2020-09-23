creds = {'log1': 'pass1', 'log': 'pass'}
def auth_required(some_func):
    pass

#@auth_required
def some_func(a, b):
    log_pass = tuple([a, b])
    if log_pass in creds.items():
        print('Authentication correct')
    else:
        print('Authentication required')


some_func(input('Login: '), input('Password: '))
