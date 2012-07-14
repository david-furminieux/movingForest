
from datetime import date, timedelta
from taj.alu.any import StackALU
from taj.alu.visit import ExpressionEvalBuilder, LogicBuilder
from taj.exception import UnknownFunction
from taj.parser.MFQLLexer import MFQLLexer
from taj.parser.MFQLParser import MFQLParser
import antlr3
import logging
import unittest

class CompositeBuilder(object):
    '''
    a composition possibility for the builders.
    '''
    def __init__(self):
        super(CompositeBuilder, self).__init__()
        self._comoponents = []
    
    def addComponent(self, cmpnt):
        self._comoponents.append(cmpnt)
    
    def __getattr__(self, name):
        def distrib(name, elems, *args):
            for elem in elems:
                meth = getattr(elem, name)
                meth(*args)
        return lambda *args: distrib(name, self._comoponents, *args)

class VerboseBuilder(object):
    '''
    verbosing informations for builders.
    @see CompositeBuilder
    '''
    def __init__(self):
        self._logger = logging.getLogger(__name__+'.'+self.__class__.__name__)
    
    def printSeparation(self):
        self._logger.info('----------------------------------------------------')
    
    def __getattr__(self, name):
        return lambda *args: self._logger.info(name) 

class Test(unittest.TestCase):

    def setUp(self):
        self.parse
        self.alu = StackALU()
        #self.alu = VerboseAlu(self.alu)

    def parse(self, rule, input):
        char_stream = antlr3.ANTLRStringStream(input)
        lexer = MFQLLexer(char_stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = MFQLParser(tokens)
        
        rule = getattr(parser, rule)
        result = rule()
        parser.eof()
        return result
    
    def evalExpr(self, tree, ast):
        expr = ExpressionEvalBuilder(self.alu)
        
        builder = CompositeBuilder()
        builder.addComponent(VerboseBuilder())
        builder.addComponent(expr)
        
        ast.walk(builder)
        
        func = expr.getResult()
        assert func is not None
        return func(tree)
    
    def evalLogic(self, tree, ast):
        logic = LogicBuilder(self.alu)
        ast.walk(logic)
        
        func = logic.getResult()
        return func(tree)

    def tearDown(self):
        pass

    def testConstant(self):
        value = self.evalExpr({}, self.parse('expr', '1'))
        self.assertTrue(value is not None)
        self.assertTrue(value == 1)
        
        value = self.evalExpr({}, self.parse('expr', '1.2'))
        self.assertTrue(value is not None)
        self.assertTrue(value == 1.2)
        
        value = self.evalExpr({}, self.parse('expr', 'null'))
        self.assertTrue(value is None)
        
        value = self.evalExpr({}, self.parse('expr', "'hello'"))
        self.assertTrue(value is not None)
    
    def testAddition(self):
        value = self.evalExpr({}, self.parse('expr', '1+2'))
        self.assertTrue(value is not None)
        self.assertTrue(value == 3)
        
        value = self.evalExpr({}, self.parse('expr', '1-2'))
        self.assertTrue(value is not None)
        self.assertTrue(value == -1)
        
        value = self.evalExpr({}, self.parse('expr', '1+null'))
        self.assertTrue(value is None)

        value = self.evalExpr({}, self.parse('expr', 'null+1'))
        self.assertTrue(value is None)
    
    def testMult(self):
        value = self.evalExpr({}, self.parse('expr', '1*2'))
        self.assertTrue(value is not None)
        self.assertTrue(value == 2)
        
        value = self.evalExpr({}, self.parse('expr', '3/2'))
        self.assertTrue(value is not None)
        self.assertTrue(value == 1)
        
        value = self.evalExpr({}, self.parse('expr', '3/2.0'))
        self.assertTrue(value is not None)
        self.assertTrue(value == 1.5)
        
        value = self.evalExpr({}, self.parse('expr', '3 % 2'))
        self.assertTrue(value is not None)
        self.assertTrue(value == 1)
    
    def testPrecedence(self):
        
        value = self.evalExpr({}, self.parse('expr', '1+2*3'))
        self.assertTrue(value == 7)
        
        value = self.evalExpr({}, self.parse('expr', '2*3+1'))
        self.assertTrue(value == 7)
        
    def testLogic(self):
        value = self.evalLogic({}, self.parse('predicate', 'true'))
        self.assertTrue(value)
        
        value = self.evalLogic({}, self.parse('predicate', 'false'))
        self.assertTrue(not value)
        
        value = self.evalLogic({}, self.parse('predicate', 'not true'))
        self.assertTrue(not value)
        
        value = self.evalLogic({}, self.parse('predicate', 'not false'))
        self.assertTrue(value)
        
        value = self.evalLogic({}, self.parse('predicate', 'true and false'))
        self.assertTrue(not value)
        
        value = self.evalLogic({}, self.parse('predicate', 'false and true'))
        self.assertTrue(not value)
        
        value = self.evalLogic({}, self.parse('predicate', 'false or true'))
        self.assertTrue(value)
        
    def testTime(self):
        value = self.evalExpr({}, self.parse('expr', "date('2010-01-01')"))
        self.assertTrue(isinstance(value, date))
        self.assertTrue(value.year == 2010)
        self.assertTrue(value.month == 01)
        self.assertTrue(value.day == 1)
        
        value = self.evalLogic({}, self.parse('predicate', """
            date('2010-01-01') > date('2009-01-01')
        """))
        self.assertTrue(value)
    
    def testFuntion(self):
        exp = False
        try:
            self.evalExpr({}, self.parse('expr', 'illegal(1)'))
        except UnknownFunction:
            exp = True
        self.assertTrue(exp)

        value = self.evalExpr({}, self.parse('expr', "str(int('1') + int('2'))"))
        self.assertTrue(value=='3')
        
        value = self.evalExpr({}, self.parse('expr', """
           date('2011-01-01') - date('2010-01-01')
        """))
        self.assertTrue(isinstance(value, timedelta))
        self.assertTrue(value == timedelta(365))
    
    def testVariable(self):
        
        value = self.evalExpr({"a": 1, "b": 2}, self.parse('expr',
        '''
          a + b + 1
        '''))
        self.assertTrue(value == 4)
    
    def testPath(self):
        value = self.evalExpr({'a': 1} , self.parse('path', '.'))
        self.assertTrue(value == {'a': 1})
        
        value = self.evalExpr({'a': 1} , self.parse('path', '.a'))
        self.assertTrue(value == 1)
        
        value = self.evalExpr({'a': 1} , self.parse('path', 'a'))
        self.assertTrue(value == 1)
        
        value = self.evalExpr({'a': [1]} , self.parse('path', '.a[0]'))
        self.assertTrue(value == 1)
        
        value = self.evalExpr({'a': [1]} , self.parse('path', '.a[2]'))
        self.assertTrue(value is None)
        
        value = self.evalExpr(None , self.parse('path', '.a'))
        self.assertTrue(value is None)
        
        value = self.evalExpr({'a': 1} , self.parse('path', '.b'))
        self.assertTrue(value is None)
    
    def testComparison(self):

        value = self.evalLogic({} , self.parse('predicate', '1<=2'))
        self.assertTrue(value)
        
        value = self.evalLogic({} , self.parse('predicate', '1<=1'))
        self.assertTrue(value)
        
        value = self.evalLogic({} , self.parse('predicate', '1<1'))
        self.assertTrue(not value)
        
        value = self.evalLogic({} , self.parse('predicate', '1>=2'))
        self.assertTrue(not value)
        
        value = self.evalLogic({} , self.parse('predicate', '1>=1'))
        self.assertTrue(value)
        
        value = self.evalLogic({} , self.parse('predicate', '1>1'))
        self.assertTrue(not value)

        value = self.evalLogic({} , self.parse('predicate', '1<>1'))
        self.assertTrue(not value)

        value = self.evalLogic({} , self.parse('predicate', '1!=1'))
        self.assertTrue(not value)
        
        value = self.evalLogic({} , self.parse('predicate', '1><1'))
        self.assertTrue(value)

#        value = self.evalLogic({} , self.parse('predicate', '1>>a'))
#        self.assertTrue(not value)
#
#        value = self.evalLogic({} , self.parse('predicate', 'a<<1'))
#        self.assertTrue(not value)

        
#    def testSelector(self):
#        
#        bookStore = {
#          "store": {
#            "book": [ 
#              {
#                "category": "reference",
#                "author": "Nigel Rees",
#                "title": "Sayings of the Century",
#                "price": 8.95
#              },
#              {
#                "category": "fiction",
#                "author": "Evelyn Waugh",
#                "title": "Sword of Honour",
#                "price": 12.99
#              },
#              {
#                "category": "fiction",
#                "author": "Herman Melville",
#                "title": "Moby Dick",
#                "isbn": "0-553-21311-3",
#                "price": 8.99
#              },
#              {
#                "category": "fiction",
#                "author": "J. R. R. Tolkien",
#                "title": "The Lord of the Rings",
#                "isbn": "0-395-19395-8",
#                "price": 22.99
#              }],
#            "bicycle": { "color": "red", "price": 19.95}
#          }
#        }
#        
#        value = self.alu.evalExpr({'a': {'b': 1}} , self.parse('selector', 'a'))
#        self.assertTrue(value == {'b': 1})
#        
#        value = self.alu.evalExpr({'a': {'b': 1}} , self.parse('selector', 'b'))
#        self.assertTrue(value is None)
#        
#        value = self.alu.evalExpr({'a': [1]} , self.parse('selector', 'a[3]'))
#        self.assertTrue(value is None)
#        
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.'))
#        self.assertTrue(value == bookStore)
#        
#        value = self.alu.evalExpr(bookStore, self.parse('selector', 'store'))
#        self.assertTrue(value == bookStore['store'])
#        
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.store'))
#        self.assertTrue(value == bookStore['store'])
#
#        value = self.alu.evalExpr(bookStore, self.parse('selector', 'store.book'))
#        self.assertTrue(value == bookStore['store']['book'])
#        
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.store.book'))
#        self.assertTrue(value == bookStore['store']['book'])
#
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.store.book[2]'))
#        self.assertTrue(value == bookStore['store']['book'][2])
#
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.store.book[*].author'))
#
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '..store'))
#        self.assertTrue(value == bookStore['store'])
#
#        
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.store.book[store.bla]'))
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.store.book[-1]'))
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.store.book[1:3]'))
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.store.book[:3]'))
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.store.book[1:3:2]'))
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.store.book[2].title'))
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.[..author IS KEY]'))
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.store.*'))
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.store[..price is key]'))
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.[@..book[2] is null]'))
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.book[0,3]'))
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.[..book[@.isbn] is key]'))
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.book[@.price<10]'))
#        
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.store.book[ @.price>10 and @.price<20]'))
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.store.book[ @.price<10, @.price>20]'))
#
#        value = self.alu.evalExpr(bookStore, self.parse('selector', '.store.book[.length<10]'))
# /store/book/author   $.store.book[*].author the authors of all books in the store
# //author             $..author              all authors
# /store/*             $.store.*              all things in store, which are some books and a red bicycle.
# /store//price        $.store..price         the price of everything in the store.
# //book[3]            $..book[2]             the third book
# //book[last()]       $..book[-1:]           the last book in order.
# //book[position()<3] $..book[0,1]
#                      $..book[:2]            the first two books
# //book[isbn]         $..book[?(@.isbn)]     filter all books with isbn number
# //book[price<10]     $..book[?(@.price<10)] filter all books cheapier than 10
# //*                  $..*                   all Elements in XML document. All members of JSON structure.
  
    def testPattern(self):
        
        value = self.evalExpr({}, self.parse('pattern', '''
            {
              "a": 1,
              "b": 1.2,
              "c": [1,2,3],
              #"d": true,  # logic not allowed for now
              "e": "hallo",
              "f": {"f1": "bla"}
            }
        '''))
        self.assertTrue(value == {
              "a": 1,
              "b": 1.2,
              "c": [1,2,3],
              #"d": True,
              "e": "hallo",
              "f": {"f1": "bla"}
            })
        
        value = self.evalExpr({'a':1}, self.parse('expr', '''
           {
             "b": a
           }
        '''))
        self.assertTrue(value=={'b':1})
    
    def testSpecialLogic(self):
        value = self.evalLogic({'a':None}, self.parse('predicate', '''
            a IS NULL
        '''))
        self.assertTrue(value is True)
        
        value = self.evalLogic({'a':1}, self.parse('predicate', '''
            a IS NULL
        '''))
        self.assertTrue(value is False)
        
        value = self.evalLogic({'a':None}, self.parse('predicate', '''
            a IS KEY
        '''))
        self.assertTrue(value is True)
        
        value = self.evalLogic({'b':None}, self.parse('predicate', '''
            a IS KEY
        '''))
        self.assertTrue(value is False)
        
if __name__ == "__main__":
    unittest.main()
