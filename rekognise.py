import os
import boto3

from api_client import BigBotherAPIClient

bucket = os.environ.get('bucket')

def handler(event, context):
    print event

    s3_object = event['Records'][0]['s3']['object']['key']

    client = boto3.client('rekognition')

    api = BigBotherAPIClient()

    rekognition_response = client.search_faces_by_image(
        CollectionId='cloudreach-faces',
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': s3_object
            }
        }
    )

    print "Number of matches found: {}".format(len(rekognition_response['FaceMatches']))

    if len(rekognition_response['FaceMatches']) is 0:
        return

    matched_face_id = rekognition_response['FaceMatches'][0]['Face']['FaceId']
    location = s3_object.split('/')[1]

    person = api.find_person_by_face_id(matched_face_id)
    updated_location = api.update_person_location(person['fullName'], location, 'London')

    return updated_location

