from connector.download.plugin.bing import smykowski


def test_register_listener():
    def callback(message):
        pass

    smykowski.register_listener("random_topic", callback)
    assert(callback in smykowski.listeners_for_topic("random_topic"))


def test_callback():
    _called = []

    def callback(message):
        print message
        _called.append(True)
    smykowski.register_listener("random_topic", callback)
    smykowski.publish("random_topic", "a message")
    assert(_called[0])
