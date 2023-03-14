import flake8.api
import glob

def test_flake8():
    style_guide = flake8.api.StyleGuide()
    report = style_guide.check_files(glob.glob('crypto_app/*.py'))
    assert report.total_errors == 0, 'Code non conforme à PEP8'
