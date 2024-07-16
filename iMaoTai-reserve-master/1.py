import datetime
import random

# 获取当前日期（如果你只需要时间部分，日期可以是任意的）
now = datetime.datetime.now()

# 设置时间范围为早上9点到9点45分
start_time = datetime.time(9, 0)
end_time = datetime.time(9, 45)

# 生成一个随机的分钟数，从0到45（包含0和45）
random_minutes = random.randint(0, 45)

# 使用随机生成的分钟数和固定的小时数（9）来创建一个时间对象
random_time = datetime.time(9, random_minutes)

# 如果需要的话，可以将这个时间和当前日期（或任意日期）结合起来
# 注意：这里我们假设我们不需要特定的日期，只需要时间
# random_datetime = datetime.datetime.combine(now.date(), random_time)

# 打印结果
print(random_time)