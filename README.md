# W1ndys-bot

基于 Python 和 OneBot 11 的 QQ 机器人实现

## 介绍及背景

Python 编写的模块加载器，使用 WebSocket 客户端模式对接上游服务，支持 OneBot 协议，如遇到问题请提 issue

本加载器不以插件的形式进行加载，而是以模块的形式进行加载，没有傻瓜式配置方法，对配置能力有些要求。

> 写这个加载器的原因是，了解到了 mf 师傅的插件式加载器，但我本人并不习惯这种方法，于是就写了这个模块式加载器，整个加载器的配置全部采用 Python 模块化编程，功能的开发模式完全基于原生 Onebot11。
> 有关插件式加载器的文档请参考：[School-Robot/Plugin-Loader: 用于对接 OneBot 的 Python 插件加载器 (github.com)](https://github.com/School-Robot/Plugin-Loader)

## 加载器特色

- 模块化编程，易于维护
- 支持断线重连，无需手动重启
- 支持上线提醒（QQ），掉线提醒（钉钉）
- 支持 OneBot 11 标准，无需修改机器人代码
- 支持 WebSocket 客户端模式，无需修改机器人代码

## 开发文档

OneBot 11 标准 [botuniverse /onebot-11: OneBot 11 标准 (github.com)](https://github.com/botuniverse/onebot-11#/)

go-cqhttp [API | go-cqhttp 帮助中心](https://docs.go-cqhttp.org/api/)

> 备注：本机器人实现基于 **Python** 做核心开发，使用 **NapCatQQ** 作为消息平台，**OneBot 11** 作为 QQ 机器人 API 实现。

## 使用方法

### 安装依赖

```bash
pip install -r requirements.txt
```

### 配置基本信息

#### 配置 ws 连接和管理员

打开`app/config.py`

```python
owner_id = [123]  # 机器人root管理员 QQ 号

ws_url = "xxx"  # napcatQQ 监听的 WebSocket API 地址

token = "xxx"  # 如果需要认证，请填写认证 token
```

#### 配置钉钉通知

打开`app/config.py`

```python
# 这里替换为你自己的TOKEN，不要直接用我的，我的有IP验证，用我的也没用
DD_BOT_TOKEN = "xxx"
# 这里替换为你自己的SECRET，不要直接用我的，我的有IP验证，用我的也没用
DD_BOT_SECRET = "xxx"
```

### 开发文档

开发功能请参考：[dev.md](dev.md)
