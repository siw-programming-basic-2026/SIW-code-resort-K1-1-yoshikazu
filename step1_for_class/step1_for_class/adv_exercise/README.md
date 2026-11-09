# STEP 1：発展課題 — クラス化 / Advanced exercise: Refactor into a class

## 出発点 / Starting point

このフォルダには、基本課題を完成させた辞書と関数のコードがあります。同じ表示を保ちながら、プレイヤーをクラスに置き換えてください。自分の基本課題の完成版を出発点にしても構いません。
This folder starts with working dictionary-and-function code from the core exercise. Replace the player representation with a class while preserving the displayed output. You may also start from your own completed core exercise.

## 課題 / Tasks

1. `player.py` に `Player` クラスを定義し、名前・座標・所持金をインスタンスに持たせる。初期値はコンストラクタの引数で指定できるようにする。
   Define a Player class in `player.py` with name, coordinates and money as instance attributes. Allow initial values to be passed to its constructor.
2. 情報表示をインスタンスメソッドにする。
   Implement player information display as an instance method.
3. `map_view.py` の座標の参照を、作成したクラスに合わせる。マップは二次元リストのままでよい。
   Adapt coordinate access in `map_view.py` to your class. The map may remain a two-dimensional list.
4. `main.py` でインスタンスを作り、表示処理を呼び出す。
   Create an instance in `main.py` and call the display operations.

## 実行 / Run

`python-casino` フォルダから実行します。
Run from the `python-casino` folder:

```sh
python step1/adv_exercise/main.py
```

## 確認 / Checks

初期値での出力を[STEP 1の完成例](../README.md)と比べ、名前・座標・所持金を変更して表示にも反映されることを確認してください。異なる初期値のインスタンスを2つ作り、片方の変更がもう片方に影響しないことも確かめましょう。
Compare the initial output with the [STEP 1 example](../README.md). Change the initial name, coordinates and money and check the display. Create two instances with different initial values and verify that changing one does not change the other.

辞書と関数の版から何を変更したか、データと操作をどこにまとめたかを説明してください。
Explain what changed from the dictionary-and-function version and where you grouped data and operations.
