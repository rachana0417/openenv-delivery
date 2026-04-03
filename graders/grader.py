def grade(env):
    """
    Returns a score between 0.0 and 1.0
    based on delivery success and efficiency
    """

    # Get environment state
    state = env.state()

    delivered = state.get("delivered", [False])
    steps = state.get("steps", 1)

    # Check if all deliveries are done
    success = all(delivered)

    if not success:
        return 0.0

    # Efficiency scoring (fewer steps = higher score)
    max_steps = 50  # you can adjust
    score = max(0.0, 1.0 - (steps / max_steps))

    return round(score, 2)