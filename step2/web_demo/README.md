# STEP 2 Webデモ / Web Demo

Python版を実装した後に使う、完成済みの比較・観察教材です。必須の実装課題ではありません。PythonとJavaScriptで共通するデータ・判定・状態更新を探してください。

This completed demo is for comparison after implementing the Python version. It is not a required implementation task. Look for shared data structures, movement checks, and state updates.

## 起動と操作 / Run and control

`index.html`をブラウザで開きます。サーバー・インストール・ビルド・外部ライブラリは不要です。4ファイルを同じフォルダに置いてください。

Open `index.html` in a browser. No server, installation, build, or external libraries are needed. Keep all four files in the same folder.

- W / ↑：上 / Up、A / ←：左 / Left、S / ↓：下 / Down、D / →：右 / Right
- 画面上の方向ボタンでも移動できます。 / The direction buttons also move the player.
- 「最初から」で位置とターンを初期化します。 / Reset restores the initial position and turn.

## Python版との対応 / Python and Web

| Python CLI版 / Python CLI | Web版 / Web |
| --- | --- |
| `input()` | `keydown`イベント・ボタン / Events and buttons |
| `print()` | HTMLの更新 / HTML updates |
| 二次元リスト / 2D list | JavaScriptの二次元配列 / 2D array |
| 辞書・Playerクラス / Dictionary or Player class | JavaScriptのオブジェクト / Object |
| 移動関数 / Movement function | `movePlayer()` |
| ターミナル / Terminal | ブラウザ / Browser |

基本版と発展版は同じマップと移動ルールを使います。Web版も初期位置`(1, 1)`、`turn = 0`です。施設のマスには移動できますが、施設のゲーム処理はありません。Python版は周辺5×5を表示し、Web版は比較しやすい全体10×10を表示します。

Both Python exercises use the same map and movement rules. The Web version also starts at `(1, 1)` with `turn = 0`. Facility cells are walkable; facility games are not implemented. Python shows a local 5×5 view, while this demo shows the full 10×10 map for comparison.

## 観察するポイント / Things to observe

1. 方向入力が`(dx, dy)`へ変換され、次の座標が計算されます。 / Input becomes `(dx, dy)`, then the next position is calculated.
2. `casinoMap[y][x]`を参照する前に範囲を確認し、壁を判定します。 / Bounds are checked before indexing `casinoMap[y][x]`, then walls are checked.
3. 壁に向かって移動しても座標とターンは変わりません。通路・施設への移動成功時だけターンが増えます。 / Failed moves preserve position and turn; successful moves onto paths or facilities increment the turn.
4. 外周は壁なので通常操作では範囲外に到達しません。コードには範囲外の判定もあります。 / Border walls prevent reaching out-of-bounds positions through normal controls; the code still checks bounds.
5. `movePlayer()`は状態更新、`renderMap()`と`renderStatus()`は表示を担当します。 / State changes happen in `movePlayer()`; rendering happens in `renderMap()` and `renderStatus()`.

> 世界の中身と、世界の見せ方は分けて考えられる。
> Separate the world’s state from the way it is presented.
