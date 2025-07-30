from crontab import CronTab

cron = CronTab(user=True)  # Should work with version 2.7.1+

cron.remove_all(comment='My daily news bot')

python_path = '/usr/local/bin/python3'
script_path = '/Users/ishanisanjel/Documents/Python/newproject.py'
log_path = '/Users/ishanisanjel/Documents/Python/cron.log'

job = cron.new(
    command=f'{python_path} {script_path} >> {log_path} 2>&1',
    comment='My daily news bot'
)

job.setall('30 7 * * *')

cron.write()

print("Cron job scheduled successfully.")
