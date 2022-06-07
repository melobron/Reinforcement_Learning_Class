import argparse

from chain_mdp import ChainMDP
# from agent_chainMDP import DQNAgent


# Arguments
parser = argparse.ArgumentParser(description='DQN')

parser.add_argument("--gpu_num", type=int, default=0, help='gpu number')
parser.add_argument("--random_seed", type=int, default=100, help='pytorch random seed')

# Evaluation Parameters
parser.add_argument("--eval_episodes", type=int, default=1, help='number of evaluation episodes')

# Training Parameters
parser.add_argument("--batch_size", type=int, default=128, help='batch size')
parser.add_argument("--lr", type=float, default=0.01, help='learning rate')
parser.add_argument("--n_episodes", type=int, default=10, help='number of episodes')
parser.add_argument("--target_update", type=int, default=10, help='episode size of target update')
parser.add_argument("--gamma", type=float, default=0.999, help='gamma factor for q learning')

# Action Parameters
parser.add_argument("--eps_start", type=int, default=0.9, help='epsilon at start')
parser.add_argument("--eps_end", type=int, default=0.05, help='epsilon at end')
parser.add_argument("--eps_decay", type=int, default=200, help='epsilon decay')
parser.add_argument("--n_actions", type=int, default=2, help='size of action space')

args = parser.parse_args()

# Environment
env = ChainMDP(n=10)
state_size = env.n
action_size = env.action_space.n

# # Agent
# agent = DQNAgent()

# Evaluation
for _ in range(args.eval_episodes):
    s = env.reset()

    done = False
    cum_reward = 0.0

    while not done:
        action = agent.action()
        ns, reward, done, _ = env.step(action)

        cum_reward += reward

    print(f"total reward: {cum_reward}")
