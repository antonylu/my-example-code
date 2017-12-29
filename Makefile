obj-m += foo_uevent.o foo_kobject.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules
	rm -rf foo_*.mod.*
	rm -rf modules.order
	rm -rf Module.symvers
	ls -la foo*.o
	rm -rf .foo*.*
	rm -rf  .tmp_versions/

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
	ls -la
	
