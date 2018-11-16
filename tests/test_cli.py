import pytest
from hrtool import cli
import tempfile

#Setup the fixture
@pytest.fixture
def create_parser():
    return cli.create_parser()

def test_get_parser_with_file(create_parser):
    '''
    parser will exit if raised without a file
    '''
    with pytest.raises(SystemExit):
        create_parser.parse_args(['--export'])

def test_main_exit_without_sudo():
    '''
    main will exit if raised being super user
    '''
    with pytest.raises(SystemExit):
        cli.main()

def test_get_parser_with_flag(create_parser):
    '''
    Checks that the parser can accept the flag to export values
    '''
    args = create_parser.parse_args(['/path/to/file.json','--export'])
    assert args.jsonfile == '/path/to/file.json'
    assert args.export == True

def test_get_parser_raised_with_nothing(create_parser):
    '''
    Checks that the parser will exit if raised with no input
    '''
    with pytest.raises(SystemExit):
        create_parser.parse_args([])
