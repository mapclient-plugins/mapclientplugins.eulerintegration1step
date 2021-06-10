from string import Template
from subprocess import call
import numpy as np
import tempfile
import sys
import os
import pathlib


class ExecuteSedml():
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        self._simulation_root = None

        self.simulationDataRoot = u"/home/abi/projects/simulation-data"
        self.template = self.simulationDataRoot + u"/sed-ml-templates/euler-with-sine-model.xml"

    def setSimulationRoot(self, location):
        self._simulation_root = location

    def execute(self, stepSize, n):
        '''
        http://stackoverflow.com/questions/6385686/python-technique-or-simple-templating-system-for-plain-text-output
        '''

        # Create our SED-ML file from the template with the given step size
        # open the file
        template_file = os.path.join(self._simulation_root, 'sed-ml-templates', 'euler-with-sine-model.xml')
        filein = open(template_file)
        # read it
        src = Template(filein.read())
        # document data
        source_model = os.path.join(self._simulation_root, 'pmr2', 'sine', 'sin_approximations.xml')
        model_url = pathlib.Path(source_model).as_uri()
        d = {'MAX_STEP_SIZE': stepSize, 'NUMBER_OF_POINTS': n, 'SINE_SOURCE_MODEL': model_url}
        # do the substitution
        result = src.substitute(d)
        tmpFile = tempfile.NamedTemporaryFile(delete=False)

        # tmpFile = os.t"/tmp/andre-tmp-sedml.xml"
        # fileout = open( tmpFile, "w" )
        tmpFile.write(result.encode())
        tmpFile.flush()

        # execute the simulation experiment
        sedmlDocument = pathlib.Path(tmpFile.name).as_uri()
        resultsFile = tempfile.NamedTemporaryFile(delete=False)
        tmpFile.close()
        resultsFile.close()
        returnCode = call(
            [os.path.join(self._simulation_root, 'bin', 'get-sed-ml-client-' + sys.platform), sedmlDocument,
             resultsFile.name])
        if returnCode != 0:
            return None
        data = np.genfromtxt(resultsFile.name, dtype=float, delimiter=',', names=True)

        os.remove(resultsFile.name)
        os.remove(tmpFile.name)

        return data
