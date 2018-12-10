import pandas as pd
import math
### battle_poke['h_j'] = h_jの部分でCopyが云々のWarningが出るのでいったん無視する
pd.options.mode.chained_assignment = None

### 図鑑番号を指定して対象のポケモンの種族値やタイプ情報を取得する
### 努力値振りは簡単化のためにHA252,B4 or HC252, D4のみ
### 性格は意地っ張り or 控えめのみ
### ACの種族値が同じ場合は意地HA252に寄せてしまう
### 今後詳細化できるポイント
class poke_generator:
    def generator(self, no):
        main_df = pd.read_csv('../pokemon_zukan_rm_MegaEvo.csv')
        battle_poke = main_df.query("no == @no")
        #print(battle_poke['attack'], battle_poke['sp_attack'])
        if battle_poke.attack.values[0] >= battle_poke.sp_attack.values[0]:
            h_j, a_j, b_j, c_j, d_j, s_j = poke_generator.param_cal(self
                                                    ,battle_poke['hp']
                                                    ,battle_poke['attack']
                                                    ,battle_poke['defence']
                                                    ,battle_poke['sp_attack']
                                                    ,battle_poke['sp_defence']
                                                    ,battle_poke['speed']
                                                    ,252, 252, 4, 0, 0, 0, 0)
        elif battle_poke.attack.values[0] < battle_poke.sp_attack.values[0]:
            h_j, a_j, b_j, c_j, d_j, s_j = poke_generator.param_cal(self
                                                    ,battle_poke['hp']
                                                    ,battle_poke['attack']
                                                    ,battle_poke['defence']
                                                    ,battle_poke['sp_attack']
                                                    ,battle_poke['sp_defence']
                                                    ,battle_poke['speed']
                                                    ,252, 0, 0, 252, 4, 0, 1)

        battle_poke['h_j'] = h_j
        battle_poke['a_j'] = a_j
        battle_poke['b_j'] = b_j
        battle_poke['c_j'] = c_j
        battle_poke['d_j'] = d_j
        battle_poke['s_j'] = s_j
        return battle_poke

    def param_cal(self, h,a,b,c,d,s,h_d,a_d,b_d,c_d,d_d,s_d,personal):
        ### 本来的には性格に対するパラメータ補正値を辞書とかで持たせておけば良い気もするが、今回そこまで種類を用意しないのでゴリ押し
        if personal == 0: ##意地っ張り
            a_hosei = 1.1
            b_hosei = 1
            c_hosei = 0.9
            d_hosei = 1
            s_hosei = 1
        elif personal == 1: ## 控えめ
            a_hosei = 0.9
            b_hosei = 1
            c_hosei = 1.1
            d_hosei = 1
            s_hosei = 1
        elif personal == 2: ##勇敢
            a_hosei = 1.1
            b_hosei = 1
            c_hosei = 1
            d_hosei = 1
            s_hosei = 0.9
        elif personal == 3: ## 冷静
            a_hosei = 1
            b_hosei = 1
            c_hosei = 1.1
            d_hosei = 1
            s_hosei = 0.9
        else: ### その他のケース
            a_hosei = 1
            b_hosei = 1
            c_hosei = 1
            d_hosei = 1
            s_hosei = 1

        h_j = math.floor((h + 31/2 + h_d/8)+60)
        a_j = math.floor(((a + 31/2 + a_d/8)+5)*a_hosei)
        b_j = math.floor(((b + 31/2 + b_d/8)+5)*b_hosei)
        c_j = math.floor(((c + 31/2 + c_d/8)+5)*c_hosei)
        d_j = math.floor(((d + 31/2 + d_d/8)+5)*d_hosei)
        s_j = math.floor(((s + 31/2 + s_d/8)+5)*s_hosei)

        return h_j, a_j, b_j, c_j, d_j, s_j

if __name__ == '__main__':
    tmp = poke_generator()
    tmp_return = tmp.generator(445) ### ガブリアスのパラメータでテスト
    print(tmp_return)
#      no   name type1 type2   hp  attack  defence  sp_attack  sp_defence  \
#442  445  ガブリアス  ドラゴン   じめん  108     130       95         80          85
#     speed  h_j  a_j  b_j  c_j  d_j  s_j
#442    102  215  200  116   90  105  122
