import os
import AcceptanceTestHelpers
## For each programming language in voicecode a file like this should be present,
## for doing the acceptance tests.

## The tests are kept in the directory Data/Demo/java (for this one), in python files.
## These files are tested in "test_acceptance_tests" one by one,
## and the results are tested against the expected results.
#  Note: the first difference ends the testing!

## The test files are also going to be used for "what can I say" demonstration.

## When you want to make a new test follow the instructions in
## the function "test_make_new_acceptance_test" below.
## Do not forget to comment out your lines after you did so.

## When one of the tests does not pass any more,
## the results are kept in the file "demo_name__new.py" (test file was "demo_name.py").
## If you are sure the new result is correct,
## for example after improvements in the voicecode code or in the vc_config file,
## simply remove the previous file and rename the __new.py file.

class JavaAcceptanceTest(AcceptanceTestHelpers.AcceptanceTestHelpers):
     
    def __init__(self, name):
        AcceptanceTestHelpers.AcceptanceTestHelpers.__init__(self, name)
        language_name = self.__class__.__name__
        self.assert_(language_name.endswith("AcceptanceTest"), "Class name must end with 'AcceptanceTest'")
        self.language_name = language_name[:-len("AcceptanceTest")]
        self.file_extension = ".java"    
        self.header_of_demo_file = "demo file generated with mediator test of %s"% self.__class__.__name__
        
    def setUp(self):
        self._init_simulator_regression()
        # test can change the working directory, so save:
        self.old_dir = os.getcwd()
        
    def tearDown(self):

        if os.getcwd() != self.old_dir:
##            print ' working directory to: %s'% self.old_dir
            os.chdir(self.old_dir)

###############################################################
# Assertions.
# 
# Demo of statements, collect new test or test previous entered tests
###############################################################

    def test_make_new_acceptance_test(self):
        """define new statements for a java acceptance test
        """
## instructions:        
## --put in source:  a series of Heard strings from an interactive session or
##                   a series of self._say("...") commands or
##                   a series of commands.say(['comment','line']) (as from the old style tests)
##                   just a series of utterances
## --put in name: the name of the test

## In Data/Demo/java a python file "name.py" is created, which contains the phrases and
## window contents.

## put in the return as the top again if you are ready. Next time the test is taken with the other acceptance tests

## For each test an empty test file is taken...
## 
        return

        name = "demo import"                        

        source =    \
"""        
        self._say("import hello world")
        self._say("new statement")
"""
        self.make_acceptance_test_file(source, name)


    def test_acceptance_tests(self):
        """go through the previous setup demo tests


        see test_make_new_acceptance_test above, for making them
        """
        demo_folder = self.find_demo_directory()
        # needed for importlater:
        os.chdir(demo_folder)
        files = os.listdir(demo_folder)

        nFail = 0
            
        for file_path in files:
            if not file_path.endswith(".py"):
                continue
            if file_path.endswith("__new.py"):
                continue
            result = self.do_test_acceptance_test_file(demo_folder, file_path, no_stop=1)
            if result:
                self.print_acceptance_fail_result(result)
                nFail += 1
        if nFail:
            self.fail("%s of the acceptance tests of %s failed"% (nFail, self.language_name))
