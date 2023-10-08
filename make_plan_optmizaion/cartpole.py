import gym
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = []
        self.gamma = 0.95  # Discount factor
        self.epsilon = 1.0  # Exploration rate
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01
        self.learning_rate = 0.001
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return np.random.choice(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])

    def replay(self, batch_size):
        minibatch = np.array(random.sample(self.memory, batch_size))
        states = np.vstack(minibatch[:, 0])
        actions = np.array(minibatch[:, 1], dtype=int)
        rewards = np.array(minibatch[:, 2], dtype=float)
        next_states = np.vstack(minibatch[:, 3])
        dones = np.array(minibatch[:, 4], dtype=bool)
        
        targets = rewards + self.gamma * np.max(self.model.predict(next_states), axis=1) * ~dones
        target_f = self.model.predict(states)
        target_f[range(batch_size), actions] = targets
        
        self.model.fit(states, target_f, epochs=1, verbose=0)
        
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

# 환경 설정
env = gym.make('CartPole-v1')
state_size = env.observation_space.shape[0]
action_size = env.action_space.n
batch_size = 32
episodes = 1000

# DQN 에이전트 초기화
agent = DQNAgent(state_size, action_size)

# 학습 루프
for episode in range(episodes):
    state = env.reset()
    state = np.reshape(state, [1, state_size])

    for t in range(500):
        # 행동 선택
        action = agent.act(state)

        # 환경에서 행동 수행 후 다음 상태, 보상, 종료 여부 받아옴
        next_state, reward, done, _ = env.step(action)
        next_state = np.reshape(next_state, [1, state_size])

        # 에피소드 기억
        agent.remember(state, action, reward, next_state, done)

        # 다음 상태로 이동
        state = next_state

        if done:
            break

    # 학습
    if len(agent.memory) > batch_size:
        agent.replay(batch_size)

    # 에피소드마다 학습 결과 출력
    print("Episode: {}/{}, Score: {}".format(episode+1, episodes, t+1))

    # 태스크가 해결되면 학습 중단
    if t == 499:
        print("Task Solved!")
        break

# 학습된 모델 저장
agent.model.save("dqn_model.h5")
