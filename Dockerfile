FROM python:3.9.7-slim
COPY ./backend /app
WORKDIR /app
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
EXPOSE 9915
ENV PATH $PATH:/usr/bin/python3.9
CMD ["python3.9", "run.py"]
