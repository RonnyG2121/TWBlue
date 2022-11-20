# -*- coding: utf-8 -*-
import mastodon
from pubsub import pub

class StreamListener(mastodon.StreamListener):

    def __init__(self, session_name, user_id):
        self.session_name = session_name
        self.user_id = user_id
        super(StreamListener, self).__init__()

    def on_update(self, status):
        pub.sendMessage("mastodon.status_received", status=status, session_name=self.session_name)

    def on_conversation(self, conversation):
        print("New conversation: {}".format(conversation))
        pub.sendMessage("mastodon.conversation_received", conversation=conversation, session_name=self.session_name)

    def on_notification(self, notification):
        pub.sendMessage("mastodon.notification_received", notification=notification, session_name=self.session_name)

    def on_unknown_event(self, event):
        log.error("Unknown event: {}".format(event))
