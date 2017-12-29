# exampleCode

Add uevent and kobject example

1. kernel generate uevent
2. Android add a Observer service through binder to receive the uevent in user space, then send notification in UI

* make
* udevadm monitor
  * insert module 時, 會有KOBJ_ADD uevent
  * rmmod 時會有 KOBJ_REMOVE uevent
* sudo insmod kset-example.ko (or uevent.ko)
* check /sys/kernel/kset-example, the device nodes are generated
