def  my_gen():
    yield 1
    yield 2
    yield 3
#yield can return multiple values

gen=my_gen()
gen


next(gen)

1st ex- 1
2nd ex -2
3rd ex -3
4th ex- error



