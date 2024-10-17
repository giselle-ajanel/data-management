import csv
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-1')
table = dynamodb.Table('Movies')

# Function to convert CSV data to JSON-like dict format
def csv_to_dynamodb(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Modify 'Id', 'Name', etc., to match your CSV headers and DynamoDB attributes
            item = {
                'id': row['id'],
                'date': row['date'],
                'description': row['description'],
                'minute': row['minute'],
                'name': row['name'],
                'rating': row['rating'],
                'tagline': row['tagline']
            }
            table.put_item(Item=item)

# Replace 'path/to/yourfile.csv' with your CSV file's path
csv_to_dynamodb('/Users/owner/Downloads/movies.csv')




