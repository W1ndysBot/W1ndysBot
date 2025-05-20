from . import *
import logger
from datetime import datetime


class NoticeHandler:
    """
    通知处理器
    websocket: 连接对象
    msg: 通知消息
    相关文档: https://napneko.github.io/develop/event#notice-%E4%BA%8B%E4%BB%B6
    """

    def __init__(self, websocket, msg):
        self.websocket = websocket
        self.msg = msg
        self.time = msg.get("time", "")
        self.formatted_time = datetime.fromtimestamp(self.time).strftime(
            "%Y-%m-%d %H:%M:%S"
        )  # 格式化时间
        self.notice_type = msg.get("notice_type", "")
        self.sub_type = msg.get("sub_type", "")
        self.user_id = str(msg.get("user_id", ""))
        self.group_id = str(msg.get("group_id", ""))
        self.operator_id = str(msg.get("operator_id", ""))

    async def handle(self):
        """
        处理通知
        """
        try:
            if self.notice_type.startswith("friend_"):
                await self.handle_friend_notice()
            elif self.notice_type.startswith("group_"):
                await self.handle_group_notice()
            elif self.notice_type == "notify":
                await self.handle_notify_notice()
            elif self.notice_type == "essence":
                await self.handle_essence_notice()
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理通知失败: {e}")

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

    async def handle_group_notice(self):
        """
        处理群聊通知
        """
        try:
            # 如果没开启群聊开关，则不处理
            if not load_switch(MODULE_NAME)["group"].get(self.group_id, False):
                return

            if self.notice_type == "group_admin":
                await self.handle_group_admin()
            elif self.notice_type == "group_ban":
                await self.handle_group_ban()
            elif self.notice_type == "group_card":
                await self.handle_group_card()
            elif self.notice_type == "group_decrease":
                await self.handle_group_decrease()
            elif self.notice_type == "group_increase":
                await self.handle_group_increase()
            elif self.notice_type == "group_recall":
                await self.handle_group_recall()
            elif self.notice_type == "group_upload":
                await self.handle_group_upload()
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理群聊通知失败: {e}")

    async def handle_notify_notice(self):
        """
        处理通知事件
        """
        try:
            if self.sub_type == "poke":
                await self.handle_notify_poke()
            elif self.sub_type == "input_status":
                await self.handle_notify_input_status()
            elif self.sub_type == "title":
                await self.handle_notify_title()
            elif self.sub_type == "profile_like":
                await self.handle_notify_profile_like()
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理通知事件失败: {e}")

    async def handle_essence_notice(self):
        """
        处理精华消息通知
        """
        try:
            if self.sub_type == "add":
                await self.handle_essence_add()
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理精华消息通知失败: {e}")

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

    # 群聊相关通知处理
    async def handle_group_admin(self):
        """
        处理群聊管理员变动通知
        """
        try:
            if self.sub_type == "set":
                await self.handle_group_admin_set()
            elif self.sub_type == "unset":
                await self.handle_group_admin_unset()
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理群聊管理员变动通知失败: {e}")

    async def handle_group_admin_set(self):
        """
        处理群聊管理员增加通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理群聊管理员增加通知失败: {e}")

    async def handle_group_admin_unset(self):
        """
        处理群聊管理员减少通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理群聊管理员减少通知失败: {e}")

    async def handle_group_ban(self):
        """
        处理群聊禁言通知
        """
        try:
            if self.sub_type == "ban":
                await self.handle_group_ban_ban()
            elif self.sub_type == "lift_ban":
                await self.handle_group_ban_lift_ban()
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理群聊禁言通知失败: {e}")

    async def handle_group_ban_ban(self):
        """
        处理群聊禁言 - 禁言通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理群聊禁言 - 禁言通知失败: {e}")

    async def handle_group_ban_lift_ban(self):
        """
        处理群聊禁言 - 取消禁言通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理群聊禁言 - 取消禁言通知失败: {e}")

    async def handle_group_card(self):
        """
        处理群成员名片更新通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理群成员名片更新通知失败: {e}")

    async def handle_group_decrease(self):
        """
        处理群聊成员减少通知
        """
        try:
            if self.sub_type == "leave":
                await self.handle_group_decrease_leave()
            elif self.sub_type == "kick":
                await self.handle_group_decrease_kick()
            elif self.sub_type == "kick_me":
                await self.handle_group_decrease_kick_me()
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理群聊成员减少通知失败: {e}")

    async def handle_group_decrease_leave(self):
        """
        处理群聊成员减少 - 主动退群通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理群聊成员减少 - 主动退群通知失败: {e}")

    async def handle_group_decrease_kick(self):
        """
        处理群聊成员减少 - 成员被踢通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理群聊成员减少 - 成员被踢通知失败: {e}")

    async def handle_group_decrease_kick_me(self):
        """
        处理群聊成员减少 - 登录号被踢通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理群聊成员减少 - 登录号被踢通知失败: {e}")

    async def handle_group_increase(self):
        """
        处理群聊成员增加通知
        """
        try:
            if self.sub_type == "approve":
                await self.handle_group_increase_approve()
            elif self.sub_type == "invite":
                await self.handle_group_increase_invite()
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理群聊成员增加通知失败: {e}")

    async def handle_group_increase_approve(self):
        """
        处理群聊成员增加 - 管理员已同意入群通知
        """
        try:
            pass
        except Exception as e:
            logger.error(
                f"[{MODULE_NAME}]处理群聊成员增加 - 管理员已同意入群通知失败: {e}"
            )

    async def handle_group_increase_invite(self):
        """
        处理群聊成员增加 - 管理员邀请入群通知
        """
        try:
            pass
        except Exception as e:
            logger.error(
                f"[{MODULE_NAME}]处理群聊成员增加 - 管理员邀请入群通知失败: {e}"
            )

    async def handle_group_recall(self):
        """
        处理群聊消息撤回通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理群聊消息撤回通知失败: {e}")

    async def handle_group_upload(self):
        """
        处理群聊文件上传通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理群聊文件上传通知失败: {e}")

    # 通知事件处理
    async def handle_notify_poke(self):
        """
        处理戳一戳通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理戳一戳通知失败: {e}")

    async def handle_notify_input_status(self):
        """
        处理输入状态更新通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理输入状态更新通知失败: {e}")

    async def handle_notify_title(self):
        """
        处理群成员头衔变更通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理群成员头衔变更通知失败: {e}")

    async def handle_notify_profile_like(self):
        """
        处理点赞通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理点赞通知失败: {e}")

    # 精华消息处理
    async def handle_essence_add(self):
        """
        处理群聊设精 - 增加通知
        """
        try:
            pass
        except Exception as e:
            logger.error(f"[{MODULE_NAME}]处理群聊设精 - 增加通知失败: {e}")
