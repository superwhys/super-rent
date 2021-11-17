# Super Rent API接口文档

pip3 install -r requirements.txt

运行方式：python3 run.py

接口文档地址： /docs

配置nginx反向代理

转发接口
此配置较为简单

```shell
...
    location /fastapi/ {
		proxy_pass http://fastapi_host/fastapi/;
	}
...
```

转发文档
接口文档使用默认时，还需添加如下配置

  ```shell
 location /openapi.json {
		proxy_pass http://fastapi_host/openapi.json;
	}
  ```

