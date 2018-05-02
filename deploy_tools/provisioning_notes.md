服务器配置新网站
==========
##需要安装的包：
* nginx
* Python3
* Git
* pip
* virtualenv
以Ubuntu为例，可以执行下面的命令安装：
sudo apt-get install nginx git python3 python3-pip
sudo pip3 install virtualenv

##配置Nginx虚拟主机
* 参考nginx.template.conf
* 把SITENAME替换成所需的域名

##将gunicorn设为开机自启动，如果崩溃了还要自动重启，Ubuntu16.04采用systemd的方式
* 参考gunicorn-service.template.conf
* 把SITENAME替换成所需的域名

##文件夹结构
假设有用户账户，家目录为/home/username

/home/username
|___sites
    |___SITENAME
        |___database
	|___source
	|___static
	|___virtualenv
