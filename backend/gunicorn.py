bind = '0.0.0.0:8000'

workers = 4
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 2000

# 指定pid文件位置
pidfile = '/tmp/gunicorn.pid'

reload = "True"

# 日志配置
loglevel = "debug"
errorlog = "/tmp/rent/error.log"
errorlog = "-"
accesslog = "/tmp/rent/access.log"
accesslog = "-"
# access日志格式。
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
