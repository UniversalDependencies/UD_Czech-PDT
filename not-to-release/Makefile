getsample:
	rm cmpr9410_001.*
	cp /net/data/pdt-c-1.0/data/PDT/pml/tamw/train-1/cmpr9410_001.* .
	gunzip cmpr9410_001.*

extract:
	extract_functors_from_pdt.py > functors.txt

add:
	add_functors_to_ud.py

