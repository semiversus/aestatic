def parse_input(line):
    # TODO: split the string `line` into the first word(`cmd`) and the rest(`argument`)
    return cmd, argument


def input_loop(items):
    while True:
        input_line = input('> ')
        cmd, argument = parse_input(input_line)

        if cmd == 'add':
            # TODO: `argument` should be added to `items`
        elif cmd == 'remove':
            # TODO: the given index should be removed from `items`
            #       If index is not valid, the command should do nothing
        # TODO: add 'list', 'exit' and 'help' commands

    return items

def main():
    items = list()
    return input_loop(items)


if __name__ == '__main__':
    main()