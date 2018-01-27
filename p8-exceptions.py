try:
    a = 4 / 0
except Exception as ex:
    print(str(ex))
finally:
    print('Thats all Folks')


