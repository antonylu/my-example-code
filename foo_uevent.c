#include <linux/kobject.h>
#include "foo_kobject.h"
#include "foo_uevent.h"

static struct foo_obj *foo_kobj;

int foo_init_events(void)
{
  int ret;

  //ret = example_init();
  if (ret) 
  { 
    printk("error - could not create ksets\n");  
    goto foo_error;
  } 
 
  foo_kobj = create_foo_obj("foo");
  if (!foo_kobj)
  {
    printk("error - could not create kobj\n"); 
    goto foo_error;
  }
 
  return 0;

foo_error:
  return -EINVAL;
}

int foo_send_uevent(struct foo_event *pce)
{
  char event_string[20];
  char *envp[] = { event_string, NULL };

  if (!foo_kobj)
    return -EINVAL;

  snprintf(event_string, 20, "FOO_EVENT=%d", pce->etype);

  return kobject_uevent_env(&foo_kobj->kobj, KOBJ_CHANGE, envp);
}

