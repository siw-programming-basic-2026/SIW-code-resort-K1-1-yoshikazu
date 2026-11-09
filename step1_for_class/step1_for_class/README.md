# Python Casino：第8回 STEP 1 / Lesson 8, STEP 1

## 今回作るもの / What you will build

10×10のカジノマップにプレイヤーを表示し、名前・所持金・位置を確認できるプログラムを作ります。今回は表示までを完成させます。
Build a program that displays a player on a 10×10 casino map, along with their name, money and position. This step focuses on display.

## 学習目標 / Learning goals

- 二次元リストでマップを表す。 / Represent a map with a two-dimensional list.
- x・y座標で位置を指定する。 / Specify positions using x/y coordinates.
- 辞書からプレイヤーの情報を取り出す。 / Read player information from a dictionary.
- 関数の呼び出しとデータの流れを説明する。 / Explain function calls and the flow of data.
- 動作を確認し、Gitで変更を記録する。 / Check behavior and record changes with Git.

## 1. 作業するファイルを確認する / Find your working files

### 基本課題と発展課題 / Core and advanced exercises

| フォルダ / Folder | 内容 / Contents |
| --- | --- |
| [base_exercise/](base_exercise/README.md) | 辞書と関数で表示を完成させる基本課題 / Complete the display using dictionaries and functions |
| [adv_exercise/](adv_exercise/README.md) | 完成した基本課題をクラス化する任意の発展課題 / Optionally refactor the completed core exercise into a class |

まず基本課題に取り組み、完成したら発展課題へ進めます。
Start with the core exercise, then continue to the advanced exercise when ready.

`step1/base_exercise/` のファイルを編集します。辞書や引数を復習したいときは [STEP 0](../step0/practice.ipynb) を参照してください。
Edit the files in `step1/base_exercise/`. Review [STEP 0](../step0/practice.ipynb) if you need a refresher on dictionaries or arguments.

| ファイル / File | 役割 / Role |
| --- | --- |
| main.py | データを作り、表示関数を呼ぶ / Create data and call display functions |
| map_data.py | マップの二次元リストを作る / Create the two-dimensional map list |
| map_view.py | マップとプレイヤーを表示する / Display the map and player |
| player.py | プレイヤーの辞書を作り、情報を表示する / Create the player dictionary and display its information |

### まず実行してみる / Run the starting code

Python 3.10以上を使います。追加ライブラリは不要です。`python-casino` フォルダから次を実行してください。
Use Python 3.10 or later; no additional libraries are needed. Run this command from the `python-casino` folder:

```sh
python step1/base_exercise/main.py
```

親のGitリポジトリから実行する場合は、次のパスを使います。
If your working directory is the parent Git repository, use this path instead:

```sh
python python-casino/step1/base_exercise/main.py
```

最初はマップの2行が空行になり、プレイヤーとその情報も表示されません。これから3つのTODOを完成させます。
Initially, two map rows are blank, and neither the player nor player information appears. Complete the three TODOs below.

## 2. マップと座標を読む / Read the map and coordinates

### 記号の意味 / Map symbols

| 記号 / Symbol | 意味 / Meaning |
| --- | --- |
| # | 壁 / Wall |
| . | 通路 / Corridor |
| B | ブラックジャック / Blackjack |
| P | ポーカー / Poker |
| S | スロット / Slot |
| R | ルーレット / Roulette |
| C | ドリンク / Drink |
| F | フード / Food |
| @ | プレイヤー / Player |

### 座標の順番 / Coordinate order

左上は `(x, y) = (0, 0)` です。xは右へ、yは下へ増え、どちらも0〜9を使います。二次元リストは **`casino_map[y][x]`** の順で参照します。
The top-left cell is `(x, y) = (0, 0)`. x increases to the right and y downward; both range from 0 to 9. Access the list as **`casino_map[y][x]`**.

完成例を見て、ブラックジャック `(2, 2)` とポーカー `(5, 2)` の位置を指でたどってみましょう。
Use the expected output below to locate blackjack at `(2, 2)` and poker at `(5, 2)`.

## 3. TODOを1つずつ完成させる / Complete one TODO at a time

### TODO 1：マップを完成させる / Complete the map

`map_data.py` の空の2行を完成させてください。完成したマップは10行×10列で、外周は壁です。施設の位置は下の完成例で確認できます。
Complete the two empty rows in `map_data.py`. The finished map must have ten rows and ten columns, with walls around the border. Check the facility positions against the expected output below.

実行して、空行がなくなったか、各行が10文字になったかを確かめましょう。
Run the program and check that no rows are blank and each row has ten characters.

### TODO 2：プレイヤーを表示する / Display the player

`map_view.py` を編集し、プレイヤーの位置に `@` が表示されるようにしてください。それ以外の位置は元のマップの記号を表示します。
Edit `map_view.py` so that `@` appears at the player position. Display the original map symbols elsewhere.

初期位置は `(1, 1)` です。表示のために、元のマップの通路 `.` を書き換えないようにしましょう。
The initial position is `(1, 1)`. Display the player without overwriting the original corridor `.` in the map data.

### TODO 3：プレイヤー情報を表示する / Display player information

`player.py` の `show_player()` を実装してください。受け取った辞書の `name`・`money`・`x`・`y` を使い、完成例と同じ形式で表示します。
Implement `show_player()` in `player.py`. Use name, money, x and y from the dictionary argument to match the expected output format.

基本課題では `create_player()` はそのまま使えます。名前や所持金を変えたときも、その辞書の値が表示されるか確認しましょう。
For the core exercise, keep `create_player()` as provided. Check that changing the name or money in the dictionary changes the displayed information too.

## 4. 完成時の表示と比べる / Compare with the expected output

```text
=== Python Casino / STEP 1 ===
##########
#@.......#
#.B..P...#
#........#
#.S..R...#
#........#
#.C..F...#
#........#
#........#
##########

名前: プレイヤー
所持金: 1000
位置: x=1, y=1
```

表示ラベルは、名前＝Name、所持金＝Money、位置＝Positionです。`プレイヤー` はPlayerを意味します。表示が終わるとプログラムは終了します。
The labels mean Name, Money and Position; `プレイヤー` means Player. The program exits after displaying the output.

### 自分で確認すること / Check your work

- マップが10行×10列で、6種類の施設がある。 / The map is 10×10 and contains all six facilities.
- 初期位置 `(1, 1)` に `@` が1つ表示される。 / Exactly one @ appears at the initial position (1, 1).
- 名前・所持金・座標が辞書の値と一致する。 / The displayed name, money and coordinates match the dictionary.
- 座標を一時的に `(3, 5)` にすると、マップと情報の両方に反映される。確認後は `(1, 1)` に戻す。 / Temporarily change the position to (3, 5), check both displays, then restore (1, 1).
- 表示処理で元のマップが変更されない。 / Displaying the player leaves the original map unchanged.

### 説明してみる / Explain your implementation

`main.py` から関数の呼び出しをたどり、マップとプレイヤーの辞書がどこで作られ、どの関数へ渡されるか説明してみましょう。
Follow the function calls from `main.py` and explain where the map and player dictionary are created and which functions receive them.

## 5. Gitで進み具合を記録する / Record your progress with Git

TODOを1つ完成させて動作を確認するたびに、変更をコミットしましょう。以下は `python-casino` フォルダから実行する例です。
Commit after completing and checking each TODO. The commands below assume you are in the `python-casino` folder.

### TODO 1ができたら / After TODO 1

```sh
git diff
git add step1/base_exercise/map_data.py
git commit -m "STEP 1: Complete casino map"
```

### TODO 2ができたら / After TODO 2

```sh
git diff
git add step1/base_exercise/map_view.py
git commit -m "STEP 1: Display player on map"
```

### TODO 3ができたら / After TODO 3

```sh
git diff
git add step1/base_exercise/player.py
git commit -m "STEP 1: Display player information"
git log --oneline -3
```

親のGitリポジトリから操作する場合は、`git add` のパスの先頭に `python-casino/` を付けてください。
From the parent Git repository, prefix the paths in `git add` with `python-casino/`.

## 発展課題（任意）：初期値を引数で指定する / Optional extension: Initial values as arguments

基本課題ができたら、`create_player()` の `name`・`x`・`y`・`money` を引数で設定できるようにしてみましょう。`main.py` の呼び出しも変更し、異なる初期値で表示を確かめてください。
After finishing the core exercises, let callers set name, x, y and money through arguments to `create_player()`. Update the call in `main.py` and check the display with different initial values.

クラスを使って実装する場合も、同じ動作を満たし、呼び出し元と整合させてください。方針は [STEP 0](../step0/practice.ipynb) で確認できます。
If you implement this with classes, preserve the required behavior and keep callers consistent. See [STEP 0](../step0/practice.ipynb) for the approach.

## 次のSTEPへ / Next step

クラス化にも取り組みたい場合は、[発展課題の手順](adv_exercise/README.md)を参照してください。
To practice class refactoring, follow the [advanced exercise instructions](adv_exercise/README.md).

完成したら [STEP 2：周辺表示と移動](../step2/README.md) に進みます。
When finished, continue to [STEP 2: Neighborhood view and movement](../step2/README.md).

## コマンド処理の準備 / Preparing command handling

各演習・完成例の `commands.py` は、STEP 2に向けた空のファイル（`pass`）です。STEP 1では変更も呼び出しも不要です。
Each exercise and reference includes a placeholder `commands.py` containing `pass` for STEP 2. It does not need to be edited or called in STEP 1.

## ノートブックで実装・確認 / Implement and check in a notebook

[practice.ipynb](practice.ipynb) のセルで関数を実装し、確認してから指定の `.py` へコピーしてください。コピー後は `main.py` で全体を確認します。Pythonカーネルが必要です。
Implement functions in [practice.ipynb](practice.ipynb), check them, then copy them to the specified `.py` files. Run main.py afterward to check integration. A Python kernel is required.
