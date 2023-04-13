from setuptools import find_packages, setup

def get_requirements(file_path:str)->List[str]:
    






setup(
name = 'mlproject'
version = 0.0.1
author = 'Reetu'
author_email = reetunarasimha400@gmail.com
packages = find_packages(),
install_required = get_requirements('requirement.txt')


)
