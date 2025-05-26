from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ["numpy","sympy","iapws"], 'include_files': ["imagem.png"]}

base = 'gui'

executables = [
    Executable('Prova1.py', base=base, target_name = 'Prova')
]

setup(name='Prova1',
      version = '1',
      description = 'evaporador',
      options = {'build_exe': build_options},
      executables = executables)