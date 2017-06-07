import os
import boto3

import json

bucket = os.environ.get('bucket')

def handler(event, context):
    s3_object = event['Records'][0]['s3']['object']['key']
    client = boto3.client('rekognition')

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
    matched_face = rekognition_response['FaceMatches'][0]['Face']['FaceId']

    match = {
        "uploadedItem": s3_object,
        "matchedFace": matched_face,
    }

    # update map

    return response
