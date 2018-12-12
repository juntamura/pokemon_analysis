import sys
import gym
import numpy as np
import gym.spaces
import json
import random
from poke_generator import generator, param_cal

### 別途用意しておくもの
# ポケモンマスタ: https://github.com/kotofurumiya/pokemon_dataからjsonデータを拝借し加工
# 技マスタ: 自前で用意
# タイプ相性マスタ: 自前で用意
# 性格マスタ: poke_generatorの中に一部の性格のみ記載

class poke_env(gym.env):
    ### 最大10ターンで対戦を終える、終わらなかったら引き分け扱い
    MAXSTEPS = 10

    def __init__(self):
        ### 使用するポケモンのセット
        self.player_poke = generator(445, 1) ###ガブリアス
        self.nonplayer_poke = generator(9, 0) ###カメックス

        ### 技マスタ・タイプ相性マスタを読み込み(自前で作成)
        f_w = open('weapon_master.json', 'r')
        self.weapon_master = json.loads(f_w)
        f_w.close()

        f_ty = open('type_match_dict.json', 'r')
        self.type_match_dict = json.loads(f_ty)
        f_ty.close()

        #action_space, observation_space, reward_rangeの設定
        self.action_space = gym.spaces.Discrete(4)  # 攻撃技4つ, 本来は交代2つもあるが割愛
        self.observation_space = gym.spaces.Box(0.0, 1.0, shape=2, ,dtype=np.float32) # 超簡単化のため自分のポケモンのHP,相手のポケモンのHPだけ観測できる形にする
        self.reward_range = (-1., 100.)

    def _reset(self):
        ### 対戦で使うポケモンを初期化して状態を返す
        self.player_poke = generator(445, 1) ###ガブリアス
        self.nonplayer_poke_ = generator(9, 0) ###カメックス
        self.done = False
        return self._make_observation()

    def _step(self, action):
        ### 技を選んだ時のダメージ計算＆状態のアップデートを行う
        ### ターンを進めるために必要な要素：先行後攻の処理＆ダメージ計算

        ### 相手のactionを決定（ランダム）
        enemy_action = random.choise([0,1,2,3])

        ### 先行後攻の決定
        first_attack_flg = self._check_speed()



        ### 報酬の計算
        reward = self._get_reward
        self.total_reward =+ reward

        ### 終了判定
        self.done = self._is_done()

        return self._make_observation(), reward, self.done, {}

    def _render(self, mode='human', close=False):
        ### 未実装


    def _make_observation(self):
        ### 現在HPをリストにして返す
        hp_list = []
        hp_list.append(self.player_poke.now_hp.values[0])
        hp_list.append(self.nonplayer_poke.now_hp.values[0])
        return np.concatenate(hp_list)

    def _cal_damage(self, att, def):
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
        if hp_list.append(self.player_poke.now_hp.values[0]) <= 0 or hp_list.append(self.nonplayer_poke.now_hp.values[0]) <= 0:
            return True
        else:
            return False

    def _check_speed(self):
        ### 素早さ判定で先行・後攻を決定、同速の場合は自プレイヤー有利とする
        if self.player_poke.s_j.values[0] >= self.nonplayer_poke.s_j.values[0]:
            first_attack_flg = 1
        else:
            first_attack_flg = 0
        return first_attack_flg

    def _one_turn_step(self, first_attack_flg):
        ### 下記の関数を用いて1ターン進める

    def _first_step(self):
        ### 先行の行動

    def _second_step(self):
        ### 後攻の行動
