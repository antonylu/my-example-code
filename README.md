# uevent usage example Code

An uevent and kobject example code

Usage:
* make
* udevadm monitor
  * insert module 時, 會有KOBJ_ADD uevent
  * rmmod 時會有 KOBJ_REMOVE uevent
* sudo insmod kset-example.ko (or uevent.ko)
* check /sys/kernel/kset-example, the device nodes are generated

How to use in Android?
1. kernel generate uevent
2. Android adds an Observer service through binder to receive the uevent in user space, then send notification in UI.
