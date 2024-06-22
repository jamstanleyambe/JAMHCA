import click

@click.command()
@click.argument('name')
def greet(name):
    if not name.lower().startswith('p'):
        print(name)

if __name__ == '__main__':
    greet()