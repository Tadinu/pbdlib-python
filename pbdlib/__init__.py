from .functions import *

from .gmm import GMM
from .gmr import GMR
from .hmm import HMM
from .hsmm import HSMM
from .model import Model
from .mvn import *
from .plot import *
from .pylqr import *
from .poglqr import PoGLQR, LQR, GMMLQR
from .mtmm import MTMM, VBayesianGMM, VMBayesianGMM, VBayesianHMM

try:
	import gui
except ImportError as e:
	print (f"Could not import gui: {e.message}")
	print ("run : sudo apt-get install tkinter")
except:
	print ("Unexpected error:", sys.exc_info()[0])
	raise

from .utils import *
from .plot import *
