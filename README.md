
# Command Project InfoHub


For run this ->

1 - create venv 
``` text
    python -n venv .venv 
```
or 
``` text
  python3 -m venv .venv
```
2 - activate <br>
---2.1 - Windows 
  ``` text
  .\.venv\Scripts\activate
```
---2.2 - linux \ macos
   ``` text
  source .venv/bin/activate
```
3 - installing poetry 
  ``` text
  pip install poetry
```

4 - installing all libraries
  ``` text
  poetry install
 ```

5 - setup secret key , create .env file and write
``` text
    SECRET_KEY = "<SECRET_KEY>"
```
    
6 - run in run_backend.py
7 - go to 
``` text
  http://127.0.0.1:8000/docs
```
its fastapi Swagger UI 

8 - Enjoy 
