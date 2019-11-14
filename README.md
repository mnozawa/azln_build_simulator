### つかいかた
```
./simulate.sh {試行回数} {ガチャ回す回数} {排出率*10} [{排出率*10}...]

# 目的のキャラが4名、それぞれ2%, 2%, 2.5%, 2.5%で排出されるガチャを100連した場合の試行を3000回行い、全キャラが揃った場合の数を返す

./simulate.sh 3000 100 20 20 25 25
1917
```

### TODO
- 建造結果が「アタリ」かどうかの判定 → ハズレ側から判定していくべき(大半はハズレなので)
- 全キャラ揃った時点で抜けるべき