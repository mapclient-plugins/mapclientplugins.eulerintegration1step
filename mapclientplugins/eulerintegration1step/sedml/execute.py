from string import Template

class ExecuteSedml():
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
	
	self.simulationDataRoot = u"/home/abi/projects/simulation-data"
	self.template = self.simulationDataRoot + u"/sed-ml-templates/DTP-template-sed-ml.xml"

    def execute(self, stepSize):
	'''
	http://stackoverflow.com/questions/6385686/python-technique-or-simple-templating-system-for-plain-text-output
	'''

	#open the file
	filein = open( self.template )
	#read it
	src = Template( filein.read() )
	#document data
	d={ 'MAX_STEP_SIZE':stepSize }
	#do the substitution
	result = src.substitute(d)
	tmpFile = u"/tmp/andre-tmp-sedml.xml"
	fileout = open( tmpFile, "w" )
	fileout.write(result)
