#!/usr/bin/env python

from google.cloud import pubsub_v1

PROJECT='simple01-216520'
TOPIC='forwork'

def list_topics(project):
    publisher = pubsub_v1.PublisherClient()
    project_path = publisher.project_path(project)

    for topic in publisher.list_topics(project_path):
        print(topic)

def publish_message(project, topic, message):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project, topic)
    data = message.encode('utf-8')
    publisher.publish(topic_path, data=data)
    print("published {}".format(data))

if __name__ == '__main__':
    print('Make sure $GOOGLE_APPLICATION_CREDENTIALS is defined')
    list_topics(PROJECT)

    publish_message(PROJECT, TOPIC, "hello world2")
