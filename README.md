# jobcan_selenium
https://id.jobcan.jp/ での打刻をターミナルから行うツール

# 動作環境 Requirements
1. ローカル環境のGoogle ChromeでSeleniumのPythonバインディングを動かせること
   Environment where Selenium on Python + local(non-docker) Google Chrome web-driver can run
2. credentials.txtという名前のファイルを同じ階層に作成し、1行目にGoogleのメールアドレス、2行目にパスワードを書いておく
   create a file named credentials.txt and write your gmail/gsuite address on the 1st line, and your password on the 2nd line

# 備考
Dockerから動かせるかは試してないけど、headlessだとうまくいかなさそうだったのでダメかもしれない

