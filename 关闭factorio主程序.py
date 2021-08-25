import os
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

# 输入模块
print('Hi，欢迎来到定时关闭程序的模块')
print("请输入想要关闭的程序名称（加上.exe）")
print("默认值为“Factorio.exe”")
Program = input() or "Factorio.exe"


# 关闭程序的模块
def Program_killer():
    def end_program(pro_name):
        Program_killer_Result = os.system('%s%s' % ("taskkill /F /IM ", pro_name))
        if Program_killer_Result == 1:
            print(Program,"已经成功关闭，感谢您的使用")
    end_program(Program)  ######为了测试方便先用cmd代替factorio


# 定时关闭程序的模块
def main():
    h = eval(input('你想要在几点钟停止程序（24小时制）'))
    m = eval(input('你想要在哪分钟停止程序'))
    sched = BlockingScheduler()
    # 每天固定时间开始任务
    c1 = CronTrigger(day_of_week='0-6', hour=h, minute=m)
    sched.add_job(Program_killer, c1, day_of_week='0-6', hour=h, minute=m)
    # h为开始任务的小时，m为开始任务的分钟，需要在前面的输入模块自定义
    sched.start()
main()
