Tests for two user-stories.
Requirements: Python3.9, Selenium Chrome Web Driver.

You should install Web Driver for Chrome(put him in PATH or add to directory) before use tests.

Installation:
1. $ cd test_sovkombank/
2. create venv, activate.
3. $ pip install -r requirements.txt
4. Make sure about installed Chrome Web Driver to scope os or directory.

Usage:
1. $ pytest -v -m search_story 
2. $ pytest -v -m images_story

The search_story mark for search story tests and
the images_story mark for images story tests.
