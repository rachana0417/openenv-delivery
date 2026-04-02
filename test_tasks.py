from tasks.tasks import easy_task, medium_task, hard_task

env1 = easy_task()
print("Easy:", env1.reset())

env2 = medium_task()
print("Medium:", env2.reset())

env3 = hard_task()
print("Hard:", env3.reset())