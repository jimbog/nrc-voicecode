import debug
import cont_gen
import VoiceCodeRootTest
from vc_globals import all_languages, c_style_languages
import sr_grammars  # for test of WinGram function get_smaller_ranges_only
import sr_grammarsNL  # for get_shortest_ranges test
import SourceBuff

class SelectTextTest(VoiceCodeRootTest.VoiceCodeRootTest):
    """Test different select results, with and without "through"

    """   
    def __init__(self, name):
        VoiceCodeRootTest.VoiceCodeRootTest.__init__(self, name)
      
    def setUp(self):
        self._init_simulator_regression()

##########################################################
# Documentation tests
#
# These tests illustrate how to use the class.
##########################################################
      
    def test_This_is_how_you_select_text(self):
        self._open_empty_test_file('temp.py')
        self._insert_in_active_buffer("small = small + 1\nlarge = large + small\n")
        self._say("select small")
        self._assert_active_buffer_content_is(\
'''small = small + 1
large = large + small<CURSOR>
''')
      
        self._say("previous one")
        self._assert_active_buffer_content_is(\
'''small = small<CURSOR> + 1
large = large + small
''')

        self._goto(0)
        self._assert_active_buffer_content_is(\
'''<CURSOR>small = small + 1
large = large + small
''')
        self._say("select large")
        self._assert_active_buffer_content_is(\
'''small = small + 1
large<CURSOR> = large + small
''')
      
        self._say(["select", "+\\plus-sign"])
        self._assert_active_buffer_content_is(\
'''small = small +<CURSOR> 1
large = large + small
''')

      
        self._say("next one")
        self._assert_active_buffer_content_is(\
'''small = small + 1
large = large +<CURSOR> small
''')

    def test_This_is_how_you_select_through_text(self):
        self._open_empty_test_file('temp.py')
        self._insert_in_active_buffer("small = small + 1\nlarge = large + small\n")
        self._say("select small through large")
        self._assert_active_buffer_content_with_selection_is(\
'''small = <SEL_START>small + 1
large<SEL_END> = large + small
''')
                   
        
    def test_This_is_how_you_select_in_explicit_direction(self):
        self._open_empty_test_file('temp.py')
        self._insert_in_active_buffer("small = small + 1\ncenter = 3\nlarge = large + small\n")
        self._say("select center")
        self._say(["select next", "small"])
        self._assert_active_buffer_content_with_selection_is(\
'''small = small + 1
center = 3
large = large + <SEL_START>small<SEL_END>
''')
        self._say(["select previous", "small"])
        self._assert_active_buffer_content_with_selection_is(\
'''small = <SEL_START>small<SEL_END> + 1
center = 3
large = large + small
''')


        self._say(["select next",  "=\\equal-sign"])
        self._assert_active_buffer_content_with_selection_is(\
'''small = small + 1
center <SEL_START>=<SEL_END> 3
large = large + small
''')
        self._say(["select previous",  "+\\plus-sign"])
        self._assert_active_buffer_content_with_selection_is(\
'''small = small <SEL_START>+<SEL_END> 1
center = 3
large = large + small
''')



    def test_This_is_how_you_select_through_or_until_text_from_cursor(self):
        self._open_empty_test_file('temp.c')
        self._insert_in_active_buffer("small = small + 1;\ncenter = 3;\nlarge = large + small;\n")
        self._assert_active_buffer_content_with_selection_is(\
'''small = small + 1;
center = 3;
large = large + small;
<CURSOR>''')
        self._say("select center")
        self._assert_active_buffer_content_with_selection_is(\
'''small = small + 1;
<SEL_START>center<SEL_END> = 3;
large = large + small;
''')
        # until::::::::::
        # note: select until is one grammar word:
        self._say(["select until", "small"])
        self._assert_active_buffer_content_with_selection_is(\
'''small = small + 1;
<SEL_START>center = 3;
large = large + <SEL_END>small;
''')

        self._say(["previous", "one"])
        self._assert_active_buffer_content_with_selection_is(\
'''small = small<SEL_START> + 1;
center<SEL_END> = 3;
large = large + small;
''')
        # through::::
        self._say("select center")
        self._assert_active_buffer_content_with_selection_is(\
'''small = small + 1;
<SEL_START>center<SEL_END> = 3;
large = large + small;
''')
        # note: select until is one grammar word:
        self._say(["select through", "small"])
        self._assert_active_buffer_content_with_selection_is(\
'''small = small + 1;
<SEL_START>center = 3;
large = large + small<SEL_END>;
''')

        self._say(["previous", "one"])
        self._assert_active_buffer_content_with_selection_is(\
'''small = <SEL_START>small + 1;
center<SEL_END> = 3;
large = large + small;
''')

        self._say("select center")
        self._assert_active_buffer_content_with_selection_is(\
'''small = small + 1;
<SEL_START>center<SEL_END> = 3;
large = large + small;
''')
        # back until::::::::::
        # note: select until is one grammar word:
        self._say(["select back until", "small"])
        self._assert_active_buffer_content_with_selection_is(\
'''small = small<SEL_START> + 1;
center<SEL_END> = 3;
large = large + small;
''')

        self._say(["next", "one"])
        self._assert_active_buffer_content_with_selection_is(\
'''small = small + 1;
<SEL_START>center = 3;
large = large + <SEL_END>small;
''')
        # back through::::
        self._say("select center")
        self._assert_active_buffer_content_with_selection_is(\
'''small = small + 1;
<SEL_START>center<SEL_END> = 3;
large = large + small;
''')
        # note: select until is one grammar word:
        self._say(["select back through", "small"])
        self._assert_active_buffer_content_with_selection_is(\
'''small = <SEL_START>small + 1;
center<SEL_END> = 3;
large = large + small;
''')

        self._say(["previous", "one"])
        self._assert_active_buffer_content_with_selection_is(\
'''<SEL_START>small = small + 1;
center<SEL_END> = 3;
large = large + small;
''')
        self._say("next one next one")
        self._assert_active_buffer_content_with_selection_is(\
'''small = small + 1;
<SEL_START>center = 3;
large = large + small<SEL_END>;
''')
        # nothing changes any more:
        self._say("next one")
        self._assert_active_buffer_content_with_selection_is(\
'''small = small + 1;
<SEL_START>center = 3;
large = large + small<SEL_END>;
''')



        



##########################################################
# Unit tests
#
# These tests check the internal workings of the class.
##########################################################

    def test_get_all_ranges_text(self):

        dummy = 1
        # function in sr_grammars.py
        win_gram = sr_grammars.WinGram(dummy)
        visible = "abg1: def(self, self.selfish, g1, h): g2 = ((self.g1,i), (h,i), (g23, 24, g))"
        #         0123456789012345678901234567890123456789012345678901234
        #                   10        20        30      40          50
        expected = {'g':  [(74, 75)],
                    'self': [(10, 14), (16, 20), (45, 49)],
                    'selfish': [(21,28)]}
                    
        for char in ['g', 'self', 'selfish']:
            all_ranges = win_gram.get_all_ranges(visible, [[char]])
            self.assert_equal(expected[char], all_ranges, "get_all_ranges result not as expected with: %s"% char)
            
    def test_get_all_ranges_spacing(self):

        # see if multiple words can be separated by 0 or 1 space...        

        dummy = 1
        # function in sr_grammars.py
        win_gram = sr_grammars.WinGram(dummy)
        visible = "self.fish, self fish, self-fish, selffishness, selfish, noself."
        #         0123456789012345678901234567890123456789012345678901234
        #                   10        20        30      40          50
        char = ['self', 'fish']
        expected =  [(0, 9), (11, 20), (22, 31)]
                    
        all_ranges = win_gram.get_all_ranges(visible, [char])
        self.assert_equal(expected, all_ranges, "get_all_ranges result not as expected with: %s"% char)

        chars = [['self', 'fish'], ['self'], ['fish']]
        expected =  [(0, 4), (5, 9), (11, 15), (16, 20), (22, 26), (27, 31)]
        all_ranges = win_gram.get_all_ranges(visible,chars)
        self.assert_equal(expected, all_ranges, "get_all_ranges result not as expected with: %s"% chars)
        
            
    def test_get_all_ranges_numbers(self):
        ## must elaborate on these:
        dummy = 1
        # function in sr_grammars.py
        win_gram = sr_grammars.WinGram(dummy)
        visible = "abg1: def(self, g1, h): g2 = ((g1,i), (h,i), (g23, 24))"
        #         0123456789012345678901234567890123456789012345678901234
        #                   10        20        30      40          50
        expected = {'1':  [(3, 4), (17, 18), (32, 33)],
                    '2': [(25, 26), (47, 48), (51, 52)],
                    '23': [(47, 49)],
                    'g1': [(16, 18), (31, 33)],
                    'g2':  [(24, 26), (46, 48)],
                    'g3': []}
                    
        for char in ['1', '2', '23', 'g1', 'g2']:
            all_ranges = win_gram.get_all_ranges(visible, [[char]])
            self.assert_equal(expected[char], all_ranges, "get_all_ranges result not as expected with: %s"% char)
            




    def test_get_smaller_ranges_only(self):
        dummy = 1
        # function in sr_grammars.py
        win_gram = sr_grammars.WinGram(dummy)
        ranges = [(1,3), (5,10), (5,20), (30,40), (35,40)]
        expected = [(1,3), (5,10), (35,40)]
        smaller_ranges = win_gram.get_smaller_ranges_only(ranges)
        self.assert_equal(expected, smaller_ranges, "get_smaller_ranges_only result not as expected")

    def test_get_shortest_ranges(self):
        dummy = 1
        # function in sr_grammars.py
        win_gram = sr_grammars.WinGram(dummy)
        start_ranges = [(1,3), (10,12), (20,22)]
        end_ranges = [(5,6), (7,8), (14,15)]
        expected = [(1,6), (10,15)]
        shortest_ranges = win_gram.get_shortest_ranges(start_ranges, end_ranges)
        self.assert_equal(expected, shortest_ranges, "get_shortest_ranges result not as expected")

        start_ranges = [(1,3), (3,4), (10,12), (20,22), (23,24), (25,26), (100,101)]
        end_ranges = [(5,6), (7,8), (14,15), (30,31), (32,33), (33,34)]
        expected =[(3, 6), (10, 15), (25, 31)]
        shortest_ranges = win_gram.get_shortest_ranges(start_ranges, end_ranges)
        self.assert_equal(expected, shortest_ranges, "get_shortest_ranges result not as expected")


    def test_ignore_occurence(self):
        dummy = 1
        # function in SourceBuff.py
        source_buff = SourceBuff.SourceBuff(dummy)
        occurence = (10,20)
        ignore_overlapping_with_cursor = 0
        ignore_left_of_cursor = 0
        ignore_right_of_cursor = 0
        start_sel = 10
        end_sel = 20
        result = source_buff.ignore_occurence( occurence=occurence,
                                            ignore_overlapping_with_cursor=ignore_overlapping_with_cursor,
                                            ignore_left_of_cursor=ignore_left_of_cursor,
                                            ignore_right_of_cursor=ignore_right_of_cursor,
                                            start_sel=start_sel,
                                            end_sel=end_sel)
        self.assert_equal(0, result, "ignore_occurence, overlapping regions fails when parameters are all 0")

        ignore_overlapping_with_cursor = 1
        result = source_buff.ignore_occurence( occurence=occurence,
                                            ignore_overlapping_with_cursor=ignore_overlapping_with_cursor,
                                            ignore_left_of_cursor=ignore_left_of_cursor,
                                            ignore_right_of_cursor=ignore_right_of_cursor,
                                            start_sel=start_sel,
                                            end_sel=end_sel)
        self.assert_equal(1, result, "ignore_occurence, overlapping regions should match")


        ignore_overlapping_with_cursor = 0
        start_sel = end_sel = 0        
        result = source_buff.ignore_occurence( occurence=occurence,
                                            ignore_overlapping_with_cursor=ignore_overlapping_with_cursor,
                                            ignore_left_of_cursor=ignore_left_of_cursor,
                                            ignore_right_of_cursor=ignore_right_of_cursor,
                                            start_sel=start_sel,
                                            end_sel=end_sel)
        self.assert_equal(0, result, "ignore_occurence, overlapping regions fails when parameters are all 0")


        ignore_overlapping_with_cursor = 1
        start_sel = end_sel = 0        
        result = source_buff.ignore_occurence( occurence=occurence,
                                            ignore_overlapping_with_cursor=ignore_overlapping_with_cursor,
                                            ignore_left_of_cursor=ignore_left_of_cursor,
                                            ignore_right_of_cursor=ignore_right_of_cursor,
                                            start_sel=start_sel,
                                            end_sel=end_sel)
        self.assert_equal(0, result, "ignore_occurence, overlapping regions should fail, non overlapping regions")

    def test_This_is_how_you_get_to_nearest_if_selection_is_there_already(self):
        self._open_empty_test_file('temp.py')
        self._insert_in_active_buffer('small = small + "abc"\nlarge = large + "def"\n')

        # until, cursor at pos already, take next one        
        self._say("after abc")
        self._assert_active_buffer_content_is(\
'''small = small + "abc<CURSOR>"
large = large + "def"
''')
        self._say(["select until", '"\\close-quote'])
        self._assert_active_buffer_content_with_selection_is(\
'''small = small + "abc<SEL_START>"
large = large + "def<SEL_END>"
''')

        # through, cursor at pos already, take this one:
        self._say("after abc")
        self._assert_active_buffer_content_is(\
'''small = small + "abc<CURSOR>"
large = large + "def"
''')
        self._say(["select through", '"\\close-quote'])
        self._assert_active_buffer_content_with_selection_is(\
'''small = small + "abc<SEL_START>"<SEL_END>
large = large + "def"
''')

    def test_This_test_of_enough_ranges_in_large_text(self):

        # large file, in order to test the visible range also
        # and more occurrences of ")" than can be held in the NatSpeak/natlink
        # range of ranges, VoiceCode must enhance this list!
        self._open_file(self._get_test_data_file_path('lots_of_parens_py'))
        self._goto_line(290)
        self._say("select center")
        self._say(["select through", ")\\close-paren"])
        self._assert_lines_with_selection_content_is(\
'''   <SEL_START>center = 1
   calc5 = (x.function1()<SEL_END> + y.function2()) /(z.function1() + z.function2())''')
        self._say(["next one"])
        self._assert_lines_with_selection_content_is(\
'''   <SEL_START>center = 1
   calc5 = (x.function1() + y.function2()<SEL_END>) /(z.function1() + z.function2())''')
        self._say(["previous one"])
        self._say(["previous one"])
        self._say(["previous one"])
        self._say(["previous one"])
        self._say(["previous one"])
        self._say(["previous one"])
        self._say(["previous one"])
        self._say(["previous one"])
        self._assert_lines_with_selection_content_is(\
'''   calc3 = (x.function1() + y.function2()) /( z.function1() + z.function2()<SEL_START>)
   calc4 = (x.function1() + y.function2()) /( z.function1() + z.function2())
   center<SEL_END> = 1''')

        
    def test_This_test_of_lots_of_through_ranges(self):

        # file with a lot of occurrences of x through y.
        # special routines have to search for the failing natlink/natspeak ranges list
        #
        # range of ranges, VoiceCode must enhance this list!
        self._open_file(self._get_test_data_file_path('lots_of_selections_py'))
        self._goto_line(30)
        self._say("select center")
        # problem NatSpeak 9, x\\X. does not work, probably we should add x\\X. in voc
        self._say(["select", "x\\xray", "through", ")\\close-paren"])
        self._assert_lines_with_selection_content_is(\
'''   calc5 = (<SEL_START>x.function1()<SEL_END> + y.function2()) /(z.function1() + z.function2())''')

        self._say(["previous one"])
        self._say(["previous one"])
        self._say(["previous one"])
        self._say(["previous one"])
        self._assert_lines_with_selection_content_is(\
'''   calc1 = (<SEL_START>x.function1(a, c, b)<SEL_END> + y.function2()) /( z.function1() + z.function2())''')
        
        self._say(["previous one"])
        self._assert_lines_with_selection_content_is(\
'''   <SEL_START>x = Lots(1, 2)<SEL_END>''')
## going on further seems instable, leave for the moment, QH

        
    def test_This_test_lots_of_combined_ranges(self):

        # file with a lot of occurrences of function one, even function/one.
        # special routines have to search for the failing natlink/natspeak ranges list
        #
        # range of ranges, VoiceCode must enhance this list!
        self._open_file(self._get_test_data_file_path('lots_of_selections_py'))
        self._goto_line(4)
        self._say(["select", "function", "one"])
        self._assert_lines_with_selection_content_is(\
'''# words to recognise: <SEL_START>function one<SEL_END>, function-one, function-1, function 1.''')

        self._say(["next one"])
        self._assert_lines_with_selection_content_is(\
'''# words to recognise: function one, <SEL_START>function-one<SEL_END>, function-1, function 1.''')
        self._say(["next one"])
        self._assert_lines_with_selection_content_is(\
'''# words to recognise: function one, function-one, <SEL_START>function-1<SEL_END>, function 1.''')
        self._say(["next one"])
        self._assert_lines_with_selection_content_is(\
'''# words to recognise: function one, function-one, function-1, <SEL_START>function 1<SEL_END>.''')
        self._say(["next one"])
        self._assert_lines_with_selection_content_is(\
'''   def <SEL_START>function1<SEL_END>(self):''')


###############################################################
# Assertions.
# 
# Use these methods to check the state of the class.
###############################################################
