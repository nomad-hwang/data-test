from typing import List


class Publisher:
    def __init__(self):
        self.subscribers: List[Subscriber] = []

    def register(self, subscriber: "Subscriber"):
        self.subscribers.append(subscriber)

    def unregister(self, subscriber: "Subscriber"):
        self.subscribers.remove(subscriber)

    def notify_all(self, *args, **kwargs):
        for subscriber in self.subscribers:
            subscriber.notify(self, *args, **kwargs)


class Subscriber:
    def __init__(self):
        self.publisher: Publisher = None

    def subscribe_to(self, publisher: Publisher):
        self.publisher = publisher
        publisher.register(self)

    def unsubscribe_from(self, publisher: Publisher):
        publisher.unregister(self)
        self.publisher = None

    def notify(self, publisher, *args, **kwargs):
        raise NotImplementedError("Subclass must implement notify()")
