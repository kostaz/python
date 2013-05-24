#!/usr/bin/python

import subprocess, os, sys

git_dir = sys.argv[1]
subtree_dir = sys.argv[2]
git_module_dir = 'avanta_lp_family'
git_module_branch = git_module_dir

def clean() :
	dir_to_rm = subtree_dir + git_module_dir
	print 'Deleting dir [' + dir_to_rm + ']'
	pr = subprocess.Popen(['/bin/rm', '-rf', dir_to_rm],
		cwd = os.path.dirname(subtree_dir),
		stdout = subprocess.PIPE,
		stderr = subprocess.PIPE,
		shell = False)
	(out, error) = pr.communicate()
	# print out
	# print error

	print 'Deleting git branch [' + git_module_branch + ']'
	pr = subprocess.Popen(['/usr/local/bin/git', 'branch', '-D', git_module_branch],
		cwd = os.path.dirname(git_dir),
		stdout = subprocess.PIPE,
		stderr = subprocess.PIPE,
		shell = False)
	(out, error) = pr.communicate()
	# print out
	# print error

print 'git_dir           = [' + git_dir + ']'
print 'subtree_dir       = [' + subtree_dir + ']'
print 'git_module_dir    = [' + git_module_dir + ']'
print 'git_module_branch = [' + git_module_branch + ']'
print

clean()

pr = subprocess.Popen(['/usr/local/bin/git', 'subtree', 'split',
	'--prefix=board/mv_ebu/alp/avanta_lp_family/', 'v2013.01..',
	'--branch', git_module_dir],
	cwd = os.path.dirname(git_dir),
	stdout = subprocess.PIPE,
	stderr = subprocess.PIPE,
	shell = False)

(out, error) = pr.communicate()
print out
print error

subgit_dir = subtree_dir + git_module_dir + '/'
print 'Creating dir [' + subgit_dir + ']'
pr = subprocess.Popen(['/bin/mkdir', subgit_dir],
	cwd = os.path.dirname(subtree_dir),
	stdout = subprocess.PIPE,
	stderr = subprocess.PIPE,
	shell = False)
(out, error) = pr.communicate()
# print out
# print error

print 'Initializing git in [' + subgit_dir + ']'
pr = subprocess.Popen(['/usr/local/bin/git', 'init'],
	cwd = os.path.dirname(subgit_dir),
	stdout = subprocess.PIPE,
	stderr = subprocess.PIPE,
	shell = False)

(out, error) = pr.communicate()
print out
print error

print 'Fetching git branch ...'
pr = subprocess.Popen(['/usr/local/bin/git', 'fetch', git_dir, 'avanta_lp_family'],
	cwd = os.path.dirname(subgit_dir),
	stdout = subprocess.PIPE,
	stderr = subprocess.PIPE,
	shell = False)

(out, error) = pr.communicate()
print out
print error

print 'Checking out git branch ...'
pr = subprocess.Popen(['/usr/local/bin/git', 'checkout', '-b', git_module_branch, 'FETCH_HEAD'],
	cwd = os.path.dirname(subgit_dir),
	stdout = subprocess.PIPE,
	stderr = subprocess.PIPE,
	shell = False)

(out, error) = pr.communicate()
print out
print error


'''
pr = subprocess.Popen(['/usr/bin/git', 'status'],
	cwd = os.path.dirname('/home/kostaz/my/dev/stuff/python_plays/repo-alp-u-boot-2013.01/u-boot/'),
	stdout = subprocess.PIPE,
	stderr = subprocess.PIPE,
	shell = False)

(out, error) = pr.communicate()
print out
print error
'''


'''
git subtree split --prefix=board/mv_ebu/alp/avanta_lp_family/ v2013.01.. --branch avanta_lp_family
'''
