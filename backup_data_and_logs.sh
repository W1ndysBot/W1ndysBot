#!/bin/bash

# 进入/home/bot/app目录
cd /home/bot/app || {
    echo "/home/bot/app 目录不存在或无法访问"
    exit 1
}

# 检查data和logs目录是否存在
if [ ! -d "data" ] || [ ! -d "logs" ]; then
    echo "data 或 logs 目录不存在"
    exit 1
fi

# 获取当前日期
current_date=$(date +%Y%m%d)

# 定义压缩文件名
archive_name="backup.tar.gz"

# 打包data和logs目录
tar -czvf $archive_name data logs

# 输出打包结果
if [ $? -eq 0 ]; then
    echo "打包成功: $archive_name"
    # 返回上一级目录
    cd ..
    # 运行当前目录下的 Python 文件
    python3 backup_data_and_logs_success_info_report.py
else
    echo "打包失败"
fi
