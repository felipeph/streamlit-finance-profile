import pytest

import project


def test_open_json_file():
    with pytest.raises(FileNotFoundError):
        project.get_form_dict('file.json')

def test_json_converts_dict():
    assert project.get_form_dict('test.json')['test_key'] == 'test_value'
    
def test_update_score():
    assert project.update_score(0,
                                project.get_form_dict('form.json'),
                                0,
                                r'Consigo pagar as minhas contas e ainda guardo mais 10% dos meus ganhos.') == 10

def test_get_options():
    assert project.get_options(project.get_form_dict('form.json'),0)[0] == r'Consigo pagar as minhas contas e ainda guardo mais 10% dos meus ganhos.'
    
def test_get_profile():
    assert project.get_profile(100, project.get_form_dict('form.json')) == 'Investidor'

def test_make_new_record():
    assert project.make_new_record(r'Investidor',
                                   100,
                                   r'Ensino Superior',
                                   37,
                                   r'Até 20 salários mínimos',
                                   r'./records/scores.csv') == True
    