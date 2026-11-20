#!/usr/bin/env python3
"""Retrieve pinned public FilmCraft sources, apply the community patch, optionally build."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination', type=Path, default=Path('build/filmcraft-source'))
    parser.add_argument('--source-only', action='store_true')
    parser.add_argument('--release', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    manifest = json.loads((root / 'BUILD-MANIFEST.json').read_text())
    patch = root / 'patches/premiere-import.patch'
    if hashlib.sha256(patch.read_bytes()).hexdigest() != manifest['patch_sha256']:
        raise SystemExit('Patch checksum mismatch; no sources changed.')
    destination = args.destination.resolve()
    if destination.exists():
        raise SystemExit('Destination already exists. Choose a new empty path; nothing was overwritten.')
    destination.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(['git', 'init', str(destination)], check=True)
    subprocess.run(['git', '-C', str(destination), 'remote', 'add', 'origin', manifest['upstream'] + '.git'], check=True)
    subprocess.run(['git', '-C', str(destination), 'fetch', '--depth', '1', 'origin', manifest['base_commit']], check=True)
    subprocess.run(['git', '-C', str(destination), 'checkout', '--detach', 'FETCH_HEAD'], check=True)
    actual = subprocess.check_output(['git', '-C', str(destination), 'rev-parse', 'HEAD'], text=True).strip()
    if actual != manifest['base_commit']:
        raise SystemExit('Upstream commit mismatch; patch was not applied.')
    subprocess.run(['git', '-C', str(destination), 'apply', '--check', str(patch)], check=True)
    subprocess.run(['git', '-C', str(destination), 'apply', str(patch)], check=True)
    print('Patched sources:', destination, flush=True)
    if not args.source_only:
        command = ['cargo', 'build', '--locked', '-p', 'filmcraft', '-p', 'filmcraft-cli']
        if args.release:
            command.append('--release')
        subprocess.run(command, cwd=destination, check=True)
        print('Executables:', destination / 'target' / ('release' if args.release else 'debug'))


if __name__ == '__main__':
    main()
