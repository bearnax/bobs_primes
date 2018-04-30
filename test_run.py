import run


def test_cube_of_three():
    test_cube = run.cube_integer(3)
    assert test_cube == 27

def test_cube_difference():
    difference = run.diff_of_two_integers(5, 10)
    assert difference == 5

def test_pair_generator_type():
    number_pair_object = run.pair_generator(1)
    assert type(number_pair_object) == tuple

def test_pair_generator():
    paired_numbers = run.pair_generator(22)
    assert paired_numbers[0] == 22
    assert paired_numbers[1] == 23

def test_isPrime():
    assert run.isPrime(12) == False
    assert run.isPrime(3) == True
    assert run.isPrime(1009) == True
    assert run.isPrime(6211) == True

def test_check_pair_differnce_prime():
    assert run.check_pair_differnce_prime(3) == True
