from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ["numpy","sympy","iapws"], 'include_files': ["Simples_E.png","Triplo_E.png"]}

base = 'gui'

executables = [
    Executable('Interface.py', base=base, target_name = 'Prova')
]

setup(name='Prova1',
      version = '1.0',
      description = 'Evaporadores',
      options = {'build_exe': build_options},
      executables = executables)