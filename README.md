# Project
Python questions for beginners

# Structure Overview
    .
    ├── problems                     	# Problems and basic tests
    ├── tests                     		# Advanced tests
    ├── utils                     		# Utilities
    ├── updates                     	# Patch notes
    └── README.md

# Setup Process 安裝過程
Below will help you setup this suite. We will heavily using command line interface to do the job for us.

請根據以下步驟安裝git，我們會大量使用終端機。
## First time setup 第一次安裝
1. download git 下載git
    * MacOS: You should have git installed already. If not, download Xcode Command Line Tools. You can also download Xcode in AppStore, which should include all the tools you need.

    &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;MacOS用戶應該會有git了，沒有的話請到AppStore下載Xcode。
    * Windows: https://git-scm.com/download/win

2. Check git version by using `git --version` in your terminal

    請用上方指令確認是否正確安裝git。

3. Setup you name and email for git like `git config --global user.name "My Name"` and `git config --global user.email "email@example.com"`

    請設定你的名字和電子郵箱，這只是適用於辨識而已，才能確認是誰訪問過或是修改過這邊的程式碼。

4. Download this suite `https://github.com/ms964107/coding-tut-python.git`

    下載這邊所有的程式碼。

5. Create and checkout your branch `git checkout -b <your_branch>`, all your work will be done in your own branch, ex: `git checkout -b johndoe`

    創造並使用你自己的分支，你只會在你的分支上做修改及儲存，請別修改其他人的分支。

## Commit your work 儲存你的修改並放入本地儲存空間和上傳至遠端儲存空間
1. Save all your file, make sure you are in your own branch

    先儲存你的檔案，請確保你在你的分支內。

2. Stage all your files `git add <files>`, ex: `git add myfile.py`

    把修改的檔案放入暫存區。

3. Commit your changes `git commit -m "some message"`, ex: `git commit -m "complete assignment 1"`

    把暫存區檔案寫入本地儲存空間。

4. Push your code to remote repository `git push origin <your_branch>`, ex: `git push origin johndoe`

    把本地儲存空間的修改上傳至遠端儲存空間

## Pull the latest changes 更新你的本地儲存空間
1. Make sure you are at your own branch `git checkout <your_branch>`, ex: `git checkout johndoe`

    請先確保你目前在你的分支

2. Pull all the latest changes from main branch `git pull origin main`

    從遠端儲存空間下載最新資料到你的分支

## Some useful git utils 一些有用的git指令
- Check version `git --version`

    查看版本
- Check git history `git log`

    查看儲存區歷史紀錄
- Check current status and modified files `git status`

    查看目前狀態

## Some useful CLI commands 一些有用的終端機指令
- Go to a folder `cd <folder>`, ex: `cd Desktop`, `<folder>` can be a relative or absolute path

    去某個資料夾，`<folder>` 可以是相對或是絕對路徑

- Go to upper folder `cd ..`

    去上個資料夾

- List all files and folders in the current folder `ls`

    列出當前資料夾裡所有的檔案及資料夾

# Note
- Advance tests will not be updated in awhile. We will provide more basic tests to ensure your solution is correct.

    進階tests目前不會繼續更新，我們會給予更多基礎tests確保算法的正確性。

# Resources
[Leetcode](https://leetcode.com/problemset/all/)
