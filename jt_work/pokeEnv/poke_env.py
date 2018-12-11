import sys
import gym
import numpy as np
import gym.spaces
import poke_generator


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
        ### 使用するポケモンのセット
        self.gen = poke_generator.poke_generator()
        self.player_poke = gen.generator(445, 1) ###ガブリアス
        self.nonplayer_poke = gen.generator(9, 0) ###カメックス

        #action_space, observation_space, reward_rangeの設定
        self.action_space = gym.spaces.Discrete(4)  # 攻撃技4つ, 本来は交代2つもあるが割愛
        self.observation_space = gym.spaces.Box(0.0, 1.0, shape=2, ,dtype=np.float32) # 超簡単化のため自分のポケモンのHP,相手のポケモンのHPだけ観測できる形にする
        self.reward_range = (-1., 100.)

    def _reset(self):
        ### 対戦で使うポケモンを初期化して状態を返す
        self.player_poke = self.gen.generator(445, 1) ###ガブリアス
        self.nonplayer_poke_ = self.gen.generator(9, 0) ###カメックス
        self.done = False
        return self._make_observation()

    def _step(self,action):
        ### 技を選んだ時のダメージ計算＆状態のアップデートを行う
        ### ターンを進めるために必要な要素：先行後攻の処理＆ダメージ計算



        return self._make_observation(), reward, self.done, {}

    def _render(self, mode='human', close=False):
        ### 未実装


    def _make_observation(self):
        ### HPを削ってアップデートしたものを返す
        hp_list = []
        hp_list.append(self.player_poke.now_hp.values[0])
        hp_list.append(self.nonplayer_poke.now_hp.values[0])
        return np.concatenate(hp_list)

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
        ### シンプル化のため与えるダメージを報酬とする
        ### 相手を倒した場合が最大報酬: 1


    def _is_done(self):
        ### 2匹のHPを入力にして、どちらかが0以下なら終了する関数

    def _one_turn_step(self):
        ### 下記の関数を用いて1ターン進める

    def _check_speed(self):
        ### 素早さ判定で先行・後攻を決定

    def _first_step(self):
        ### 先行の行動

    def _second_step(self):
        ### 後攻の行動
