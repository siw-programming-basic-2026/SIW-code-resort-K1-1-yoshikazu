# STEP 2：発展課題 — Playerクラスで移動を追加 / Advanced exercise: Add movement with the Player class

## 出発点 / Starting point

このフォルダは、STEP 1 の `Player` クラスを引き継いで、STEP 2 の移動処理を追加する課題です。
辞書版と同じ世界・同じ移動ロジックを、クラスで表現します。

This folder extends the STEP 1 `Player` class with STEP 2 movement features.
It represents the same world and movement logic as the dictionary version, but with a class.

## 課題 / Tasks

1. `player.py` の **TODO 1** で `Player.move()` を完成させる。  
   移動成功時だけ `x`・`y`・`turn` を更新する。
2. `map_view.py` の **TODO 2** で `extract_view()` の開始座標を完成させる。  
   5×5表示の中央 `[2][2]` がプレイヤー位置になるようにする。

## 実行 / Run

このフォルダで次を実行します。

```sh
python main.py
```

## 確認 / Checks

- `q` で終了できる
- 不正入力で終了しない
- TODO完成後、壁・範囲外を拒否し、施設には移動できる
- TODO完成後、移動成功時だけ `turn` が増える
- TODO完成後、常に5×5表示で中央 `[2][2]` が `@`

## English summary

This exercise is for students who want to continue with the class-based design from STEP 1.
It is not a separate world, only a different expression of the same movement rules.
