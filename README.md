# robosys2022
![test](https://github.com/ChikaraHanakawa/robosys2022/actions/workflows/test.yml/badge.svg)  
↑ テスト結果を反映したバッジの画像が埋め込まれる。標準入力から読み込んだ数字を足す。  
![chase_inspection](https://github.com/ChikaraHanakawa/robosys2022/actions/workflows/chase_inspection.yml/badge.svg)  
↑ chase_inspection.bashでの結果を反映したバッジの画像が埋め込ます。  

## OpenCVとは
OpenCVはintelのエンジニアが開発した、画像や動画に関する処理をまとめたオープンソースのライブラリです。画像や動画中に存在する物体の位置情報やパターン、動きをプログラムが識別できるようになります。認識した情報を用いて、画像の切り出しや編集も可能です。  
## 概要
パソコンに備わっているwebカメラを利用して、設定した閾値の色を追跡して、ウィンドウに表示させます。そして、認識した1フレームの画像を保存します。  
## 目的
色検出をしてみたかったからです。  
## 使用方法
* terminal上にて以下のコマンドを実行  
  * **HTTPS**  
  ```
  https://github.com/ChikaraHanakawa/robosys2022.git
  ```
  * **SSH**  
  ```
  git@github.com:ChikaraHanakawa/robosys2022.git
  ```
## plus
### コマンド概要
* 標準入力から読み込んで、数値を足していきます。  
### how to use
* 与えたれた自然数以下の数値を全て足して表示します。  
* terminalで'seq [自然数] | ./plus'  
## chase
### コマンド概要
* 実行後にwebカメラが開き、'frame','mask','ans'のウィンドウが表示され、'mask'と'ans'に検出した色をハイライトで表示します。  
### how to use
1. クローン後に、'chase.py'を実行
2. webカメラが閾値に設定した色を捉えるとその1フレームだけ画像を保存します。  
3. 終了する時は、何かしらのキーを打ちます。  
## 動作確認済み環境
* Ubuntu 20.04.5 LTS
  * naitive
* Python
  * テスト済み: 3.7〜3.10
## LISESE
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。  
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。  
  * [ryuichiueda/my_slides robotsys2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
  * © 2022 ChikaraHanakawa test in robosys2022
