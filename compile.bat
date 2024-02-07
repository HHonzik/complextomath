@rd /s /q compiled
@pyinstaller -F complextomath.py
@rd /s /q build
@move dist compiled
@rd /s /q compiled\dist
@del complextomath.spec