from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = 'https://github.com/YYWQ/mysite'

#主函数，在命令行中调用这个函数
def deploy():
    site_folder = '/home/%s/sites/%s' % (env.user, env.host)
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder,env.host)
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)

#创建目录结构
def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ('database', 'static','virtualenv', 'source'):
        run('mkdir -p %s/%s' % (site_folder, subfolder))

#拉取源码
def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):
        run('cd %s && git fetch' % (source_folder,))
    else:
        run('git clone %s %s' % (REPO_URL,source_folder))
    current_commit = local("git log -n 1 --foramt=%H",capture=True)
    run('cd &s && git reset --hard %s'
        % (source_folder,current_commit)
        )

#更新配置文件
def _update_settings(source_folder,site_name):
    settings_path = source_folder + '/mysite/settings.py'
    sed(settings_path, "DEBUG = True","DEBUG = False")
    sed(settings_path,
        'ALLOWED_HOSTS =.+$',
        'ALLOWED_HOSTS = ["%s"]' % (site_name,))
    secret_key_file = source_folder + '/mysite/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file,"SECRET_KEY = '%s'" % (key,))
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')

#创建或更新虚拟环境
def _update_virtualenv(source_folder):
    virtualenv_folder = source_folder + '/../virtualenv'
    if not exists(virtualenv_folder + '/bin/pip'):
        run('virtualenv --python=python3 %s'
            % (virtualenv_folder,)
            )
    run('%s/bin/pip install -r %s/requirements.txt'
        % (virtualenv_folder,source_folder)
        )

#更新静态文件
def _update_static_files(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py collectstatic --noinput'
        % (source_folder,)
        )

#更新数据库
def _update_database(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py migrate --noinpute'
        % (source_folder,)
        )
