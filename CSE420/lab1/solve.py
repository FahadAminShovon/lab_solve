from typing import List
import re

KEYWORD_REGEX = "int|float|double|string|if|else"
MATH_OPERATOR_REGEX = "\+|-|\*|\/|\="
LOGICAL_OPERATOR_REGEX = "\>|\<|(==)|(\>=)"
OTHERS_REGEX = ",|\;|\|\(|\)|\{|\}|\[|\]"
IDENTIFIER_REGEX = "^[A-Za-z_][A-Za-z0-9_]*"
NUMERIC_REGEX = "[-]?([\d]*[\.]?[\d]+)"

class Solve:
    def __init__(self, file_path):
        self.file = file_path
        self.keyword_list = set()
        self.math_operator_list = set()
        self.logical_operator_list = set()
        self.others_list = set()
        self.identifier_list = set()
        self.numeric_list = set()

    def splitter(self, string:str)->List:
        string.strip()
        return string.split()

    def remove_symbol(self, string):
        symbols = "+-*/++--,;><>=<==="
        if (len(string) > 1):
            if string[-1] in symbols:
                string = string[:-1]
            elif string[0] in symbols:
                string = string[1:]
        return string

    def matcher(self,string,regex,items:set, identifier_of_numeric=False)->List:
        if identifier_of_numeric:
            if re.match(KEYWORD_REGEX, string) or re.match(OTHERS_REGEX, string):
                return items
            string = self.remove_symbol(string)

        matched_string = re.match(regex, string)
        if re.match(regex, string[-1]): items.add(string[-1])
        if matched_string:
            items.add(matched_string.group())
        return items
    
    def parser(self, line):
        for word in self.splitter(line):
            self.matcher(word, KEYWORD_REGEX, self.keyword_list)
            self.matcher(word, MATH_OPERATOR_REGEX, self.math_operator_list)
            self.matcher(word, LOGICAL_OPERATOR_REGEX, self.logical_operator_list)
            self.matcher(word, OTHERS_REGEX, self.others_list)
            self.matcher(word, IDENTIFIER_REGEX, self.identifier_list, identifier_of_numeric=True)
            self.matcher(word, NUMERIC_REGEX, self.numeric_list, identifier_of_numeric=True)

    def printer(self, name, lst):
        print(name, end =": ");
        list_to_set = list(lst);
        if(len(list_to_set) > 0): print(list_to_set[0], end = " ")
        for i in range (1, len(list_to_set)):
            print(",",list_to_set[i], end = " ")
        print()

    def result(self):
        self.printer("Keywords", self.keyword_list)
        self.printer("Identifiers", self.identifier_list)   
        self.printer("Math Operators", self.math_operator_list)   
        self.printer("Logical Operators", self.logical_operator_list)        
        self.printer("Numerical Values", self.numeric_list)   
        self.printer("Others", self.others_list)   

    def analyze(self):
        with open(self.file, 'r') as file:
            Lines = file.readlines()
            for line in Lines:
                self.parser(line)


if __name__ == "__main__":
    solve = Solve('./input.txt')
    solve.analyze()
    solve.result()