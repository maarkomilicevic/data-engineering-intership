import unittest
from unittest.mock import MagicMock, patch
from lambda_function import lambda_handler

class TestLambdaHandlerWithoutMoto(unittest.TestCase):
    @patch('lambda_function.boto3.client')
    def test_lambda_handler(self, mock_boto_client):

        mock_s3_client = MagicMock()
        mock_boto_client.return_value = mock_s3_client


        mock_s3_client.get_paginator.return_value.paginate.return_value = [
            {'Contents': [
                {'Key': 'pollution/Levi9 NineAir Belgrade/file1.txt'},
                {'Key': 'pollution/Levi9 NineAir Belgrade/file2.txt'},
                {'Key': 'pollution/Levi9 NineAir Belgrade/sub/file3.txt'}
            ]}
        ]


        mock_s3_client.copy_object.return_value = {}


        event = {}
        context = {}


        lambda_handler(event, context)


        expected_calls = [
            {
                'CopySource': {'Bucket': 'nine-air-weather-data', 'Key': 'pollution/Levi9 NineAir Belgrade/file1.txt'},
                'Bucket': 'destination-bucket-mm',
                'Key': 'pollution/Levi9 NineAir Belgrade/file1.txt'
            },
            {
                'CopySource': {'Bucket': 'nine-air-weather-data', 'Key': 'pollution/Levi9 NineAir Belgrade/file2.txt'},
                'Bucket': 'destination-bucket-mm',
                'Key': 'pollution/Levi9 NineAir Belgrade/file2.txt'
            },
            {
                'CopySource': {'Bucket': 'nine-air-weather-data', 'Key': 'pollution/Levi9 NineAir Belgrade/subfolder/file3.txt'},
                'Bucket': 'destination-bucket-mm',
                'Key': 'pollution/Levi9 NineAir Belgrade/subfolder/file3.txt'
            }
        ]

        for call in expected_calls:

            mock_s3_client.copy_object.assert_any_call(**call)


        self.assertEqual(mock_s3_client.copy_object.call_count, 3)

if __name__ == '__main__':
    unittest.main()
