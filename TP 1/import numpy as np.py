import numpy as np

L = ['rén', 'nü', 'ri', 'yuè', 'shan', 'shui', 'mu', 'macheval', 'niu', 'yang', 'yu', 'kou', 'men_porte', 'zi', 'xin', 'da_grand', 'tian', 'xiao', 'an', 'nan', 'zhong', 'zi_caractère', 'wen_langue', 'xue', 'wen_demander', 'shang', 'xia', 'qu', 'fa', 'yu', 'guo', 'wang', 'wo', 'ni', 'ta', 'men_pluriel', 'nin', 'ben', 'cha', 'mei', 'you', 'cji', 'kan', 'gong', 'zuo', 'shen', 'me', 'ma_mot_interrogatif', 'shou', 'huo', 'mi', 'che', 'dong', 'bei', 'rou', 'cai', 'jiu', 'zao', 'bi', 'xiu', 'mei', 'ming', 'xing', 'tai', 'bai', 'fan', 'hai', 'han', 'hai_enfant', 'jia', 'ma_maman', 'ba', 'dian', 'de', 'ye', 'he', 'le', 'zhe']

def f(x):
    for i in range(x):
        print(np.random.choice(L))

# Exemple d'utilisation
f(30)
