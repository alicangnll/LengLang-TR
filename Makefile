all:
	pyinstaller leng.py leng2.py parser.py dosya_ac.py --onefile
	mkdir ../bin
	mv dist/leng ../bin/
	@echo "Birlestirme : OK"
install:
	@sudo cp ../bin/leng /usr/bin/
clean:
	rm -rf build/
	rm -rf dist/
	rm leng.spec
