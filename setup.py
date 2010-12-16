import madpy.config.configyml
from distutils.core import setup, Extension
suffixes = ['c', 'h', 'py', 'in', 'yml', 'sh', 'sql']
additional_files = ['Makefile']

conf = madpy.config.configyml.get_config('madpy')
rev = madpy.config.configyml.get_version('madpy')

pkg_data = {'madlib' : []}
for mpair in conf['methods']:
    m = mpair['name']
    pport = mpair['port']
    for s in suffixes:
        # print "pkg_data['madlib'] += " + str([m+'/src/'+pport+'/*.'+s])
        pkg_data['madlib'] += [m+'/src/'+pport+'/*.'+s]
    pkg_data['madlib'] += [m+'/src/'+pport+'/'+ f for f in additional_files]

pkg_data['madpy'] = []
for s in suffixes:
    pkg_data['madpy'] += ['*.' + s]
    pkg_data['madpy'] += ['config'+'/*.'+s]
    
setup(name='madlib',
      version=rev,
      description='MADlib library of SQL analytics',
      url='http://github.com/madlib',
      packages=['madpy','madlib','madpy.config','madpy.migrate'],
      package_dir={'madpy': 'madpy', 'madlib': 'methods'},
      package_data=pkg_data,
      requires=['yaml','argparse', 'shutil', 'sqlparse', 'imp', 'traceback', 'hashlib'],
      provides=['madpy','madlib']
      )