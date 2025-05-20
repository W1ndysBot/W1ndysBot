from . import *
import logger


class FriendNoticeHandler:
    """
    好友通知处理器
    """

    def __init__(self, notice_handler):
        self.notice_handler = notice_handler
        self.websocket = notice_handler.websocket
        self.msg = notice_handler.msg
        self.time = notice_handler.time
        self.formatted_time = notice_handler.formatted_time
        self.notice_type = notice_handler.notice_type
        self.sub_type = notice_handler.sub_type
        self.user_id = notice_handler.user_id

    async def handle_friend_notice(self):
        """
        处理好友通知
        """
        try:
            # 如果没开启私聊开关，则不处理
            if not load_switch(MODULE_NAME)["private"]:
                return

            if self.notice_type == "friend_add":
                await self.handle_friend_add()
            elif self.notice_type == "friend_recall":
                await self.handle_friend_recall()
            elif self.notice_type == "offline_file":
                await self.handle_offline_file()
            elif self.notice_type == "client_status":
                await self.handle_client_status()
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理好友通知失败: {e}")

    # 好友相关通知处理
    async def handle_friend_add(self):
        """
        处理好友添加通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理好友添加通知失败: {e}")

    async def handle_friend_recall(self):
        """
        处理好友撤回通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理好友撤回通知失败: {e}")

    async def handle_offline_file(self):
        """
        处理接收到离线文件通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理接收到离线文件通知失败: {e}")

    async def handle_client_status(self):
        """
        处理其他客户端在线状态变更通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理其他客户端在线状态变更通知失败: {e}")
