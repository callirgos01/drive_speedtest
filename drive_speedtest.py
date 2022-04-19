from os import system;

output_name = "output.txt"
def run_test(drive_name, permissions):
    print('############################################################################\r\n####testing [{0}]#######################'.format(drive_name))
    print('write test...')
    #write test
    system('sync;{0} dd of={1}/tempfile if=/dev/zero bs=1M count=1024; sync'.format(permissions, drive_name, output_name))
    print('read test...')
    #read test
    system('sync;{0} dd if={1}/tempfile of=/dev/zero bs=1M count=1024; sync'.format(permissions, drive_name, output_name))
    system('{0} rm {1}/tempfile'.format(permissions, drive_name));

# run_test('/backup-btrfs', '')

run_test('/media-pool', '')
run_test('/programs-pool', '')
run_test('/tmp', '')
run_test('/second-zfs-pool','')
# run_test('/backup-truenas','')

