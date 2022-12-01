import boto3
from moto import mock_dynamodb2
from src.boto3_example import DynamodBExample
import unittest
class Dynamodb_test(unittest.TestCase):
    @mock_dynamodb2
    def test_create_dynamo_table(self):
        dynamo = boto3.resource('dynamodb',region_name='us-east-1')
        model_instance = DynamodBExample()
        model_instance.create_movies_table()
        self.table = dynamo.Table("Movies")
        self.assertTrue(self.table) # check if we got a result
        self.assertIn('Movies', self.table.name) # check if the table name is 'Movies'
        

    @mock_dynamodb2
    def test_add_dynamo_record_table(self):
        dynamo = boto3.resource('dynamodb',region_name='us-east-1')
        model_instance = DynamodBExample()
        model_instance.create_movies_table()
        model_instance.add_dynamo_record("Movies",{"title":"End game","year":2019,"Prequel":"Avenger","Universe":"Marvel"})
        table = dynamo.Table("Movies")
        res = table.get_item(Key = {"title":"End game","year":2019})
        self.assertEqual(200, res['ResponseMetadata']['HTTPStatusCode'])
    '''
    @mock_dynamodb2
    def test_add_dynamo_record_table_failure(self):
        
            Implement the test logic here test_add_dynamo_record_table method for failures
        
    ''' 


if __name__ == "__main__":
    unittest.main()