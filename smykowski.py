from collections import namedtuple

listeners = {'*': []}

SmykowskiMessage = namedtuple('SmykowskiMessage', ['topic', 'message'])


def publish(topic, message):
    smykowski_message = SmykowskiMessage(topic=topic, message=message)
    for listener in listeners[topic]:
        listener(smykowski_message)
    for listener in listeners['*']:
        listener(smykowski_message)


def listeners_for_topic(topic):
    return listeners[topic]


def register_listener(topic, callback):
    if topic not in listeners.keys():
        listeners[topic] = []
    listeners[topic].append(callback)
