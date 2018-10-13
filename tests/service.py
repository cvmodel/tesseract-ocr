import unittest
import requests

url = "http://127.0.0.1:8080/infer"

class ServiceTester(unittest.TestCase):
    
    def test_irs(self):
        file = open("tests/test.png", "rb")
        files = {'file': file}        
        config = {
            "delete_after_process":"true"
        }
        r = requests.post(url, files=files, data=config)
        file.close()
        print (r.text)

if __name__ == '__main__':
    unittest.main()