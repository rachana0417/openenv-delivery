def grade_easy(env):
    if all(env.delivered):
        if env.steps <= 10:
            return 1.0
        else:
            return 0.5
    return 0.0


def grade_medium(env):
    if all(env.delivered):
        if env.steps <= 20:
            return 1.0
        else:
            return 0.5
    return 0.0


def grade_hard(env):
    if all(env.delivered):
        if env.steps <= 30:
            return 1.0
        else:
            return 0.5
    return 0.0