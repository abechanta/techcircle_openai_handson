import os
import argparse
import gym

def main(env_name, episode_count):
    env = gym.make(env_name)

    for _ in range(episode_count):
        observation = env.reset()
        done = False
        score = 0

        while not done:
            env.render()
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            score += reward

            if done:
                print('Episode {} end: score={}'.format(_, score))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Let's Start OpenAI Gym")
    parser.add_argument("--env", type=str, help="Name of environment", default="Pong-v0")
    parser.add_argument("--episode", type=int, help="Episode Count to work", default=2)

    args = parser.parse_args()
    main(args.env, args.episode)
