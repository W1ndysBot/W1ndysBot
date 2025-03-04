# handlers/message_handler.py


import json
import logging
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 统一从各模块导入事件处理器
from app.scripts.Example.main import handle_events as handle_Example_events

# 系统模块
from app.system import handle_events as handle_System_events
from app.switch import handle_events as handle_Switch_events


# 处理ws消息
async def handle_message(websocket, message):
    try:
        msg = json.loads(message)

        logging.info(f"收到ws事件：{msg}")

        # 系统基础功能
        await handle_System_events(websocket, msg)
        await handle_Switch_events(websocket, msg)

        # 功能模块事件处理
        await handle_Example_events(websocket, msg)
    except Exception as e:
        logging.error(f"处理ws消息的逻辑错误: {e}")
