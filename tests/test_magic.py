from card_parser import __version__


def test_version():
    assert __version__ == '0.1.0'

text = 'Add 1 blue mana to your mana pool. Tapping this artifact can be played as an interrupt.'
def parse(text):
    dict = parse(text)
    assert dict.get('Add_mana') == '1 blue'
    assert len (dict) == 1

