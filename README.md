# fastapi-template

## TODO
- [ ] Add database (ORM), using SQLAlchemy
- [X] A simple webpage that can upload file
- [ ] Unit test

## Build
1. Install `virtualenv`
```
pip install virtualenv
```

2. Clone git repository and open the working folder
```
git clone https://github.com/CK642509/fastapi-template.git
```
3. Create virtual environment
```
virtualenv .venv
```

4. Select the virtual environment as the interpreter in VS Code (Ctrl + Shift + P)
5. Install requirements
```
pip install -r requirements.txt
```
6. Start main.py
```
python -m main
```

## 討論紀錄
### 10/13
- 前端用 [Vue](https://vuejs.org/)，後端用 [fastapi](https://fastapi.tiangolo.com/)
- 測試、部屬之後再討論
- 主要功能為 活動報名網站
- 目前只有 python，Vue之後再加進來
- 版本
    - Vue 3
    - python 3.9
- 未來可能添加功能
    - 使用 google、FB 登入
    - 串金流