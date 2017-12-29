#ifndef FOO_UEVENT_
#define FOO_UEVENT_

enum foo_event_type {
  FOO_GET = 1,
  FOO_SET
};

struct foo_event {
  enum foo_event_type etype;
};

int foo_init_events(void);

int foo_send_uevent(struct foo_event *fooe);

#endif
