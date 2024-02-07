@pyinstaller -F complextomath.py
@rd /s /q build
@move dist compiled
@del complextomath.spec