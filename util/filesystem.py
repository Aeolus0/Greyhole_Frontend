__author__ = 'Dhash'


def get_storage_disks(conf_path):
    import commands
    trimmed_lines = commands.getoutput('cat ' + conf_path + ' | grep storage_pool_drive | sed s/storage_pool_drive//')
    trimmed_lines = trimmed_lines.split('\n')
    uncommented_lines = []
    for elem in trimmed_lines:
        if elem[0] != '#':
            uncommented_lines.append(elem)
    for elem in range(0, len(uncommented_lines)):
        if ',' in uncommented_lines[elem]:
            uncommented_lines[elem] = uncommented_lines[elem][5:uncommented_lines[elem].index(',')]
    return uncommented_lines

def avail_space(conf_path):
    import commands
    output = commands.getoutput('df -h')
    output = output.split('\n')
    for elem in output:
        elem = elem[::-1]
        val = elem.index(' ')
        elem = elem[::-1]
        val = len(elem) - val
        final_drive_lines = []
        if elem[val:] in get_storage_disks(conf_path):
            final_drive_lines.append(elem)