import boto3, pprint, os

# There is another way to interact with the SDK called the 'resource' interface.
# The two interfaces differ in the way that they are used and how they work underneath.
# s3 = boto3.resource('s3')
s3 = boto3.client('s3')


def create_bucket(name: str, **kwargs) -> None:
    '''Create a new empty bucket.'''
    if not isinstance(name, str):
        raise TypeError(f'Expected type str for agument name, got: {type(name)}')

    # The following is required for Europe, otherwise AWS will throw an error
    config = {
        'LocationConstraint': 'eu-north-1',
    }
    output = s3.create_bucket(Bucket=name,
                              CreateBucketConfiguration=config,
                              **kwargs)
    pprint.pprint(output)


def upload_file(file_path: str, bucket_name: str, **kwargs) -> None:
    '''Upload a local file to an existing bucket.'''
    with open(file_path, 'rb') as data:
        output = s3.put_object(Bucket=bucket_name,
                               Key=os.path.basename(data.name),
                               Body=data.read(),
                               **kwargs)
        pprint.pprint(output)


def main():
    # create_bucket("eb1-dd")
    upload_file('../files/dummy.txt', 'eb1-dd')

if __name__ == "__main__":
    main()
