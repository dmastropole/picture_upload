import os
import io
import app
import unittest
import StringIO
#import tempfile

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        #self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        #app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        self.app.testing = True
        #app.init_db()

    def tearDown(self):
        pass
        #os.close(self.db_fd)
        #os.unlink(app.app.config['DATABASE'])
        
    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        #assert '<Response streamed [200 OK]>' in rv.data
        
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