# jobcan_selenium
https://id.jobcan.jp/ での打刻をターミナルから行うツール

### 動作環境 Requirements

0. 筆者の用途上、GSuiteでのログインに限定した実装になっています、あしからず。  
1. ローカル環境のGoogle ChromeでSeleniumのPythonバインディングを動かせること  
   特にこだわりがなければ、pipかpip3でインストールするのがおすすめです。  
   Environment where Selenium on Python + local(non-docker) Google Chrome web-driver can run  
   It's recomended to install them via pip or pip3 unless you already have any specific package managers like pyenv or conda.  
   
2. credentials.txtという名前のファイルを同じ階層に作成し、  
   1行目にGoogleのメールアドレス、2行目にパスワードを書いておく  
   Create a file named credentials.txt  
   and write your gmail/gsuite address on the 1st line, 
   and your password on the 2nd line  


### 備考
Dockerから動かせるかは試してないけど、headlessだとうまくいかなさそうだったのでダメかもしれない

