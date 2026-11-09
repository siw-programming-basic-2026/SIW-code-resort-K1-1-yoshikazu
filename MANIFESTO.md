# 生成AIを使う前に整えておくべき土台 / Foundations before using generative AI

## 後期「プログラミング基礎」後半で大切にすること / Priorities for the latter half of second-semester Programming Fundamentals

後期「プログラミング基礎」後半では、これまでの授業で学んだ知識や実装経験をつなげ、今あるコードを読み、自分で処理を考え、実行結果を確かめ、間違いを直す力をさらに固めます。完成したファイルを手に入れることだけが目標ではありません。自分のコードについて「なぜ動くのか」「どこを直すのか」を説明できることを目指します。
The latter half of second-semester Programming Fundamentals connects the knowledge and implementation experience you have gained in earlier lessons, strengthening your ability to read existing code, design logic, check results and fix mistakes. Obtaining completed files is only part of the goal. You should be able to explain why your code works and where it needs changing.

## 1. コードを丁寧に読む / Read code carefully

辞書に項目が多く、関数が複数のファイルに分かれていると、最初は複雑に見えます。一度に全部を理解しようとせず、具体的な値を1つ選んで追ってください。
A dictionary with many fields and functions spread across files can look complicated at first. Choose one concrete value and trace it instead of trying to understand everything at once.

- この辞書には、どんなキーと値が入っているか。 / Which keys and values does this dictionary contain?
- この関数には何が渡され、何が返るか。 / What does this function receive and return?
- 呼び出し元は、その結果をどう使うか。 / How does the caller use the result?

## 2. 値が作られ、変わる順番を追う / Trace when values are created and changed

変数の意味は、名前を見るだけでは分からないことがあります。どこで定義され、どの順で関数に渡され、いつ更新されるかをたどりましょう。関数がファイルに書かれた順番と、実行される順番は同じとは限りません。
A variable's name may not tell you enough. Trace where it is defined, how it passes through functions and when it changes. The order of function definitions in a file is not necessarily their execution order.

紙に値を書いたり、必要な場所に一時的な `print()` を置いたりして構いません。辞書なら、処理の前後でどの項目が変わったかを比べてください。
Write values on paper or temporarily add print() where needed. For dictionaries, compare the entries before and after an operation.

## 3. 実行する前に予想する / Predict before running

「動いた」だけで終わらず、先に結果を予想してください。普通の入力だけでなく、所持金が価格と同じ場合、壁へ進む場合、範囲外の座標なども考えます。予想と実際が違った場所が、次に調べる手がかりです。
Before running code, predict its result. Consider ordinary inputs as well as exact funds, movement into a wall and out-of-bounds coordinates. A difference between your prediction and the actual result tells you where to investigate next.

## 4. 自分でロジックを組む / Build the logic yourself

求める動作を、小さな判断と更新に分けてください。たとえば購入なら「所持金を確認する」「回復後の値を求める」「辞書を更新する」という仕事があります。どの順で行い、失敗したとき何を変更しないかを、自分で考えます。
Break required behavior into small decisions and updates. A purchase involves checking funds, calculating recovery and updating the dictionary. Work out the order and which values must remain unchanged on failure.

辞書と関数でも、クラスでも構いません。自分が選んだ構成でデータと処理がどうつながるかを説明できることが大切です。
You may use dictionaries and functions or classes. What matters is explaining how data and operations connect in your chosen design.

## 5. 悩む時間を飛ばさない / Do not skip the time spent figuring things out

コードを行き来し、値の流れを追い、予想が外れた理由を考える時間も学習の一部です。すぐに答えが出なくても、その時間を無駄だと考える必要はありません。
Moving between files, tracing values and investigating a wrong prediction are part of learning. Time spent without an immediate answer is not necessarily wasted.

ただし、同じ画面を見続けるだけで抱え込む必要はありません。「何をしたかったか」「どこまで分かったか」「何を試したか」を整理して質問してください。教員や仲間と確認しながら、自分で考える過程を続けましょう。
You do not have to struggle alone while staring at the same screen. Ask for help by explaining your goal, what you understand and what you tried. Work with your teacher and classmates while continuing to reason for yourself.

## 6. 後期「プログラミング基礎」後半での生成AIの扱い / Generative AI in the latter half of second-semester Programming Fundamentals

後期「プログラミング基礎」後半のコード読解・実装練習・確認問題・振り返りでは、生成AIを使わずに取り組んでください。解答や実装、原因の説明を先に生成してもらうと、自分で読み、考え、確かめる機会を飛ばしてしまいます。生成AIによるコード補完や、振り返りの作成・書き換え・翻訳も含みます。
Work on code reading, implementation practice, checks and reflections in this part of the course without generative AI. Having answers, implementations or explanations generated first can bypass the opportunity to read, reason and verify for yourself. This includes generative code completion and generating, rewriting or translating reflections.

配布教材、公式ドキュメント、辞書、教員や仲間への相談は活用してください。相談後も、自分で動作を確認し、説明できるようにしましょう。
Use the provided materials, official documentation, dictionaries and help from your teacher or classmates. After receiving help, check the behavior yourself and make sure you can explain it.

## 7. 自分の言葉で残す / Record your own experience

振り返りは日本語・英語・母国語のいずれでも構いません。短い文や箇条書きでも大丈夫です。実際に試したこと、分かったこと、今後工夫したいことを具体的に書いてください。文法や綴りの正確さは採点対象にしません。
Reflections may be written in Japanese, English or your native language. Short sentences or bullet points are welcome. Describe what you actually tried, what you learned and what you would like to improve. Grammar and spelling accuracy are not graded.

学生本人の考えを確認するため、振り返りにも生成AIを使わないでください。教員は、母国語で提出された文章の内容を理解するために生成AIで翻訳する場合があります。
Do not use generative AI for reflections: they should express your own thinking. The teacher may use generative AI to translate submissions in your native language to understand their content.

## その先の生成AI活用へ / Toward using generative AI

生成AIを使うときにも、提案されたコードが目的に合うかを判断し、実行して確かめ、必要なら直す力が必要です。後期「プログラミング基礎」後半では、これまでの学びを通して培った土台を固め、その判断を自分でできるようになることを目指します。
When using generative AI, you still need to judge whether suggested code meets your goals, test it and make corrections. This part of the course consolidates the foundation developed through your earlier learning so you can make those judgments yourself.
