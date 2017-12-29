#ifndef FOO_KOBJECT_
#define FOO_KOBJECT_

/* 
 * Partially copied from linux/samples/kobject/kset-example.c
 *
 * Released under the GPL version 2 only.
 */

/*
 * This is our "object" that we will create and register it with sysfs.
 */
struct foo_obj {
 struct kobject kobj;
 int foo;
};
#define to_foo_obj(x) container_of(x, struct foo_obj, kobj)

struct foo_obj *
create_foo_obj(const char *name);

int 
foo_kobj_init(void);

void
foo_kobj_exit(void);

#endif
