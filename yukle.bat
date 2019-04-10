cls
@echo LengLang v0.1
@echo Lütfen Dosyalarınızı C:\Python27\Scripts knumuna kopyalayın
@cd C:\Python27\Scripts
@pip update
@pip install pyinstaller
@pyinstaller leng leng.py dosya_ac.py ayirici.py --onefile
@mkdir ../bin/
@copy dist/leng ../bin/
@del leng.spec
@rmdir /S /Q dist
@rmdir /S /Q build
pause