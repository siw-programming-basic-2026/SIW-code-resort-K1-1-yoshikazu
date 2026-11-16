"use strict";

// Python版と同じ二次元データ。参照順は [y][x]。 / Same map as Python; index with [y][x].
const casinoMap = [
  "##########",
  "#........#",
  "#.B..P...#",
  "#........#",
  "#.S..R...#",
  "#........#",
  "#.C..F...#",
  "#........#",
  "#........#",
  "##########",
].map((row) => row.split(""));

const player = { x: 1, y: 1, turn: 0 };
const directions = { w: [0, -1], a: [-1, 0], s: [0, 1], d: [1, 0] };
const arrowKeys = { ArrowUp: "w", ArrowLeft: "a", ArrowDown: "s", ArrowRight: "d" };
let lastAction = "移動してみましょう。 / Try moving.";

function canMove(nextX, nextY) {
  // 負の座標も配列参照の前に確認する。 / Check bounds before accessing the array.
  if (nextY < 0 || nextY >= casinoMap.length || nextX < 0 || nextX >= casinoMap[nextY].length) {
    return { allowed: false, reason: "マップの範囲外です。 / Outside the map." };
  }
  if (casinoMap[nextY][nextX] === "#") {
    return { allowed: false, reason: "壁があるため移動できません。 / A wall blocks the way." };
  }
  return { allowed: true };
}

function movePlayer(dx, dy) {
  const nextX = player.x + dx;
  const nextY = player.y + dy;
  const result = canMove(nextX, nextY);
  // 成功時だけ状態を更新する。 / Update state only after a successful move.
  if (result.allowed && (dx !== 0 || dy !== 0)) {
    player.x = nextX;
    player.y = nextY;
    player.turn += 1;
    lastAction = `(${nextX}, ${nextY}) へ移動しました。 / Moved to (${nextX}, ${nextY}).`;
  } else {
    lastAction = result.reason || "移動していません。 / No movement.";
  }
  renderMap();
  renderStatus();
}

function renderMap() {
  const map = document.getElementById("map");
  const cells = document.createDocumentFragment();
  casinoMap.forEach((row, y) => {
    row.forEach((symbol, x) => {
      const cell = document.createElement("span");
      const isPlayer = x === player.x && y === player.y;
      const kind = symbol === "#" ? "wall" : symbol === "." ? "path" : "facility";
      cell.className = `cell ${kind}${isPlayer ? " player" : ""}`;
      cell.textContent = isPlayer ? "@" : symbol === "." ? "·" : symbol;
      cell.title = `(${x}, ${y}) ${isPlayer ? "プレイヤー / Player" : symbol}`;
      cell.setAttribute("aria-hidden", "true");
      cells.appendChild(cell);
    });
  });
  map.replaceChildren(cells);
  map.setAttribute("aria-label", `10×10マップ、プレイヤー位置 / Player position: (${player.x}, ${player.y}). # 壁 / Wall, B P S R C F 施設 / Facilities.`);
}

function renderStatus() {
  document.getElementById("player-x").textContent = player.x;
  document.getElementById("player-y").textContent = player.y;
  document.getElementById("player-turn").textContent = player.turn;
  document.getElementById("last-action").textContent = lastAction;
}

function handleDirection(command) {
  if (Object.hasOwn(directions, command)) {
    movePlayer(...directions[command]);
  }
}

// キーとボタンは同じ方向データを使う。 / Keys and buttons share the same direction data.
document.addEventListener("keydown", (event) => {
  if (event.ctrlKey || event.altKey || event.metaKey || event.isComposing) return;
  if (event.target instanceof HTMLElement && event.target.matches("input, textarea, select, [contenteditable]")) return;
  const command = Object.hasOwn(arrowKeys, event.key) ? arrowKeys[event.key] : event.key.toLowerCase();
  if (Object.hasOwn(directions, command)) {
    event.preventDefault();
    handleDirection(command);
  }
});

document.querySelectorAll("[data-direction]").forEach((button) => {
  button.addEventListener("click", () => handleDirection(button.dataset.direction));
});

document.getElementById("reset").addEventListener("click", () => {
  Object.assign(player, { x: 1, y: 1, turn: 0 });
  lastAction = "初期状態に戻しました。 / Reset to the initial state.";
  renderMap();
  renderStatus();
});

renderMap();
renderStatus();
