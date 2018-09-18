#!/usr/bin/env python
import time
from google.cloud import pubsub_v1

PROJECT='simple01-216520'
SUBSCRIPTION='forwork-test'


def list_subscriptions_in_project(project):
    """Lists all subscriptions in the current project."""
    # [START pubsub_list_subscriptions]
    subscriber = pubsub_v1.SubscriberClient()
    project_path = subscriber.project_path(project)

    for subscription in subscriber.list_subscriptions(project_path):
        print(subscription.name)
    # [END pubsub_list_subscriptions]


def callback(message):
    print('callback fired')
    print(message)
    message.ack()

def involked_subscriber(project, subscription):
    print("looking for message on project {}".format(project))
    subscriber = pubsub_v1.SubscriberClient()
    subscriber_path = subscriber.subscription_path(project, subscription)
    print("looking for message on path {}".format(subscriber_path))

    subscriber.subscribe(subscriber_path, callback = callback)

if __name__ == '__main__':
    print('Make sure $GOOGLE_APPLICATION_CREDENTIALS is defined')
    list_subscriptions_in_project(PROJECT)
    involked_subscriber(PROJECT, SUBSCRIPTION)

    while True:
        time.sleep(60)
        print(".")
