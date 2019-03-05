from pylint.interfaces import IRawChecker
from pylint.checkers import BaseChecker

class MyRawChecker(BaseChecker):
    #check for lines with absolute imports and warns

    __implements__ = IRawChecker

    name = 'relative-checker'
    msgs = {'W0043': (
                'Use only relative imports for keras classes and functions',
                'absolute-import',
                'Refer to relative versus absolute imports'
                ),
            }
    options = ()

    def process_module(self, node):
        """process a module

        the module's content is accessible via node.stream() function
        """
        
        ignore = ['__future__', 'collections', 'random', 'six', 'cPickle', 'scipy', 'hashlib', 
                  'io', 'contextlib', 'unittest', 'types', 'h5py', 'inspect', 'tarfile', 'yaml', 
                  'copy', 'marshal', 'requests', 'functools', 'gzip', 're', 'Queue', 'queue', 
                  'os', 'pickle', 'importlib', 'mock', 'threading', 'codecs', 'tempfile', 'time', 
                  'binascii', 'pydot', 'zipfile', 'json', 'shutil', 'abc', 'sys', 'csv', 'cntk',
                  'warnings', 'numpy', 'skimage', 'multiprocessing', 'distutils', 'tensorflow', 
                  'theano', 'keras_applications', "keras_preprocessing"]
    
        
        comment = False
        with node.stream() as stream:
            for (lineno, line) in enumerate(stream):
                line = line.decode("utf-8").strip()
                #Ingore lines withing multi line comments
                if '\"\"\"' in line:
                    comment = not comment
                #Empty line or comment line
                if line == "" or comment == True or '#' in line:
                    continue
                else:
                    split_line = line.split()
                    #Import
                    if split_line[0] == 'import':
                        module_split = split_line[1].split('.')
                        #Check if module is an ignored library
                        if module_split[0] in ignore:
                            continue
                        else:
                            self.add_message('W0043', line=lineno) 
        
                    #ImportFrom
                    elif split_line[0] == 'from' and len(split_line) >= 3:
                        #Check if module is an ignored library or line doesnt contain import
                        if split_line[1] in ignore or split_line[2] != 'import':
                            continue
                        #Check if import is absolute or relative
                        elif split_line[1].startswith('.'):
                            pass
                        else:
                            module_split = split_line[1].split('.')
                            if module_split[0] in ignore:
                                continue
                            else:
                                self.add_message('W0043', line=lineno)
                    else:
                        continue
                
        


def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(MyRawChecker(linter))
