import sys
import gym
import numpy as np
import gym.spaces


### 別途用意しておくもの
# ポケモンマスタ
# 技マスタ
# タイプ相性マスタ
# 性格マスタ
### 別途書いたものはあるので、それを反映させればなんとか、、、
### この環境限定で使えるようにこの中に書いてしまうか、、、

class poke_env(gym.env):
    ### 最大10ターンで対戦を終える、終わらなかったら引き分け扱い
    MAXSTEPS = 10

    def __init__(self):
        super().__init__()
        #action_space, observation_space, reward_rangeの設定する
        self.action_space = gym.spaces.Discrete(4)  # 攻撃技4つ
        self.observation_space = gym.spaces.Box(0.0, 1.0, shape=2, ,dtype=np.float32) # 超簡単化のため自分のポケモンのHP,相手のポケモンのHPだけ観測できる形にする
        self.reward_range = (-1.0, 1.0)

    def _step(self,action):
        ### 技を選んだ時のダメージ計算＆状態のアップデートを行う
        ### これはエージェント視点でのstepだから自分を中心
        ### 相手ターンのstepも記載する必要がある
        ### ターンを進めるために必要な要素：先行後攻の処理＆ダメージ計算
        action == 1


    def _render(self, mode='human', close=False):
        ### とりあえずログが吐ければいいが、いったん吐けなくてもいい


    def _make_observation(self):
        ### HPを削ってアップデートする


    def _cal_damage(self):
        # 物理と特殊の判断、物理技なら攻撃・防御、特殊技ならとくこう・とくぼうで計算
        if A_spA == 'A':
            a_param = a_a
            d_param = d_b
        else:
            a_param = a_c
            d_param = d_d
        
        type_aisyou = 1 ### 技タイプとポケモンタイプを照らし合わせて係数算出、一旦１としている

        dam = math.floor(50 * 2 / 5 + 2) * math.floor(a_param*wep / d_param) * type_aisyou / 50 + 2
        if wep_type == poketype: ### タイプ一致の処理
            dam = math.floor(dam * 1.5)
        else:
            dam = dam
        
        return dam
        ### ここで計算した値をそのまま報酬に使う、正規化はいれよう、1024で割る？
        ### 倒す＝最大報酬にする


    def _get_reward(self):
        ### 削ったHPに応じて報酬を計算
        ### 与えるダメージを報酬とするのがシンプルかも


    def _is_done(self):
        ### 2匹のHPを入力にして、どっちかが0以下なら終了する関数
