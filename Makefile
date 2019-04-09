all:
	pyinstaller giris.py leng.py ayirici.py dosya_ac.py --onefile
	mkdir ../bin
	mv dist/lenglang ../bin/
	@echo "Birlestirme : OK"
install:
	@sudo cp ../bin/lenglang /usr/bin/
clean:
	rm -rf build/
	rm -rf dist/
	rm lenglang.spec
