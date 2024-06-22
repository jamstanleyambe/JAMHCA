import fire

class MyScript:
    def greet(self, name):
        return f"Hello, {name}!"

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

if __name__ == '__main__':
    fire.Fire(MyScript)