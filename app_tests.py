import os
import io
import app
import unittest
import StringIO
#import tempfile

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass
        
    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        
    def uploading(self):
        with open('test.jpg') as test:
            imgStringIO = StringIO.StringIO(test.read())

        return self.app.post('/img',
            content_type='multipart/form-data',
            data={'file': (imgStringIO, 'test.jpg')},
            follow_redirects=True
        )

    def test_uploading(self):
        rv = self.uploading()
        assert '\xff\xd8' in rv.data

if __name__ == '__main__':
    unittest.main()
    os.system('rm uploaded_image')