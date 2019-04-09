cls
@echo Bu kurulum kodu sadece eger pyinstaller kurulu ise calisacaktir.
@echo Eger bu programin kurulu oldugundan emin degilseniz lutfen internetten pyinstallerin
@echo nasil kurulacagi hakkindaki kaynaklara goz atiniz.

@pyinstaller giris.py leng.py dosya_ac.py ayirici.py --onefile

@mkdir ../bin/

@copy dist/lenglang ../bin/

@del lenglang.spec
@rmdir /S /Q dist
@rmdir /S /Q build
pause