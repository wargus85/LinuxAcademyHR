import pytest
from hrtool import cli
import tempfile

#Setup the fixture
@pytest.fixture
def get_parser():
    return cli.get_parser()

@pytest.fixture
def testfile():
    f = tempfile.TemporaryFile()
    f.write(b'Testfile')
    f.seek(0)
    return f

def test_get_parser_with_file(testfile):
    '''
    parser will exit if raised without a file
    '''
    with pytest.raises(SystemExit):
        get_parser.parse_args()

def test_get_parser_with_flag():
    '''
    Checks that the parser can accept the flag to export values
    '''
    pass

 

