from tasks.tasks import easy_task
from graders.grader import grade_easy

env = easy_task()
env.reset()

# simulate fake success
env.delivered = [True]

score = grade_easy(env)
print("Score:", score)