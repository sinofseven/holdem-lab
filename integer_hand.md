- ハンドを整数値化することで、比較を容易にする
- 数値化しなければならないもの
  - ハンドのランク
  - キッカーのカード
- 数値化で大事なこと
  - ハンドのランクは支配的に作用する
  - キッカーは枚数が可変
- ハンド
  - 0〜8
  - 8はストレートフラッシュ、0はハイカード
- キッカー
  - 0〜13
  - ただし0は使用しない(0はエースの1解釈となる。ただ1解釈になるのはホイールのみであるために、このときのキッカーは4となる)
- ValueString
  - ```01122334455```
  - 解釈
    - 0: ハンドのランク
    - 11: キッカー(一番強い)
    - 22
    - 33
    - 44
    - 55: キッカー(一番弱い)