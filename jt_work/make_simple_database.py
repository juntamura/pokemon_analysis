import pandas as pd
import numpy as np
import json
import math
pd.options.mode.chained_assignment = None

### 元データのインポート
f = open("pokemon_data.json", 'r')
data_j = json.load(f)
data_df = pd.DataFrame(data_j)

### メガ進化やフォームチェンジをいったん除外
### この仕様でボルトルネなどが図鑑から消失、すまぬ
data_df_rm_MegaEvo = data_df.query("isMegaEvolution == False and form == '' ")

### type情報をparseして２列に持たせ直す
data_df_rm_MegaEvo['type1'] = data_df_rm_MegaEvo['types'].apply(lambda x: x[0])
data_df_rm_MegaEvo['type2'] = data_df_rm_MegaEvo['types'].apply(lambda x: x[1])

### 種族値情報をparseして参照しやすい形にする
data_df_rm_MegaEvo['hp'] = data_df_rm_MegaEvo['stats'].apply(lambda x : x['hp'])
data_df_rm_MegaEvo['attack'] = data_df_rm_MegaEvo['stats'].apply(lambda x : x['attack'])
data_df_rm_MegaEvo['defence'] = data_df_rm_MegaEvo['stats'].apply(lambda x : x['defence'])
data_df_rm_MegaEvo['sp_attack'] = data_df_rm_MegaEvo['stats'].apply(lambda x : x['spAttack'])
data_df_rm_MegaEvo['sp_defence'] = data_df_rm_MegaEvo['stats'].apply(lambda x : x['spDefence'])
data_df_rm_MegaEvo['speed'] = data_df_rm_MegaEvo['stats'].apply(lambda x : x['speed'])

### 必要なカラムだけ抽出
new_data_df_zukan = data_df_rm_MegaEvo.loc[:,['no','name','type1','type2', 'hp', 'attack', 'defence', 'sp_attack', 'sp_defence', 'speed']]

### タイプを英語表記に変更
replace_dict =  {
    'ノーマル' : 'NORMAL'
    ,'ほのお' : 'FIRE'
    ,'みず' : 'WATER'
    ,'でんき' : 'ELECTR'
    ,'くさ' : 'GRASS'
    ,'こおり' : 'ICE'
    ,'かくとう' : 'FIGHT'
    ,'どく' : 'POISON'
    , 'じめん' : 'GROUND'
    ,'ひこう' : 'FLYING'
    ,'エスパー' : 'PSYCHC'
    ,'むし' : 'BUG'
    ,'いわ' : 'ROCK'
    ,'ゴースト' : 'GHOST'
    ,'ドラゴン' : 'DRAGON'
    ,'あく' : 'DARK'
    ,'はがね' : 'STEEL'
    ,'フェアリー' : 'FAIRY'}

new_data_df_zukan = new_data_df_zukan.replace(replace_dict)

### 保存
new_data_df_zukan.to_csv('pokemon_zukan_rm_MegaEvo.csv', index=False)
