# Python Casino：第9回 STEP 2 / Lesson 9, STEP 2

## STEP 1からの接続 / Connection from STEP 1

STEP 1 の10×10マップとプレイヤー表示に、移動と周辺表示を追加します。  
This step extends STEP 1's 10×10 map and player display with movement and neighborhood view.

STEP 1教材: [step1_for_class/README.md](../step1_for_class/README.md)

> STEP 1でクラス版のほうが読みやすかった人は、STEP 2でもadv_exerciseに進んで構いません。  
> 辞書と関数でもクラスでも、同じ世界と移動ロジックを異なる方法で表現しています。  
> If the class version was easier to read in STEP 1, you may continue with `adv_exercise` in STEP 2.  
> Dictionary+function and class versions express the same world and movement logic in different ways.

## 今回作るもの / What you will build

- WASDで移動するプレイヤー
- 壁・範囲外への移動防止
- プレイヤー中心5×5表示
- 成功時のみturn加算
- `q` で終了、不正入力で継続

- A player that moves with WASD
- Block movement into walls/out-of-bounds
- Centered 5×5 neighborhood display
- Increment turn only on successful moves
- Quit with `q`; continue on invalid input

## 学習目標 / Learning goals

- `(dx, dy)` で座標更新を扱う
- `casino_map[y][x]` の参照順を守る
- 5×5を新しい二次元リストとして抽出する
- 失敗移動で状態を変えない条件分岐を書く
- Notebookで検証し、`.py`へ反映する

- Handle coordinate updates with `(dx, dy)`
- Respect `casino_map[y][x]` indexing order
- Extract 5×5 as a new 2D list
- Keep state unchanged on failed movement
- Validate in notebook and transfer to `.py`

## フォルダ構成 / Folder structure

```text
step2_for_class/
├── README.md
├── practice.ipynb
├── base_exercise/
│   ├── README.md
│   ├── main.py
│   ├── commands.py
│   ├── map_data.py
│   ├── map_view.py
│   └── player.py
└── adv_exercise/
    ├── README.md
    ├── main.py
    ├── commands.py
    ├── map_data.py
    ├── map_view.py
    └── player.py
```

## base_exercise と adv_exercise の違い / Difference between base and adv

- `base_exercise/`: 辞書 (`player["x"]`) と関数で実装
- `adv_exercise/`: `Player` クラス (`player.x`) を拡張

- `base_exercise/`: dictionary + functions (`player["x"]`)
- `adv_exercise/`: extends `Player` class (`player.x`)

どちらも同じマップ、同じ移動ルールです。  
Both use the same map and movement rules.

## 実行方法 / How to run

リポジトリのルートで実行:  
Run from repository root:

```sh
python step2_for_class/base_exercise/main.py
python step2_for_class/adv_exercise/main.py
```

## WASDと `(dx, dy)` の対応 / WASD to `(dx, dy)`

| 入力 / Input | 動作 / Action | (dx, dy) |
| --- | --- | --- |
| w | 上 / Up | (0, -1) |
| a | 左 / Left | (-1, 0) |
| s | 下 / Down | (0, 1) |
| d | 右 / Right | (1, 0) |
| q | 終了 / Quit | — |

`read_command()` は前後空白と大文字を吸収します（`strip().lower()`）。  
`read_command()` normalizes surrounding spaces and uppercase letters.

## `casino_map[y][x]` の説明 / About `casino_map[y][x]`

- 先に `y`（行）を選び、その中で `x`（列）を選ぶ
- 左上が `(0,0)`、右に行くと`x`増加、下に行くと`y`増加

- Select row with `y`, then column with `x`
- Top-left is `(0,0)`, x increases rightward, y downward

## 5×5の抽出方法 / How to extract 5×5

プレイヤー位置を `(px, py)` とすると、開始位置は `(px-2, py-2)`。  
`range(start, start + 5)` で5行×5列を走査します。  
マップ外は `#` で埋めます。

For player position `(px, py)`, start from `(px-2, py-2)`.  
Iterate with `range(start, start + 5)` for 5 rows and 5 columns.  
Fill out-of-map cells with `#`.

## Pythonの負の添字への注意 / Warning about negative indices

Pythonの負の添字は末尾を参照するため、`casino_map[y][x]` に触る前に `0 <= y` と `0 <= x` を必ず確認します。  
Negative indices access from the end in Python, so always check `0 <= y` and `0 <= x` before `casino_map[y][x]`.

## TODOの場所 / TODO locations

### base_exercise

1. `player.py` TODO 1: `get_move()` の `a/s/d`
2. `player.py` TODO 2: `can_move()` の壁判定
3. `map_view.py` TODO 3: `extract_view()` の `start_x/start_y`

### adv_exercise

1. `player.py` TODO 1: `Player.move()` の成功時更新
2. `map_view.py` TODO 2: `extract_view()` の `start_x/start_y`

Notebookでは `extract_view()` 全体に挑戦できます。  
`.py` 側の最低到達は開始座標TODOを完成させることです。  
In the notebook, students can implement full `extract_view()`.  
In `.py`, the minimum target is to complete the start-coordinate TODO.

## 模範出力 / Sample output

```text
=== Python Casino / STEP 2 ===
#####
#####
##@..
##.B.
##...
名前: プレイヤー
所持金: 1000
位置: x=1, y=1
ターン: 0
移動 w/a/s/d、終了 q > d
移動しました。
#####
#####
#.@..
#.B..
#....
名前: プレイヤー
所持金: 1000
位置: x=2, y=1
ターン: 1
移動 w/a/s/d、終了 q > q
終了します。
```

## 動作確認例 / Behavior checks

各行は起動し直して確認:  
Restart program for each row:

- `d → s → a → w → q`
- `w → a → q`
- `xyz → 空入力 → d → q`
- `d → s → s → q`
- `空白付きの大文字 D → Q`

## 共通の完成条件 / Shared completion criteria

TODOを完成させた状態で、base/adv の両方が次を満たすこと:

- 初期位置 `(1,1)`、初期turn `0`
- `d` 後に `(2,1)`、turn `1`
- 初期位置から `w` と `a` は壁で失敗
- 不正入力で座標・turn不変
- 施設マスへ移動可能
- 常に5×5表示、プレイヤーは表示上の中央 `[2][2]`
- マップ外は `#` 埋め
- 元の10×10マップ不変
- 大文字入力・前後空白を処理
- `q` で正常終了

## Gitでの記録方法 / Recording with Git

リポジトリルートで実行:

```sh
git diff
git add step2_for_class/base_exercise
git commit -m "STEP 2: Add movement and neighborhood exercises"

git diff
git add step2_for_class/adv_exercise
git commit -m "STEP 2: Add Player class exercise"

git diff
git add step2_for_class/README.md step2_for_class/practice.ipynb
git commit -m "STEP 2: Add bilingual practice notebook and README"
```

`__pycache__` と `.ipynb_checkpoints` はコミットしません。  
Do not commit `__pycache__` or `.ipynb_checkpoints`.

## 完成条件（提出時） / Done definition

- base/adv のTODO位置が明確
- Notebookの確認セルが想定解で通る
- READMEのコマンド・パスが現リポジトリと一致
- `git diff` に意図しない変更がない
