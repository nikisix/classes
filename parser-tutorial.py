
import ConfigParser as cp
cp.ConfigParser()
parser = cp.ConfigParser()
parser.add_section('section1')
parser.set('section1','key1','v1')
parser.set('section1','key2','v2')
parser.write(file('config.out','w'))

cat config.out
[section1]
key1 = v1
key2 = v2

parser.read('config.out')
parser.sections()
parser.items('section1')
