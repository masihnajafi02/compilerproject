from declarations import Nonterminalstates as NT, LanguageRules, Transition, TokenType, Token_ID

lang_main_keywords = ['break', 'else', 'if', 'int', 'repeat', 'return', 'until', 'void']
input_file = "input.txt"
tokens_file = "tokens.txt"
lexical_error_file_name = "lexical_errors.txt"
symbol_table_file_name = "symbol_table.txt"
parse_tree_save_file = "parse_tree.txt"
syntax_errors_file = "syntax_errors.txt"
epsilon = "epsilon"


class LanguageRules:
    first: list[str]
    follow: list[str]

    def __init__(self, first, follow):
        self.first = first
        self.follow = follow


LANG_RULES_INFO: dict[NT, LanguageRules] = {
    NT.PROGRAM: LanguageRules(
        [
            Token_ID(TokenType.KEYWORD, "int"), Token_ID(TokenType.KEYWORD, "void"), epsilon
        ],
        [
            Token_ID(TokenType.EOF, "$")
        ]),
    NT.DECLARATION_LIST: LanguageRules(
        [
            Token_ID(TokenType.KEYWORD, "int"), Token_ID(TokenType.KEYWORD, "void"), epsilon
        ],
        [
            Token_ID(TokenType.EOF, "$"), TokenType.ID, Token_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            Token_ID(TokenType.SYMBOL, "("),
            Token_ID(TokenType.SYMBOL, "{"), Token_ID(TokenType.SYMBOL, "}"), Token_ID(TokenType.KEYWORD, "break"),
            Token_ID(TokenType.KEYWORD, "if"),
            Token_ID(TokenType.KEYWORD, "repeat"), Token_ID(TokenType.KEYWORD, "return")
        ]
    ),
    NT.DECLARATION: LanguageRules(
        [
            Token_ID(TokenType.KEYWORD, "int"), Token_ID(TokenType.KEYWORD, "void")
        ],
        [
            Token_ID(TokenType.EOF, "$"), TokenType.ID, Token_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            Token_ID(TokenType.SYMBOL, "("),
            Token_ID(TokenType.SYMBOL, "{"), Token_ID(TokenType.SYMBOL, "}"), Token_ID(TokenType.KEYWORD, "break"),
            Token_ID(TokenType.KEYWORD, "if"),
            Token_ID(TokenType.KEYWORD, "repeat"), Token_ID(TokenType.KEYWORD, "return"),
            Token_ID(TokenType.KEYWORD, "int"), Token_ID(TokenType.KEYWORD, "void")
        ]
    ),
    NT.DECLARATION_INITIAL: LanguageRules(
        [
            Token_ID(TokenType.KEYWORD, "int"), Token_ID(TokenType.KEYWORD, "void")
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "["), Token_ID(TokenType.SYMBOL, "("),
            Token_ID(TokenType.SYMBOL, ")"), Token_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.DECLARATION_PRIME: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "["), Token_ID(TokenType.SYMBOL, "(")
        ],
        [
            Token_ID(TokenType.EOF, "$"), TokenType.ID, Token_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            Token_ID(TokenType.SYMBOL, "("),
            Token_ID(TokenType.SYMBOL, "{"), Token_ID(TokenType.SYMBOL, "}"), Token_ID(TokenType.KEYWORD, "break"),
            Token_ID(TokenType.KEYWORD, "if"),
            Token_ID(TokenType.KEYWORD, "repeat"), Token_ID(TokenType.KEYWORD, "return"),
            Token_ID(TokenType.KEYWORD, "int"), Token_ID(TokenType.KEYWORD, "void")
        ]
    ),
    NT.VAR_DECLARATION_PRIME: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "[")
        ],
        [
            Token_ID(TokenType.EOF, "$"), TokenType.ID, Token_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            Token_ID(TokenType.SYMBOL, "("),
            Token_ID(TokenType.SYMBOL, "{"), Token_ID(TokenType.SYMBOL, "}"), Token_ID(TokenType.KEYWORD, "break"),
            Token_ID(TokenType.KEYWORD, "if"),
            Token_ID(TokenType.KEYWORD, "repeat"), Token_ID(TokenType.KEYWORD, "return"),
            Token_ID(TokenType.KEYWORD, "int"), Token_ID(TokenType.KEYWORD, "void")
        ]
    ),
    NT.FUN_DECLARATION_PRIME: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, "(")
        ],
        [
            Token_ID(TokenType.EOF, "$"), TokenType.ID, Token_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            Token_ID(TokenType.SYMBOL, "("),
            Token_ID(TokenType.SYMBOL, "{"), Token_ID(TokenType.SYMBOL, "}"), Token_ID(TokenType.KEYWORD, "break"),
            Token_ID(TokenType.KEYWORD, "if"),
            Token_ID(TokenType.KEYWORD, "repeat"), Token_ID(TokenType.KEYWORD, "return"),
            Token_ID(TokenType.KEYWORD, "int"), Token_ID(TokenType.KEYWORD, "void")
        ]
    ),
    NT.TYPE_SPECIFIER: LanguageRules(
        [
            Token_ID(TokenType.KEYWORD, "int"), Token_ID(TokenType.KEYWORD, "void")
        ],
        [
            TokenType.ID
        ]
    ),
    NT.PARAMS: LanguageRules(
        [
            Token_ID(TokenType.KEYWORD, "int"), Token_ID(TokenType.KEYWORD, "void")
        ],
        [
            Token_ID(TokenType.SYMBOL, ")")
        ]
    ),
    NT.PARAM_LIST: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, ","), epsilon
        ],
        [
            Token_ID(TokenType.SYMBOL, ")")
        ]
    ),
    NT.PARAM: LanguageRules(
        [
            Token_ID(TokenType.KEYWORD, "int"), Token_ID(TokenType.KEYWORD, "void")
        ],
        [
            Token_ID(TokenType.SYMBOL, ")"), Token_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.PARAM_PRIME: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, "["), epsilon
        ],
        [
            Token_ID(TokenType.SYMBOL, ")"), Token_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.COMPOUND_STMT: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, "{")
        ],
        [
            Token_ID(TokenType.EOF, "$"), TokenType.ID, Token_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            Token_ID(TokenType.SYMBOL, "("),
            Token_ID(TokenType.SYMBOL, "{"), Token_ID(TokenType.SYMBOL, "}"), Token_ID(TokenType.KEYWORD, "break"),
            Token_ID(TokenType.KEYWORD, "if"),
            Token_ID(TokenType.KEYWORD, "repeat"), Token_ID(TokenType.KEYWORD, "return"),
            Token_ID(TokenType.KEYWORD, "int"), Token_ID(TokenType.KEYWORD, "void"),
            Token_ID(TokenType.KEYWORD, "else"), Token_ID(TokenType.KEYWORD, "until")
        ]
    ),
    NT.STATEMENT_LIST: LanguageRules(
        [
            TokenType.ID, Token_ID(TokenType.SYMBOL, ";"), TokenType.NUM, Token_ID(TokenType.SYMBOL, "("),
            Token_ID(TokenType.SYMBOL, "{"), Token_ID(TokenType.KEYWORD, "break"), Token_ID(TokenType.KEYWORD, "if"),
            Token_ID(TokenType.KEYWORD, "repeat"), Token_ID(TokenType.KEYWORD, "return"), epsilon
        ],
        [
            Token_ID(TokenType.SYMBOL, "}")
        ]
    ),
    NT.STATEMENT: LanguageRules(
        [
            TokenType.ID, Token_ID(TokenType.SYMBOL, ";"), TokenType.NUM, Token_ID(TokenType.SYMBOL, "("),
            Token_ID(TokenType.SYMBOL, "{"), Token_ID(TokenType.KEYWORD, "break"), Token_ID(TokenType.KEYWORD, "if"),
            Token_ID(TokenType.KEYWORD, "repeat"), Token_ID(TokenType.KEYWORD, "return")
        ],
        [
            TokenType.ID, Token_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            Token_ID(TokenType.SYMBOL, "("),
            Token_ID(TokenType.SYMBOL, "{"), Token_ID(TokenType.SYMBOL, "}"), Token_ID(TokenType.KEYWORD, "break"),
            Token_ID(TokenType.KEYWORD, "if"),
            Token_ID(TokenType.KEYWORD, "repeat"), Token_ID(TokenType.KEYWORD, "return"),
            Token_ID(TokenType.KEYWORD, "else"), Token_ID(TokenType.KEYWORD, "until")
        ]
    ),
    NT.EXPRESSION_STMT: LanguageRules(
        [
            TokenType.ID, Token_ID(TokenType.SYMBOL, ";"), TokenType.NUM, Token_ID(TokenType.SYMBOL, "("),
            Token_ID(TokenType.KEYWORD, "break")
        ],
        [
            TokenType.ID, Token_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            Token_ID(TokenType.SYMBOL, "("),
            Token_ID(TokenType.SYMBOL, "{"), Token_ID(TokenType.SYMBOL, "}"), Token_ID(TokenType.KEYWORD, "break"),
            Token_ID(TokenType.KEYWORD, "if"),
            Token_ID(TokenType.KEYWORD, "repeat"), Token_ID(TokenType.KEYWORD, "return"),
            Token_ID(TokenType.KEYWORD, "else"), Token_ID(TokenType.KEYWORD, "until")
        ]
    ),
    NT.SELECTION_STMT: LanguageRules(
        [
            Token_ID(TokenType.KEYWORD, "if")
        ],
        [
            TokenType.ID, Token_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            Token_ID(TokenType.SYMBOL, "("),
            Token_ID(TokenType.SYMBOL, "{"), Token_ID(TokenType.SYMBOL, "}"), Token_ID(TokenType.KEYWORD, "break"),
            Token_ID(TokenType.KEYWORD, "if"),
            Token_ID(TokenType.KEYWORD, "repeat"), Token_ID(TokenType.KEYWORD, "return"),
            Token_ID(TokenType.KEYWORD, "else"), Token_ID(TokenType.KEYWORD, "until")
        ]
    ),
    NT.ITERATION_STMT: LanguageRules(
        [
            Token_ID(TokenType.KEYWORD, "repeat")
        ],
        [
            TokenType.ID, Token_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            Token_ID(TokenType.SYMBOL, "("),
            Token_ID(TokenType.SYMBOL, "{"), Token_ID(TokenType.SYMBOL, "}"), Token_ID(TokenType.KEYWORD, "break"),
            Token_ID(TokenType.KEYWORD, "if"),
            Token_ID(TokenType.KEYWORD, "repeat"), Token_ID(TokenType.KEYWORD, "return"),
            Token_ID(TokenType.KEYWORD, "else"), Token_ID(TokenType.KEYWORD, "until")
        ]
    ),
    NT.RETURN_STMT: LanguageRules(
        [
            Token_ID(TokenType.KEYWORD, "return")
        ],
        [
            TokenType.ID, Token_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            Token_ID(TokenType.SYMBOL, "("),
            Token_ID(TokenType.SYMBOL, "{"), Token_ID(TokenType.SYMBOL, "}"), Token_ID(TokenType.KEYWORD, "break"),
            Token_ID(TokenType.KEYWORD, "if"),
            Token_ID(TokenType.KEYWORD, "repeat"), Token_ID(TokenType.KEYWORD, "return"),
            Token_ID(TokenType.KEYWORD, "else"), Token_ID(TokenType.KEYWORD, "until")
        ]
    ),
    NT.RETURN_STMT_PRIME: LanguageRules(
        [
            TokenType.ID, Token_ID(TokenType.SYMBOL, ";"), TokenType.NUM, Token_ID(TokenType.SYMBOL, "(")
        ],
        [
            TokenType.ID, Token_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            Token_ID(TokenType.SYMBOL, "("),
            Token_ID(TokenType.SYMBOL, "{"), Token_ID(TokenType.SYMBOL, "}"), Token_ID(TokenType.KEYWORD, "break"),
            Token_ID(TokenType.KEYWORD, "if"),
            Token_ID(TokenType.KEYWORD, "repeat"), Token_ID(TokenType.KEYWORD, "return"),
            Token_ID(TokenType.KEYWORD, "else"), Token_ID(TokenType.KEYWORD, "until")
        ]
    ),
    NT.EXPRESSION: LanguageRules(
        [
            TokenType.ID, TokenType.NUM, Token_ID(TokenType.SYMBOL, "(")
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.B: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, "["), Token_ID(TokenType.SYMBOL, "("), Token_ID(TokenType.SYMBOL, "="),
            Token_ID(TokenType.SYMBOL, "<"), Token_ID(TokenType.SYMBOL, "=="), Token_ID(TokenType.SYMBOL, "+"),
            Token_ID(TokenType.SYMBOL, "-"), Token_ID(TokenType.SYMBOL, "*"), epsilon
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.H: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, "="),
            Token_ID(TokenType.SYMBOL, "<"), Token_ID(TokenType.SYMBOL, "=="), Token_ID(TokenType.SYMBOL, "+"),
            Token_ID(TokenType.SYMBOL, "-"), Token_ID(TokenType.SYMBOL, "*"), epsilon
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.SIMPLE_EXPRESSION_ZEGOND: LanguageRules(
        [
            TokenType.NUM, Token_ID(TokenType.SYMBOL, "(")
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.SIMPLE_EXPRESSION_PRIME: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, "("),
            Token_ID(TokenType.SYMBOL, "<"), Token_ID(TokenType.SYMBOL, "=="), Token_ID(TokenType.SYMBOL, "+"),
            Token_ID(TokenType.SYMBOL, "-"), Token_ID(TokenType.SYMBOL, "*"), epsilon
        ],
        [

            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.C: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, "<"), Token_ID(TokenType.SYMBOL, "=="), epsilon
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.RELOP: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, "<"), Token_ID(TokenType.SYMBOL, "==")
        ],
        [
            TokenType.ID, TokenType.NUM, Token_ID(TokenType.SYMBOL, "(")
        ]
    ),
    NT.ADDITIVE_EXPRESSION: LanguageRules(
        [
            TokenType.ID, TokenType.NUM, Token_ID(TokenType.SYMBOL, "(")
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.ADDITIVE_EXPRESSION_PRIME: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, "("), Token_ID(TokenType.SYMBOL, "+"),
            Token_ID(TokenType.SYMBOL, "-"), Token_ID(TokenType.SYMBOL, "*"), epsilon
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ","), Token_ID(TokenType.SYMBOL, "<"), Token_ID(TokenType.SYMBOL, "==")
        ]
    ),
    NT.ADDITIVE_EXPRESSION_ZEGOND: LanguageRules(
        [
            TokenType.NUM, Token_ID(TokenType.SYMBOL, "(")
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ","), Token_ID(TokenType.SYMBOL, "<"), Token_ID(TokenType.SYMBOL, "==")
        ]
    ),
    NT.D: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, "+"), Token_ID(TokenType.SYMBOL, "-"), epsilon
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ","), Token_ID(TokenType.SYMBOL, "<"), Token_ID(TokenType.SYMBOL, "==")
        ]
    ),
    NT.ADDOP: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, "+"), Token_ID(TokenType.SYMBOL, "-")
        ],
        [
            TokenType.ID, TokenType.NUM, Token_ID(TokenType.SYMBOL, "(")
        ]
    ),
    NT.TERM: LanguageRules(
        [
            TokenType.ID, TokenType.NUM, Token_ID(TokenType.SYMBOL, "(")
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ","), Token_ID(TokenType.SYMBOL, "<"), Token_ID(TokenType.SYMBOL, "=="),
            Token_ID(TokenType.SYMBOL, "+"), Token_ID(TokenType.SYMBOL, "-")
        ]
    ),
    NT.TERM_PRIME: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, "("), Token_ID(TokenType.SYMBOL, "*"), epsilon
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ","), Token_ID(TokenType.SYMBOL, "<"), Token_ID(TokenType.SYMBOL, "=="),
            Token_ID(TokenType.SYMBOL, "+"), Token_ID(TokenType.SYMBOL, "-")
        ]
    ),
    NT.TERM_ZEGOND: LanguageRules(
        [
            TokenType.NUM, Token_ID(TokenType.SYMBOL, "(")
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ","), Token_ID(TokenType.SYMBOL, "<"), Token_ID(TokenType.SYMBOL, "=="),
            Token_ID(TokenType.SYMBOL, "+"), Token_ID(TokenType.SYMBOL, "-")
        ]
    ),
    NT.G: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, "*"), epsilon
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ","), Token_ID(TokenType.SYMBOL, "<"), Token_ID(TokenType.SYMBOL, "=="),
            Token_ID(TokenType.SYMBOL, "+"), Token_ID(TokenType.SYMBOL, "-")
        ]
    ),
    NT.FACTOR: LanguageRules(
        [
            TokenType.ID, TokenType.NUM, Token_ID(TokenType.SYMBOL, "(")
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ","), Token_ID(TokenType.SYMBOL, "<"), Token_ID(TokenType.SYMBOL, "=="),
            Token_ID(TokenType.SYMBOL, "+"), Token_ID(TokenType.SYMBOL, "-"), Token_ID(TokenType.SYMBOL, "*")
        ]
    ),
    NT.VAR_CALL_PRIME: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, "["), Token_ID(TokenType.SYMBOL, "("), epsilon
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ","), Token_ID(TokenType.SYMBOL, "<"), Token_ID(TokenType.SYMBOL, "=="),
            Token_ID(TokenType.SYMBOL, "+"), Token_ID(TokenType.SYMBOL, "-"), Token_ID(TokenType.SYMBOL, "*")
        ]
    ),
    NT.VAR_PRIME: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, "["), epsilon
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ","), Token_ID(TokenType.SYMBOL, "<"), Token_ID(TokenType.SYMBOL, "=="),
            Token_ID(TokenType.SYMBOL, "+"), Token_ID(TokenType.SYMBOL, "-"), Token_ID(TokenType.SYMBOL, "*")
        ]
    ),
    NT.FACTOR_PRIME: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, "("), epsilon
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ","), Token_ID(TokenType.SYMBOL, "<"), Token_ID(TokenType.SYMBOL, "=="),
            Token_ID(TokenType.SYMBOL, "+"), Token_ID(TokenType.SYMBOL, "-"), Token_ID(TokenType.SYMBOL, "*")
        ]
    ),
    NT.FACTOR_ZEGOND: LanguageRules(
        [
            TokenType.NUM, Token_ID(TokenType.SYMBOL, "(")
        ],
        [
            Token_ID(TokenType.SYMBOL, ";"), Token_ID(TokenType.SYMBOL, "]"), Token_ID(TokenType.SYMBOL, ")"),
            Token_ID(TokenType.SYMBOL, ","), Token_ID(TokenType.SYMBOL, "<"), Token_ID(TokenType.SYMBOL, "=="),
            Token_ID(TokenType.SYMBOL, "+"), Token_ID(TokenType.SYMBOL, "-"), Token_ID(TokenType.SYMBOL, "*")
        ]
    ),
    NT.ARGS: LanguageRules(
        [
            TokenType.ID, TokenType.NUM, Token_ID(TokenType.SYMBOL, "("), epsilon
        ],
        [
            Token_ID(TokenType.SYMBOL, ")")
        ]
    ),
    NT.ARG_LIST: LanguageRules(
        [
            TokenType.ID, TokenType.NUM, Token_ID(TokenType.SYMBOL, "(")
        ],
        [
            Token_ID(TokenType.SYMBOL, ")")
        ]
    ),
    NT.ARG_LIST_PRIME: LanguageRules(
        [
            Token_ID(TokenType.SYMBOL, ","), epsilon
        ],
        [
            Token_ID(TokenType.SYMBOL, ")")
        ]
    ),
}

T_DIAGRAMS: dict[NT, list[list[Transition]]] = {
    NT.PROGRAM: [
        [Transition(1, NT.DECLARATION_LIST)],
        [Transition(2, Token_ID(TokenType.EOF, "$"))],
    ],
    NT.DECLARATION_LIST: [
        [Transition(1, NT.DECLARATION), Transition(2, epsilon)],
        [Transition(2, NT.DECLARATION_LIST)],
    ],
    NT.DECLARATION: [
        [Transition(1, NT.DECLARATION_INITIAL)],
        [Transition(2, NT.DECLARATION_PRIME)],
    ],
    NT.DECLARATION_INITIAL: [
        [Transition(1, NT.TYPE_SPECIFIER)],
        [Transition(2, TokenType.ID)],
    ],
    NT.DECLARATION_PRIME: [
        [Transition(1, NT.FUN_DECLARATION_PRIME), Transition(1, NT.VAR_DECLARATION_PRIME)],
    ],
    NT.VAR_DECLARATION_PRIME: [
        [Transition(1, Token_ID(TokenType.SYMBOL, "[")), Transition(4, Token_ID(TokenType.SYMBOL, ";"))],
        [Transition(2, TokenType.NUM)],
        [Transition(3, Token_ID(TokenType.SYMBOL, "]"))],
        [Transition(4, Token_ID(TokenType.SYMBOL, ";"))],
    ],
    NT.FUN_DECLARATION_PRIME: [
        [Transition(1, Token_ID(TokenType.SYMBOL, "("))],
        [Transition(2, NT.PARAMS)],
        [Transition(3, Token_ID(TokenType.SYMBOL, ")"))],
        [Transition(4, NT.COMPOUND_STMT)],
    ],
    NT.TYPE_SPECIFIER: [
        [Transition(1, Token_ID(TokenType.KEYWORD, "int")), Transition(1, Token_ID(TokenType.KEYWORD, "void"))],
    ],
    NT.PARAMS: [
        [Transition(1, Token_ID(TokenType.KEYWORD, "int")), Transition(4, Token_ID(TokenType.KEYWORD, "void"))],
        [Transition(2, TokenType.ID)],
        [Transition(3, NT.PARAM_PRIME)],
        [Transition(4, NT.PARAM_LIST)],
    ],
    NT.PARAM_LIST: [
        [Transition(1, Token_ID(TokenType.SYMBOL, ",")), Transition(3, epsilon)],
        [Transition(2, NT.PARAM)],
        [Transition(3, NT.PARAM_LIST)],
    ],
    NT.PARAM: [
        [Transition(1, NT.DECLARATION_INITIAL)],
        [Transition(2, NT.PARAM_PRIME)],
    ],
    NT.PARAM_PRIME: [
        [Transition(1, Token_ID(TokenType.SYMBOL, "[")), Transition(2, epsilon)],
        [Transition(2, Token_ID(TokenType.SYMBOL, "]"))],
    ],
    NT.COMPOUND_STMT: [
        [Transition(1, Token_ID(TokenType.SYMBOL, "{"))],
        [Transition(2, NT.DECLARATION_LIST)],
        [Transition(3, NT.STATEMENT_LIST)],
        [Transition(4, Token_ID(TokenType.SYMBOL, "}"))],
    ],
    NT.STATEMENT_LIST: [
        [Transition(1, NT.STATEMENT), Transition(2, epsilon)],
        [Transition(2, NT.STATEMENT_LIST)]
    ],
    NT.STATEMENT: [
        [
            Transition(1, NT.EXPRESSION_STMT),
            Transition(1, NT.COMPOUND_STMT),
            Transition(1, NT.SELECTION_STMT),
            Transition(1, NT.ITERATION_STMT),
            Transition(1, NT.RETURN_STMT),
        ]
    ],
    NT.EXPRESSION_STMT: [
        [Transition(1, NT.EXPRESSION), Transition(1, Token_ID(TokenType.KEYWORD, "break")),
         Transition(2, Token_ID(TokenType.SYMBOL, ";"))],
        [Transition(2, Token_ID(TokenType.SYMBOL, ";"))]
    ],
    NT.SELECTION_STMT: [
        [Transition(1, Token_ID(TokenType.KEYWORD, "if"))],
        [Transition(2, Token_ID(TokenType.SYMBOL, "("))],
        [Transition(3, NT.EXPRESSION)],
        [Transition(4, Token_ID(TokenType.SYMBOL, ")"))],
        [Transition(5, NT.STATEMENT)],
        [Transition(6, Token_ID(TokenType.KEYWORD, "else"))],
        [Transition(7, NT.STATEMENT)],
    ],
    NT.ITERATION_STMT: [
        [Transition(1, Token_ID(TokenType.KEYWORD, "repeat"))],
        [Transition(2, NT.STATEMENT)],
        [Transition(3, Token_ID(TokenType.KEYWORD, "until"))],
        [Transition(4, Token_ID(TokenType.SYMBOL, "("))],
        [Transition(5, NT.EXPRESSION)],
        [Transition(6, Token_ID(TokenType.SYMBOL, ")"))],
    ],
    NT.RETURN_STMT: [
        [Transition(1, Token_ID(TokenType.KEYWORD, "return"))],
        [Transition(2, NT.RETURN_STMT_PRIME)]
    ],
    NT.RETURN_STMT_PRIME: [
        [Transition(1, NT.EXPRESSION), Transition(2, Token_ID(TokenType.SYMBOL, ";"))],
        [Transition(2, Token_ID(TokenType.SYMBOL, ";"))]
    ],
    NT.EXPRESSION: [
        [Transition(1, TokenType.ID), Transition(2, NT.SIMPLE_EXPRESSION_ZEGOND)],
        [Transition(2, NT.B)]
    ],
    NT.B: [
        [Transition(1, Token_ID(TokenType.SYMBOL, "=")), Transition(2, Token_ID(TokenType.SYMBOL, "[")),
         Transition(5, NT.SIMPLE_EXPRESSION_PRIME)],
        [Transition(5, NT.EXPRESSION)],
        [Transition(3, NT.EXPRESSION)],
        [Transition(4, Token_ID(TokenType.SYMBOL, "]"))],
        [Transition(5, NT.H)],
    ],
    NT.H: [
        [Transition(1, NT.G), Transition(3, Token_ID(TokenType.SYMBOL, "="))],
        [Transition(2, NT.D)],
        [Transition(4, NT.C)],
        [Transition(4, NT.EXPRESSION)]
    ],
    NT.SIMPLE_EXPRESSION_ZEGOND: [
        [Transition(1, NT.ADDITIVE_EXPRESSION_ZEGOND)],
        [Transition(2, NT.C)]
    ],
    NT.SIMPLE_EXPRESSION_PRIME: [
        [Transition(1, NT.ADDITIVE_EXPRESSION_PRIME)],
        [Transition(2, NT.C)]
    ],
    NT.C: [
        [Transition(1, NT.RELOP), Transition(2, epsilon)],
        [Transition(2, NT.ADDITIVE_EXPRESSION)]
    ],
    NT.RELOP: [
        [Transition(1, Token_ID(TokenType.SYMBOL, "<")), Transition(1, Token_ID(TokenType.SYMBOL, "=="))]
    ],
    NT.ADDITIVE_EXPRESSION: [
        [Transition(1, NT.TERM)],
        [Transition(2, NT.D)]
    ],
    NT.ADDITIVE_EXPRESSION_PRIME: [
        [Transition(1, NT.TERM_PRIME)],
        [Transition(2, NT.D)]
    ],
    NT.ADDITIVE_EXPRESSION_ZEGOND: [
        [Transition(1, NT.TERM_ZEGOND)],
        [Transition(2, NT.D)]
    ],
    NT.D: [
        [Transition(1, NT.ADDOP), Transition(3, epsilon)],
        [Transition(2, NT.TERM)],
        [Transition(3, NT.D)],
    ],
    NT.ADDOP: [
        [Transition(1, Token_ID(TokenType.SYMBOL, "+")), Transition(1, Token_ID(TokenType.SYMBOL, "-"))]
    ],
    NT.TERM: [
        [Transition(1, NT.FACTOR)],
        [Transition(2, NT.G)]
    ],
    NT.TERM_PRIME: [
        [Transition(1, NT.FACTOR_PRIME)],
        [Transition(2, NT.G)]
    ],
    NT.TERM_ZEGOND: [
        [Transition(1, NT.FACTOR_ZEGOND)],
        [Transition(2, NT.G)]
    ],
    NT.G: [
        [Transition(1, Token_ID(TokenType.SYMBOL, "*")), Transition(3, epsilon)],
        [Transition(2, NT.FACTOR)],
        [Transition(3, NT.G)],
    ],
    NT.FACTOR: [
        [Transition(1, Token_ID(TokenType.SYMBOL, "(")), Transition(3, TokenType.ID), Transition(4, TokenType.NUM)],
        [Transition(2, NT.EXPRESSION)],
        [Transition(4, Token_ID(TokenType.SYMBOL, ")"))],
        [Transition(4, NT.VAR_CALL_PRIME)]
    ],
    NT.VAR_CALL_PRIME: [
        [Transition(1, Token_ID(TokenType.SYMBOL, "(")), Transition(3, NT.VAR_PRIME)],
        [Transition(2, NT.ARGS)],
        [Transition(3, Token_ID(TokenType.SYMBOL, ")"))]
    ],
    NT.VAR_PRIME: [
        [Transition(1, Token_ID(TokenType.SYMBOL, "[")), Transition(3, epsilon)],
        [Transition(2, NT.EXPRESSION)],
        [Transition(3, Token_ID(TokenType.SYMBOL, "]"))]
    ],
    NT.FACTOR_PRIME: [
        [Transition(1, Token_ID(TokenType.SYMBOL, "(")), Transition(3, epsilon)],
        [Transition(2, NT.ARGS)],
        [Transition(3, Token_ID(TokenType.SYMBOL, ")"))]
    ],
    NT.FACTOR_ZEGOND: [
        [Transition(1, Token_ID(TokenType.SYMBOL, "(")), Transition(3, TokenType.NUM)],
        [Transition(2, NT.EXPRESSION)],
        [Transition(3, Token_ID(TokenType.SYMBOL, ")"))]
    ],
    NT.ARGS: [
        [Transition(1, NT.ARG_LIST), Transition(1, epsilon)]
    ],
    NT.ARG_LIST: [
        [Transition(1, NT.EXPRESSION)],
        [Transition(2, NT.ARG_LIST_PRIME)]
    ],
    NT.ARG_LIST_PRIME: [
        [Transition(1, Token_ID(TokenType.SYMBOL, ",")), Transition(3, epsilon)],
        [Transition(2, NT.EXPRESSION)],
        [Transition(3, NT.ARG_LIST_PRIME)],
    ]
}

# Program⟶Declarationlist
# Declarationlist⟶Declaration Declarationlist
# Declarationlist⟶
# Declaration⟶Declarationinitial Declarationprime
# Declarationinitial⟶Typespecifier ID
# Declarationprime⟶Fundeclarationprime
# Declarationprime⟶Vardeclarationprime
# Vardeclarationprime⟶;
# Vardeclarationprime⟶[ NUM ] ;
# Fundeclarationprime⟶( Params ) Compoundstmt
# Typespecifier⟶int
# Typespecifier⟶void
# Params⟶int ID Paramprime Paramlist
# Params⟶void
# Paramlist⟶, Param Paramlist
# Paramlist⟶
# Param⟶Declarationinitial Paramprime
# Paramprime⟶[ ]
# Paramprime⟶
# Compoundstmt⟶{ Declarationlist Statementlist }
# Statementlist⟶Statement Statementlist
# Statementlist⟶
# Statement⟶Expressionstmt
# Statement⟶Compoundstmt
# Statement⟶Selectionstmt
# Statement⟶Iterationstmt
# Statement⟶Returnstmt
# Expressionstmt⟶Expression ;
# Expressionstmt⟶break ;
# Expressionstmt⟶;
# Selectionstmt⟶if ( Expression ) Statement else Statement
# Iterationstmt⟶repeat Statement until ( Expression )
# Returnstmt⟶return Returnstmtprime
# Returnstmtprime⟶;
# Returnstmtprime⟶Expression ;
# Expression⟶Simpleexpressionzegond
# Expression⟶ID B
# B⟶= Expression
# B⟶[ Expression ] H
# B⟶Simpleexpressionprime
# H⟶= Expression
# H⟶G D C
# Simpleexpressionzegond⟶Additiveexpressionzegond C
# Simpleexpressionprime⟶Additiveexpressionprime C
# C⟶Relop Additiveexpression
# C⟶
# Relop⟶<
# Relop⟶==
# Additiveexpression⟶Term D
# Additiveexpressionprime⟶Termprime D
# Additiveexpressionzegond⟶Termzegond D
# D⟶Addop Term D
# D⟶
# Addop⟶+
# Addop⟶-
# Term⟶Factor G
# Termprime⟶Factorprime G
# Termzegond⟶Factorzegond G
# G⟶* Factor G
# G⟶
# Factor⟶( Expression )
# Factor⟶ID Varcallprime
# Factor⟶NUM
# Varcallprime⟶( Args )
# Varcallprime⟶Varprime
# Varprime⟶[ Expression ]
# Varprime⟶
# Factorprime⟶( Args )
# Factorprime⟶
# Factorzegond⟶( Expression )
# Factorzegond⟶NUM
# Args⟶Arglist
# Args⟶
# Arglist⟶Expression Arglistprime
# Arglistprime⟶, Expression Arglistprime
# Arglistprime⟶