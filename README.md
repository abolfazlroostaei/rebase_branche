# check rebase in git_projects

*run shell commands in python with subprocess library*

```python
import subprocess

```

*a primary command used to download contents from a remote repository*
```python
up_date = subprocess.run('git fetch orign', shell=True, capture_output=True)

```



*List all branches with the code below*
```python

branches = subprocess.check_output('git branch -r', shell=True)
all_branch = (branches.decode().strip().replace('orign/', '').split('\n'))
my_branch = [x.strip() for x in all_branch]

```
*if my branch is update, add branch to success_list. else call check_branch def*
*in my def if rabase successfull,add branch to success_list,else run rebase --abort*
```python

 print(subprocess.run('git rebase --abort', shell=True))
 ```


