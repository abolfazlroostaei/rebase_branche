import os
import subprocess

success_list = []
failed_list = []


def check_branch(item):
    subprocess.run(f'git checkout {item}', shell=True)
    result = subprocess.run('git rebase master', shell=True, capture_output=True)
    print('result--->', result)
    if result.returncode == 0:
        success_list.append(item)

    if result.returncode != 0:
        print('this is a conflit error')
        failed_list.append(item)
        print(subprocess.run('git rebase --abort', shell=True))


subprocess.run('cd /home/abolfazl/temp/clone', shell=True)

#fetch
up_date = subprocess.run('git fetch orign', shell=True, capture_output=True)

#branches list
branches = subprocess.check_output('git branch -r', shell=True)
all_branch = (branches.decode().strip().replace('orign/', '').split('\n'))
my_branch = [x.strip() for x in all_branch]
print(my_branch)

if up_date.returncode == 0:
    success_list = my_branch
else:
    for item in my_branch:
        check_branch(item)

print('success_list= ', success_list)
print('failed_list= ', failed_list)
