# robosys2022
こちらは、千葉工業大学先進工学部未来ロボティクス学科2年4Semesterの講義で取り扱われているリポジトリになります。  
本リポジトリには、講義で扱った`plus`,`plus_stdin`,`test.bash`と、  
自分が作成したプログラムの`chase.py`,`chase_inspection.bash`などが含まれます。 

___
![chase_inspection](https://github.com/ChikaraHanakawa/robosys2022/actions/workflows/chase_inspection.yml/badge.svg)   
↑ テスト結果を反映したバッジの画像が埋め込まれる。標準入力から読み込んだ数字を足す。  

## 本リポジトリの概要
パソコンに備わっているwebカメラを利用して、設定した閾値の色を追跡して、ウィンドウに表示させます。そして、認識した1フレームの画像を保存します。  
## 本リポジトリの使用方法
* terminal上にて以下のコマンドを実行  
  ```
  https://github.com/ChikaraHanakawa/robosys2022.git
  ```
## plus
### プログラム概要
* 標準入力から読み込んで、数値を足していきます。  
### how to use
* 与えたれた自然数以下の数値を全て足して表示します。  
* terminalで`seq [自然数] | ./plus`  
## chase.py
### プログラム概要
* 実行後にwebカメラが開き、`frame`,`mask`,`ans`のウィンドウが表示され、`mask`には2値化して、`ans`にはHSV色空間に変換ハイライトにして表示します。プログラム終了後に`images`というディレクトリを作り、検出した時の1フレームの画像を保存します。  
### how to use
1. クローン後に、`chase.py`を実行  
```
python3 chase.py
```
2. webカメラが閾値に設定した色を捉えるとその1フレームだけ画像を保存します。  
3. 終了する時は、何かしらのキーを打ちます。
4. プログラム終了後に、`image`ディレクトリを確認
```
ls images/
```
5. `images`ディレクトリに移動
```
cd images/
```
6. 保存した画像の表示
```
eog *.png
```
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
