#!/usr/bin/env python
# coding=utf-8

import click

from magnet_dht.dht import start_server
from magnet_dht.magnet_to_torrent_aria2c import magnet2torrent
from magnet_dht.parse_torrent import parse_torrent


@click.command()
@click.option('--dht', 'action', flag_value='dht', default=True)
@click.option('--convert', 'action', flag_value='convert')
@click.option('--parse', 'action', flag_value='parse')
def command_line_runner(action):
    """
    执行命令行操作
    """
    if action == 'dht':
        start_server()
    elif action == 'convert':
        magnet2torrent()
    elif action == 'parse':
        parse_torrent()


if __name__ == "__main__":
    command_line_runner()
