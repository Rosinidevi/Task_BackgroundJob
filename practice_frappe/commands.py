import click 
@click.command("hello-app")
def hello():
    click.echo("hello, I am working....")
commands=[hello]