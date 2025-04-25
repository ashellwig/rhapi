# Copyright (c) 2025 Ash Hellwig <ahellwig.dev@gmail.com>
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
"""Generates a public and private key pair."""

import base64
import nacl.signing
from pathlib import Path
from typing import Any

from rhapi.util.logger import setup_logger

logger = setup_logger()


def generate_keypair(output_directory_str: str):
    """Generate a keypair for use with Robinhood's API.

    Args:
        output_directory_str (str): Directory to output the key files.
    """
    output_directory_path: Path = Path(output_directory_str)
    output_file_plain: Path = output_directory_path / 'unencrypted_keys.txt'
    output_file_b64: Path = output_directory_path / 'encrypted_keys.txt'

    file_horizontal_line: str = '----'

    if not output_directory_path.exists():
        logger.warning('Path %s not found. Creating it.', output_directory_path)

        output_directory_path.mkdir(parents=True, exist_ok=False)

        if output_directory_path.exists():
            logger.info('Output folder successfully created! Continuing.')
    else:
        logger.info('Found output directory. Continuing to generate keys.')

    # Create the plaintext keys.
    private_key_plain: nacl.signing.SigningKey = \
        nacl.signing.SigningKey.generate()
    public_key_plain: Any = private_key_plain.verify_key

    # Convert plaintext keys to base64 format.
    private_key_b64: str = base64.b64encode(private_key_plain.encode()).decode()
    public_key_b64: str = base64.b64encode(public_key_plain.encode()).decode()

    # Write the plaintext files to the output directory.
    output_file_plain.write_text(
            f'{file_horizontal_line}\n'
            'PRIVATE KEY (plaintext):\n'
            f'{private_key_plain}\n'
            f'{file_horizontal_line}\n'
            '\n'
            f'{file_horizontal_line}\n'
            'PUBLIC KEY (plaintext):\n'
            f'{public_key_plain}\n'
            f'{file_horizontal_line}\n'
    )
    logger.info('Wrote plaintext file to: %s', output_file_plain.absolute())

    # Write the base64 encoded files to the output directory.
    output_file_b64.write_text(
            f'{file_horizontal_line}\n'
            'PRIVATE KEY (encoded):\n'
            f'{private_key_b64}\n'
            f'{file_horizontal_line}\n'
            '\n'
            f'{file_horizontal_line}\n'
            'PUBLIC KEY (encoded):\n'
            f'{public_key_b64}\n'
            f'{file_horizontal_line}\n'
    )
    logger.info('Wrote encoded file to: %s', output_file_b64.absolute())


def add_one(number: int) -> int:
    """Increments the given number by one.

    Args:
        number (int): Number to increment.

    Returns:
        int: Incremented number.
    """
    logger.info('Running add_one')

    return number + 1
