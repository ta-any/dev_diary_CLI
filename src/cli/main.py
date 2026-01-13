# Инициализирует DevDiaryManager при запуске

import click
@click.group()
def cli(): pass

@cli.command()
@click.argument('text')
@click.option('--duration', '-d', type=int, help='Duration in minutes')
@click.option('--commit', '-c', help='Git commit hash')
def add(text, duration, commit):
    """Добавляет новую запись"""
    click.echo(f"Adding: {text}")
    if duration:
        click.echo(f"Duration: {duration} minutes")
    if commit:
        click.echo(f"Commit: {commit}")

@cli.command()
@click.option('--all', '-a', is_flag=True, help='Show all entries')
def list(all):
    """Показывает список записей"""
    if all:
        click.echo("Showing all entries")
    else:
        click.echo("Showing recent entries")

if __name__ == '__main__':
    cli()

