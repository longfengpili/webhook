# 使用 Go 进行编译
FROM golang:alpine AS build

# 维护者信息
MAINTAINER Dolf <398745129@qq.com>

# 安装依赖
RUN apk add --update --no-cache -t build-deps curl gcc libc-dev libgcc

# 设置工作目录
WORKDIR /go/src/github.com/adnanh/webhook

# 设置环境变量
ENV WEBHOOK_VERSION 2.8.1

# 下载并解压 webhook 源码
RUN curl -L --silent -o webhook.tar.gz https://github.com/adnanh/webhook/archive/${WEBHOOK_VERSION}.tar.gz && \
    tar -xzf webhook.tar.gz --strip 1

# 获取依赖
RUN go get -d -v

# 编译 webhook，禁用 CGO
RUN CGO_ENABLED=0 go build -ldflags="-s -w" -o /usr/local/bin/webhook


# 使用Ubuntu 镜像作为最终镜像
FROM ubuntu:latest

# # 更新软件包列表并安装 bash
# RUN apt-get update && apt-get install -y \
#     bash \
#     && rm -rf /var/lib/apt/lists/*

# 设置环境变量，以支持中文
ENV LANG zh_CN.UTF-8
ENV LANGUAGE zh_CN.UTF-8
ENV LC_ALL zh_CN.UTF-8

# 设置容器的时区为东八区，即北京时间
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 更新系统包列表并安装
RUN echo "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse" > /etc/apt/sources.list \
    && echo "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse" >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y locales wget git python3-pip \
    && locale-gen zh_CN.UTF-8 \
    && rm -rf /var/lib/apt/lists/*

#Copy requirements
COPY requirements.txt ./requirements.txt

#Pip
RUN pip3 install --break-system-packages -i https://mirrors.ustc.edu.cn/pypi/web/simple -r requirements.txt

# 从构建阶段复制 webhook 二进制文件
COPY --from=build /usr/local/bin/webhook /usr/local/bin/webhook

# 复制配置文件
COPY ./webhook_init /webhook_init

# 赋予启动脚本执行权限
RUN chmod +x /webhook_init/startup.sh

# 设置工作目录
WORKDIR /webhook

# 暴露端口
EXPOSE 9000

# 设置入口点为启动脚本
ENTRYPOINT ["/webhook_init/startup.sh"]

# 设置默认命令
CMD ["-verbose", "-hotreload", "-hooks=config/hooks.yml"]
