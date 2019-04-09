cls
@echo LengLang v0.1
@echo Lütfen Dosyalarınızı C:\Python27\Scripts knumuna kopyalayın
@cd C:\Python27\Scripts
@pip update
@pip install pyinstaller
@pyinstaller giris.py leng.py dosya_ac.py ayirici.py --onefile
@mkdir ../bin/
@copy dist/lenglang ../bin/
@del lenglang.spec
@rmdir /S /Q dist
@rmdir /S /Q build
pause
