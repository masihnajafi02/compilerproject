from constants import epsilon
from declarations import Nonterminalstates as NT, TokenType, Token_ID, LanguageRules

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
