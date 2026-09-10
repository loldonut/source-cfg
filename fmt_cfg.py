import argparse
import shutil
import os
import sys

def format_content(content, tab_width=5):
    lines = content.splitlines()
    processed_lines = []
    max_var_length = 0

    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 2 and parts[1].startswith('"'):
            max_var_length = max(max_var_length, len(parts[0]))

    target_column = max_var_length + tab_width

    for line in lines:
        parts = line.strip().split()

        if len(parts) >= 2 and parts[1].startswith('"'):
            var_name = parts[0]
            value = ' '.join(parts[1:])

            spacing = ' ' * (target_column - len(var_name))
            processed_lines.append(f'{var_name}{spacing}{value}')
        else:
            processed_lines.append(line)

    return '\n'.join(processed_lines)

def main():
    parser = argparse.ArgumentParser(description='Align CFG variables into clean columns.')
    parser.add_argument('file', help='Path to the .cfg file')
    parser.add_argument('-t', '--tab-width', type=int, default=5, help='Spaces after the longest variable (default: 5)')

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f'error: File \'{args.file}\' not found.')
        sys.exit(1)

    backup_path = f'{args.file}.bak'
    try:
        shutil.copy2(args.file, backup_path)
        print(f'backup created: {backup_path}')
    except Exception as e:
        print(f'failed to create backup: {e}')
        sys.exit(1)

    try:
        with open(args.file, 'r') as f:
            original_content = f.read()

        formatted_content = format_content(original_content, args.tab_width)

        with open(args.file, 'w') as f:
            f.write(formatted_content)

        print(f'successfully formatted: {args.file}')

    except Exception as e:
        print(f'an error occurred during formatting: {e}')
        sys.exit(1)

if __name__ == '__main__':
    main()
