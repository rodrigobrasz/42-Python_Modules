#!/usr/env python 3

def secure_archive(f: str, act: str = 'r', data: str = "") -> tuple[bool, str]:
    check = True
    try:
        if act == "r":
            with open(f, 'r') as r_file:
                data = r_file.read()
                return (check, data)
        elif act == "w":
            with open(f, 'w') as w_file:
                w_file.write(data)
                return (check, "'Content successfully written to file'")
        return (False, "Invalid Action")
    except OSError as e:
        check = False
        return (check, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file'))

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive('test_archive.txt', 'w',
                         '[FRAGMENT 001] Digital preservation protocols '
                         'established 2087...'))

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive('test_archive.txt', 'r'))


if __name__ == "__main__":
    main()
