#django-go
---
##1. 简介   
django是MVC模型,模型、视图、控制器

##2. 安装
pip install django

##3. 创建项目  
- 在当前目录，创建项目  
**`$  django-admin startproject <projectname>`**

- 运行服务器  
**`$  python manage.py runserver [ip:port]`**  
不输入[ip:port]参数时，默认监听127.0.0.1:8000，在浏览器中访问http://127.0.0.1:8000将有所显示

-  创建应用  
**`$  python manage.py startapp <appname>`**  
创建一个应用，应用是独立的类式插件，可以用于多个项目

- 创建数据库  
**`$  python manage.py migrate`**

- 激活模型
  - 在`settings.py`中`INSTALLED_APPS`中添加`<appname>.apps.PollsConfig`  
  - 执行**`$  python manage.py makemigrations <appname>`**，检测模型的修改，并完成一次迁移（类似一个缓存）保存在`<appname>/migrations/0001_initial.py`文件中。使用命令`python manage.py sqlmigrate polls 0001`查看迁移将执行的sql语句。再次执行`$  python manage.py migrate`将未执行的迁移应用在数据库上。