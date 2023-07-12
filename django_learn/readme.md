

### 构建环境
```
python -m venv ll_env
```

### Linux

构建环境

```
source ll_env/bin/activate
```
### Win

####  开启PowerShell 执行策略
```
Set-ExecutionPolicy RemoteSigned
 或者
Set-ExecutionPolicy Unrestricted
```

构建环境

```
ll_env/Scripts/activate
```

### 安装

**安装`Django`**

```
pip install django
```

**创建项目**

```
django-admin startproject learning .
```

最重要的是settings.py、urls.py和wsgi.py。

- settings.py 管理项目设置
- urls.py 创建哪些页面来响应浏览器请求
- wsgi.py  Web服务器网关接口 （Web server gateway interface）的首字母缩写。


**构建数据库**

sqlite
```
python manage.py migrate
```



## 查询进程占用

```
# 查询PID
netstat -ano | findstr :8000

# 查询PID应用
tasklist /fi 'PID eq  123'

# 杀死
taskkill /PID 1234
```


```
python manage.py makemigrations user


```