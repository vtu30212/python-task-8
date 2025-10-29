def squares():
    for i in range(5):
        yield i ** 2

squares_generator = squares()
for square in squares_generator:
    print(square)
