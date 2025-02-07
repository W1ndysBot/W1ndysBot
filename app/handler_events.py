# handlers/message_handler.py


import json
import logging
import os
import sys
import asyncio
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# 总开关
from app.switch import handle_GroupSwitch_group_message


# 系统
from app.system import handle_System_group_message

# api
from app.api import *

# 配置
from app.config import *


# 处理消息事件的逻辑
async def handle_message_event(websocket, msg):
    try:
        # 处理群消息
        if msg.get("message_type") == "group":

            # 系统必需功能
            await handle_System_group_message(websocket, msg)  # 处理系统消息
            await handle_GroupSwitch_group_message(websocket, msg)  # 处理群组开关

            # 依次执行scripts功能

        # 处理私聊消息
        elif msg.get("message_type") == "private":
            # 由于私聊风险较大，不处理私聊消息，仅占位
            pass

        else:
            logging.info(f"收到未知消息类型: {msg}")

    except KeyError as e:
        logging.error(f"处理消息事件的逻辑错误: {e}")


# 处理通知事件的逻辑
async def handle_notice_event(websocket, msg):

    # 处理群通知
    if msg.get("post_type") == "notice":
        group_id = msg["group_id"]
        logging.info(f"收到群通知事件, 群ID: {group_id}")


# 处理请求事件的逻辑
async def handle_request_event(websocket, msg):
    pass


# 处理元事件的逻辑，每次心跳周期检查一次，用于启动时确保数据目录存在
async def handle_meta_event(websocket):
    try:
        pass
    except Exception as e:
        logging.error(f"处理元事件的逻辑错误: {e}")


# 处理定时任务，每个心跳周期检查一次
async def handle_cron_task(websocket):
    try:
        pass

    except Exception as e:
        logging.error(f"处理定时任务的逻辑错误: {e}")


# 处理回应消息
async def handle_response_message(websocket, message):
    msg = json.loads(message)
    if msg.get("status") == "ok":
        pass


# 处理ws消息
async def handle_message(websocket, message):

    msg = json.loads(message)

    # 处理回应消息
    if msg.get("status") == "ok":
        logging.info(f"收到回应消息：{msg}")
        await handle_response_message(websocket, message)

    # 处理事件
    if "post_type" in msg:
        logging.info(f"收到事件消息：{msg}")
        if msg["post_type"] == "message":
            # 处理消息事件
            await handle_message_event(websocket, msg)
        elif msg["post_type"] == "notice":
            # 处理通知事件
            await handle_notice_event(websocket, msg)
        elif msg["post_type"] == "request":
            # 处理请求事件
            await handle_request_event(websocket, msg)
        elif msg["post_type"] == "meta_event" and msg["meta_event_type"] == "heartbeat":
            # 处理元事件
            await handle_meta_event(websocket)
            # 处理定时任务，每个心跳周期检查一次
            await handle_cron_task(websocket)
