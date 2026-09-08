import click 
@click.command("hello")
def hello():
    click.echo("hello, I am working....")
commands=[hello]