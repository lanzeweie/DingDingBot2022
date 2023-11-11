# 使用一个基础镜像
FROM python:3.12.0

# 设置工作目录
WORKDIR /dingtingbot

# 复制应用程序代码到镜像中
COPY . /dingtingbot

# 在容器中执行 yarn install 安装依赖
RUN cd /dingtingbot && pip install -r requirements.txt


EXPOSE 8978


#  依次运行
#  docker build -t python:3.12.0 .
#  docker run -d -p 8978:8978 --name dingdingbot python:3.12.0 tail -f /dev/null
#  docker exec -it dingdingbot /bin/bash
