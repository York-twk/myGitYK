Hello World
This is a test for git and github

常用的語法
git init 一開始建立git儲存庫
git config --global user.name ""  設定user name
git config --global user.email ""  設定user email
git add 新增至儲存庫
    add . 新增全部檔案
    add *.py 新增所有副檔名為py的檔案
git commit -m "" 新增修改版本

基本上需同時使用 add 與 commit 將檔案更新至儲存庫
git push -u origin main 第一次將檔案推送至github
git push 將本地檔案推送至github 需確認修改檔案已使用 add 與 commit 新增至本地庫
