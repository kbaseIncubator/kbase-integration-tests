import re
import sys

re_typedef_string = '^\\s*typedef\\s+string\\s+(.*);$'
re_typedef_int = '^\\s*typedef\\s+int\\s+(.*);$'


def main(filename):
    # read in file
    type_defs = {}
    with open(filename) as fin:
        lines = fin.readlines()
        print(f'opened file {filename} with {len(lines)} lines')
        mode = None
        comment_line_count = None
        for raw_line in lines:
            line = raw_line.trim
            if mode == None:
                if re.match('^\\s*/*', line):
                    mode = 'comment'
                    comment_line_count = 1
                    # print('comment begin')
                elif re.match(re_typedef_string, line):
                    m = re.match(re_typedef_string, line)
                    type_name = m.group(1)
                    print('string', type_name)
                    type_defs[type_name] = {
                        'fundamental_type': 'string'
                    }
                elif re.match(re_typedef_int, line):
                    m = re.match(re_typedef_int, line)
                    type_name = m.group(1)
                    type_defs[type_name] = {
                        'fundamental_type': 'int'
                    }

            if mode == 'comment':
                if re.match('/\\*\\s*$', line):
                    mode = None
                    # print('comment end', comment_line_count)
                    comment_line_count = None
                else:
                    comment_line_count += 1

    print(type_defs)


# parse it, line by line!


def usage():
    print('parse-type type-file')
    print('Reads in a KBase kidl type spec and outputs a JSON representation')
    print('for easier consumption with other tools')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    spec_file = sys.argv[1]
    main(spec_file)
