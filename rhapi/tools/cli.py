# Copyright (c) 2025 Ash Hellwig <ahellwig.dev@gmail.com>
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import click

from rhapi.tools.generate_key_pair import add_one


@click.command()
@click.option('-n', '--num', type=int)
def cli_add_one(num: int):
    click.echo(str(add_one(number=num)))
