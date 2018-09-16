import core
import mesh
import sys,time
from modelcore import *

e=core.Environment(sys.argv,opts=toolboxes_options("fluid"))

import discr
import exporter
import ts
from fluid import *

f=Fluid_P2P1G1("fluid")
f.init()
f.printAndSaveInfo()
if f.isStationary():
    f.solve()
    f.exportResults()
else:
    if not f.doRestart():
        f.exportResults( f.timeInitial() )
    while not f.timeStepBase().isFinished():
        if f.worldComm().isMasterRank():
            print("============================================================\n")
            print("time simulation: ", f.time(), "s \n")
            print("============================================================\n")
        f.solve()
        f.exportResults()
        f.updateTimeStep()
