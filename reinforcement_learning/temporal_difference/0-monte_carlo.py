#!/usr/bin/env python3
"""Performs the Monte Carlo algorithm"""
import numpy as np


def monte_carlo(env, V, policy, episodes=5000, max_steps=100,
                 alpha=0.1, gamma=0.9):
    """
    Performs the Monte Carlo algorithm

    env: environment instance
    V: numpy.ndarray of shape (s,) containing the value estimate
    policy: function that takes in a state and returns the next
            action to take
    episodes: total number of episodes to train over
    max_steps: maximum number of steps per episode
    alpha: learning rate
    gamma: discount rate

    Returns: V, the updated value estimate
    """
    for ep in range(episodes):
        state, _ = env.reset()
        episode = []

        for step in range(max_steps):
            action = policy(state)
            next_state, reward, terminated, truncated, info = env.step(
                action)
            episode.append((state, reward))
            state = next_state

            if terminated or truncated:
                break

        episode = np.array(episode, dtype=int)
        visited = set()

        for i, (state, _) in enumerate(episode):
            if state not in visited:
                visited.add(state)
                discounts = np.array(
                    [gamma ** j for j in range(len(episode[i:]))])
                G = np.sum(episode[i:, 1] * discounts)
                V[state] = V[state] + alpha * (G - V[state])

    return V
