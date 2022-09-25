import subprocess
from subprocess import Popen
import tarfile
import sys, os
from datetime import date

def get_backup_name():
    cur_date = str(date.today())
    hostname = Popen(['hostname'], stdout = subprocess.PIPE).communicate()[0]
    backup_name_lower = '/opt/backup/' +'backup_' + hostname[:hostname.index('.')].lower() + '_' + cur_date + '.tar.bz2'
    backup_name_upper = '/opt/backup/' +'backup_' + hostname[:hostname.index('.')].upper() + '_' + cur_date + '.tar.bz2'
    if os.path.isfile(backup_name_lower):
        return backup_name_lower
    elif os.path.isfile(backup_name_upper):
        return backup_name_upper
    else:
        print('Please dowload archive to /opt/backup directory.\nExit')
        sys.exit(0)

def process_find():
    filtering = Popen(['ps', 'aux'], stdout=subprocess.PIPE).communicate()[0].split()
    pids = []
    for position in range(len(filtering)):
        if filtering[position] == '/usr/bin/mysqld_safe':
            pids.append(filtering[position - 10])
        if filtering[position] == '/usr/sbin/mysqld':
            pids.append(filtering[position - 9])
        if len(pids) == 2: break
    return pids

def process_kill(pid):
    subprocess.Popen(['kill', '-9', pid])

def services_stop():
    Popen(['rm', '-rf', '/var/run/mysqld/mysqld.pid']).wait()
    Popen(['rm', '-rf', '/var/lock/subsys/mysqld']).wait()
    try_mysqld = Popen(['service', 'mysqld', 'stop'], stdout=subprocess.PIPE).communicate()[0].split()
    try_crond = Popen(['service', 'crond', 'stop'], stdout=subprocess.PIPE).communicate()[0].split()
    if  try_mysqld[-2] != 'OK' or try_crond[-2] != 'OK':
        print('Mysqld or crond cannot stop correct.\nExit')
        sys.exit(0)

def directory_clean():
    for file in os.listdir('/var/lib/mysql'):
        path = '/var/lib/mysql/'+ file
        Popen(['rm', '-rf', path]).wait()

def database_extract():
    with tarfile.open(BACKUP_ARCHIVE, mode='r:bz2', bufsize=10240) as archive:
        archive.extractall(path='/var/lib/mysql')

def backup_check():
    inno_check = Popen(['/usr/bin/innobackupex', '/var/lib/mysql', '--apply-log'], stdout=subprocess.PIPE).communicate[0].split()
    if inno_check[-1] != 'OK!':
        print('Problem with innobackupex.\nExit')
        sys.exit(0)

if __name__ == '__main__':
    print('Download backup archive manually with scp. This function still TODO\n')

    print('Check correct archive name\n')
    BACKUP_ARCHIVE = get_backup_name()

    print('Kill mysqld process\n')
    for pid in process_find():
        process_kill(pid)

    print('Stop mysqld and crond services\n')
    services_stop()

    print('Clean /var/lib/mysql\n')
    directory_clean()

    print('Unpack backup archive to /var/lib/mysql\n')
    database_extract()

    print('Checking unpacking data with /usr/bin/innobackupex\n')
    backup_check()
