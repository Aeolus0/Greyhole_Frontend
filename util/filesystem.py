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

def avail_space():
    import commands
    output = commands.getoutput('greyhole --stats | grep :')
    output = output.split('\n')
    for iter in range(0, len(output)):
        output[iter] = output[iter][2:]
    return_dict = {}
    for elem in output:
        sizes = elem[elem.index(':') + 1:]
        sizes = sizes.split('G')
        for iter in range(0,len(sizes)):
            sizes[iter] = filter(lambda x: x.isdigit(), sizes[iter])
        return_dict[elem[:elem.index(':')]] = sizes
    return return_dict

def raw_usage():
    import commands
    return commands.getoutput('greyhole --stats')

def mount(sudo_pw):
    import subprocess
    proc = subprocess.Popen(['sudo', 'mount', '-a'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    proc.stdin.write(sudo_pw + '\n')
    proc.stdin.close()
    out = proc.stdout()
    return out
