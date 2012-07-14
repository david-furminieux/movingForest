from taj.parser.MFQLLexer import MFQLLexer
from taj.parser.MFQLParser import MFQLParser
from taj.parser.visitor import CompositeVisitor, IsKeyValidator
import antlr3
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def parse(self, rule, input):
        char_stream = antlr3.ANTLRStringStream(input)
        lexer = MFQLLexer(char_stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = MFQLParser(tokens)
        
        rule = getattr(parser, rule)
        result = rule()
        parser.eof()
        
        validator = CompositeVisitor()
        validator.addComponent(IsKeyValidator())

        if isinstance(result, list):
            for elem in result:
                elem.walk(validator)
        else:
            result.walk(validator)
        
        return result

    def testIntro(self):
        
        result = self.parse('stmts', '''
          SELECT
            p.price AS price
          FROM items[ROWS 5] AS i, priceTable AS p
          WHERE i.item_id = p.item_id;
        ''')
        self.assertTrue(result is not None)

        result = self.parse('stmts', '''
          CREATE TABLE carSeg AS SELECT
            car_id, speed, exp_way, lane, dir, (x_pos/52800) AS seg
          FROM
            carLoc;
        ''')



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()