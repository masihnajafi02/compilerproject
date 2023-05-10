from declarations import Nonterminal as NT, NTerminalInfo, Transition, TokenType, T_ID

all_keywords = ['break', 'else', 'if', 'int', 'repeat', 'return', 'until', 'void']
input_file_name = "input.txt"
token_file_name = "tokens.txt"
lexical_error_file_name = "lexical_errors.txt"
symbol_table_file_name = "symbol_table.txt"
parse_tree_file_name = "parse_tree.txt"
syntax_error_file_name = "syntax_errors.txt"
epsilon = "epsilon"


class NTerminalInfo:
    first: list[str]
    follow: list[str]

    def __init__(self, first, follow):
        self.first = first
        self.follow = follow


N_TERMINALS_INFO: dict[NT, NTerminalInfo] = {
    NT.PROGRAM: NTerminalInfo(
        [
            T_ID(TokenType.KEYWORD, "int"), T_ID(TokenType.KEYWORD, "void"), epsilon
        ],
        [
            T_ID(TokenType.EOF, "$")
        ]),
    NT.DECLARATION_LIST: NTerminalInfo(
        [
            T_ID(TokenType.KEYWORD, "int"), T_ID(TokenType.KEYWORD, "void"), epsilon
        ],
        [
            T_ID(TokenType.EOF, "$"), TokenType.ID, T_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            T_ID(TokenType.SYMBOL, "("),
            T_ID(TokenType.SYMBOL, "{"), T_ID(TokenType.SYMBOL, "}"), T_ID(TokenType.KEYWORD, "break"),
            T_ID(TokenType.KEYWORD, "if"),
            T_ID(TokenType.KEYWORD, "repeat"), T_ID(TokenType.KEYWORD, "return")
        ]
    ),
    NT.DECLARATION: NTerminalInfo(
        [
            T_ID(TokenType.KEYWORD, "int"), T_ID(TokenType.KEYWORD, "void")
        ],
        [
            T_ID(TokenType.EOF, "$"), TokenType.ID, T_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            T_ID(TokenType.SYMBOL, "("),
            T_ID(TokenType.SYMBOL, "{"), T_ID(TokenType.SYMBOL, "}"), T_ID(TokenType.KEYWORD, "break"),
            T_ID(TokenType.KEYWORD, "if"),
            T_ID(TokenType.KEYWORD, "repeat"), T_ID(TokenType.KEYWORD, "return"),
            T_ID(TokenType.KEYWORD, "int"), T_ID(TokenType.KEYWORD, "void")
        ]
    ),
    NT.DECLARATION_INITIAL: NTerminalInfo(
        [
            T_ID(TokenType.KEYWORD, "int"), T_ID(TokenType.KEYWORD, "void")
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "["), T_ID(TokenType.SYMBOL, "("),
            T_ID(TokenType.SYMBOL, ")"), T_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.DECLARATION_PRIME: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "["), T_ID(TokenType.SYMBOL, "(")
        ],
        [
            T_ID(TokenType.EOF, "$"), TokenType.ID, T_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            T_ID(TokenType.SYMBOL, "("),
            T_ID(TokenType.SYMBOL, "{"), T_ID(TokenType.SYMBOL, "}"), T_ID(TokenType.KEYWORD, "break"),
            T_ID(TokenType.KEYWORD, "if"),
            T_ID(TokenType.KEYWORD, "repeat"), T_ID(TokenType.KEYWORD, "return"),
            T_ID(TokenType.KEYWORD, "int"), T_ID(TokenType.KEYWORD, "void")
        ]
    ),
    NT.VAR_DECLARATION_PRIME: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "[")
        ],
        [
            T_ID(TokenType.EOF, "$"), TokenType.ID, T_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            T_ID(TokenType.SYMBOL, "("),
            T_ID(TokenType.SYMBOL, "{"), T_ID(TokenType.SYMBOL, "}"), T_ID(TokenType.KEYWORD, "break"),
            T_ID(TokenType.KEYWORD, "if"),
            T_ID(TokenType.KEYWORD, "repeat"), T_ID(TokenType.KEYWORD, "return"),
            T_ID(TokenType.KEYWORD, "int"), T_ID(TokenType.KEYWORD, "void")
        ]
    ),
    NT.FUN_DECLARATION_PRIME: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, "(")
        ],
        [
            T_ID(TokenType.EOF, "$"), TokenType.ID, T_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            T_ID(TokenType.SYMBOL, "("),
            T_ID(TokenType.SYMBOL, "{"), T_ID(TokenType.SYMBOL, "}"), T_ID(TokenType.KEYWORD, "break"),
            T_ID(TokenType.KEYWORD, "if"),
            T_ID(TokenType.KEYWORD, "repeat"), T_ID(TokenType.KEYWORD, "return"),
            T_ID(TokenType.KEYWORD, "int"), T_ID(TokenType.KEYWORD, "void")
        ]
    ),
    NT.TYPE_SPECIFIER: NTerminalInfo(
        [
            T_ID(TokenType.KEYWORD, "int"), T_ID(TokenType.KEYWORD, "void")
        ],
        [
            TokenType.ID
        ]
    ),
    NT.PARAMS: NTerminalInfo(
        [
            T_ID(TokenType.KEYWORD, "int"), T_ID(TokenType.KEYWORD, "void")
        ],
        [
            T_ID(TokenType.SYMBOL, ")")
        ]
    ),
    NT.PARAM_LIST: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, ","), epsilon
        ],
        [
            T_ID(TokenType.SYMBOL, ")")
        ]
    ),
    NT.PARAM: NTerminalInfo(
        [
            T_ID(TokenType.KEYWORD, "int"), T_ID(TokenType.KEYWORD, "void")
        ],
        [
            T_ID(TokenType.SYMBOL, ")"), T_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.PARAM_PRIME: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, "["), epsilon
        ],
        [
            T_ID(TokenType.SYMBOL, ")"), T_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.COMPOUND_STMT: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, "{")
        ],
        [
            T_ID(TokenType.EOF, "$"), TokenType.ID, T_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            T_ID(TokenType.SYMBOL, "("),
            T_ID(TokenType.SYMBOL, "{"), T_ID(TokenType.SYMBOL, "}"), T_ID(TokenType.KEYWORD, "break"),
            T_ID(TokenType.KEYWORD, "if"),
            T_ID(TokenType.KEYWORD, "repeat"), T_ID(TokenType.KEYWORD, "return"),
            T_ID(TokenType.KEYWORD, "int"), T_ID(TokenType.KEYWORD, "void"),
            T_ID(TokenType.KEYWORD, "else"), T_ID(TokenType.KEYWORD, "until")
        ]
    ),
    NT.STATEMENT_LIST: NTerminalInfo(
        [
            TokenType.ID, T_ID(TokenType.SYMBOL, ";"), TokenType.NUM, T_ID(TokenType.SYMBOL, "("),
            T_ID(TokenType.SYMBOL, "{"), T_ID(TokenType.KEYWORD, "break"), T_ID(TokenType.KEYWORD, "if"),
            T_ID(TokenType.KEYWORD, "repeat"), T_ID(TokenType.KEYWORD, "return"), epsilon
        ],
        [
            T_ID(TokenType.SYMBOL, "}")
        ]
    ),
    NT.STATEMENT: NTerminalInfo(
        [
            TokenType.ID, T_ID(TokenType.SYMBOL, ";"), TokenType.NUM, T_ID(TokenType.SYMBOL, "("),
            T_ID(TokenType.SYMBOL, "{"), T_ID(TokenType.KEYWORD, "break"), T_ID(TokenType.KEYWORD, "if"),
            T_ID(TokenType.KEYWORD, "repeat"), T_ID(TokenType.KEYWORD, "return")
        ],
        [
            TokenType.ID, T_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            T_ID(TokenType.SYMBOL, "("),
            T_ID(TokenType.SYMBOL, "{"), T_ID(TokenType.SYMBOL, "}"), T_ID(TokenType.KEYWORD, "break"),
            T_ID(TokenType.KEYWORD, "if"),
            T_ID(TokenType.KEYWORD, "repeat"), T_ID(TokenType.KEYWORD, "return"),
            T_ID(TokenType.KEYWORD, "else"), T_ID(TokenType.KEYWORD, "until")
        ]
    ),
    NT.EXPRESSION_STMT: NTerminalInfo(
        [
            TokenType.ID, T_ID(TokenType.SYMBOL, ";"), TokenType.NUM, T_ID(TokenType.SYMBOL, "("),
            T_ID(TokenType.KEYWORD, "break")
        ],
        [
            TokenType.ID, T_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            T_ID(TokenType.SYMBOL, "("),
            T_ID(TokenType.SYMBOL, "{"), T_ID(TokenType.SYMBOL, "}"), T_ID(TokenType.KEYWORD, "break"),
            T_ID(TokenType.KEYWORD, "if"),
            T_ID(TokenType.KEYWORD, "repeat"), T_ID(TokenType.KEYWORD, "return"),
            T_ID(TokenType.KEYWORD, "else"), T_ID(TokenType.KEYWORD, "until")
        ]
    ),
    NT.SELECTION_STMT: NTerminalInfo(
        [
            T_ID(TokenType.KEYWORD, "if")
        ],
        [
            TokenType.ID, T_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            T_ID(TokenType.SYMBOL, "("),
            T_ID(TokenType.SYMBOL, "{"), T_ID(TokenType.SYMBOL, "}"), T_ID(TokenType.KEYWORD, "break"),
            T_ID(TokenType.KEYWORD, "if"),
            T_ID(TokenType.KEYWORD, "repeat"), T_ID(TokenType.KEYWORD, "return"),
            T_ID(TokenType.KEYWORD, "else"), T_ID(TokenType.KEYWORD, "until")
        ]
    ),
    NT.ITERATION_STMT: NTerminalInfo(
        [
            T_ID(TokenType.KEYWORD, "repeat")
        ],
        [
            TokenType.ID, T_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            T_ID(TokenType.SYMBOL, "("),
            T_ID(TokenType.SYMBOL, "{"), T_ID(TokenType.SYMBOL, "}"), T_ID(TokenType.KEYWORD, "break"),
            T_ID(TokenType.KEYWORD, "if"),
            T_ID(TokenType.KEYWORD, "repeat"), T_ID(TokenType.KEYWORD, "return"),
            T_ID(TokenType.KEYWORD, "else"), T_ID(TokenType.KEYWORD, "until")
        ]
    ),
    NT.RETURN_STMT: NTerminalInfo(
        [
            T_ID(TokenType.KEYWORD, "return")
        ],
        [
            TokenType.ID, T_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            T_ID(TokenType.SYMBOL, "("),
            T_ID(TokenType.SYMBOL, "{"), T_ID(TokenType.SYMBOL, "}"), T_ID(TokenType.KEYWORD, "break"),
            T_ID(TokenType.KEYWORD, "if"),
            T_ID(TokenType.KEYWORD, "repeat"), T_ID(TokenType.KEYWORD, "return"),
            T_ID(TokenType.KEYWORD, "else"), T_ID(TokenType.KEYWORD, "until")
        ]
    ),
    NT.RETURN_STMT_PRIME: NTerminalInfo(
        [
            TokenType.ID, T_ID(TokenType.SYMBOL, ";"), TokenType.NUM, T_ID(TokenType.SYMBOL, "(")
        ],
        [
            TokenType.ID, T_ID(TokenType.SYMBOL, ";"), TokenType.NUM,
            T_ID(TokenType.SYMBOL, "("),
            T_ID(TokenType.SYMBOL, "{"), T_ID(TokenType.SYMBOL, "}"), T_ID(TokenType.KEYWORD, "break"),
            T_ID(TokenType.KEYWORD, "if"),
            T_ID(TokenType.KEYWORD, "repeat"), T_ID(TokenType.KEYWORD, "return"),
            T_ID(TokenType.KEYWORD, "else"), T_ID(TokenType.KEYWORD, "until")
        ]
    ),
    NT.EXPRESSION: NTerminalInfo(
        [
            TokenType.ID, TokenType.NUM, T_ID(TokenType.SYMBOL, "(")
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.B: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, "["), T_ID(TokenType.SYMBOL, "("), T_ID(TokenType.SYMBOL, "="),
            T_ID(TokenType.SYMBOL, "<"), T_ID(TokenType.SYMBOL, "=="), T_ID(TokenType.SYMBOL, "+"),
            T_ID(TokenType.SYMBOL, "-"), T_ID(TokenType.SYMBOL, "*"), epsilon
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.H: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, "="),
            T_ID(TokenType.SYMBOL, "<"), T_ID(TokenType.SYMBOL, "=="), T_ID(TokenType.SYMBOL, "+"),
            T_ID(TokenType.SYMBOL, "-"), T_ID(TokenType.SYMBOL, "*"), epsilon
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.SIMPLE_EXPRESSION_ZEGOND: NTerminalInfo(
        [
            TokenType.NUM, T_ID(TokenType.SYMBOL, "(")
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.SIMPLE_EXPRESSION_PRIME: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, "("),
            T_ID(TokenType.SYMBOL, "<"), T_ID(TokenType.SYMBOL, "=="), T_ID(TokenType.SYMBOL, "+"),
            T_ID(TokenType.SYMBOL, "-"), T_ID(TokenType.SYMBOL, "*"), epsilon
        ],
        [

            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.C: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, "<"), T_ID(TokenType.SYMBOL, "=="), epsilon
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.RELOP: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, "<"), T_ID(TokenType.SYMBOL, "==")
        ],
        [
            TokenType.ID, TokenType.NUM, T_ID(TokenType.SYMBOL, "(")
        ]
    ),
    NT.ADDITIVE_EXPRESSION: NTerminalInfo(
        [
            TokenType.ID, TokenType.NUM, T_ID(TokenType.SYMBOL, "(")
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ",")
        ]
    ),
    NT.ADDITIVE_EXPRESSION_PRIME: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, "("), T_ID(TokenType.SYMBOL, "+"),
            T_ID(TokenType.SYMBOL, "-"), T_ID(TokenType.SYMBOL, "*"), epsilon
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ","), T_ID(TokenType.SYMBOL, "<"), T_ID(TokenType.SYMBOL, "==")
        ]
    ),
    NT.ADDITIVE_EXPRESSION_ZEGOND: NTerminalInfo(
        [
            TokenType.NUM, T_ID(TokenType.SYMBOL, "(")
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ","), T_ID(TokenType.SYMBOL, "<"), T_ID(TokenType.SYMBOL, "==")
        ]
    ),
    NT.D: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, "+"), T_ID(TokenType.SYMBOL, "-"), epsilon
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ","), T_ID(TokenType.SYMBOL, "<"), T_ID(TokenType.SYMBOL, "==")
        ]
    ),
    NT.ADDOP: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, "+"), T_ID(TokenType.SYMBOL, "-")
        ],
        [
            TokenType.ID, TokenType.NUM, T_ID(TokenType.SYMBOL, "(")
        ]
    ),
    NT.TERM: NTerminalInfo(
        [
            TokenType.ID, TokenType.NUM, T_ID(TokenType.SYMBOL, "(")
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ","), T_ID(TokenType.SYMBOL, "<"), T_ID(TokenType.SYMBOL, "=="),
            T_ID(TokenType.SYMBOL, "+"), T_ID(TokenType.SYMBOL, "-")
        ]
    ),
    NT.TERM_PRIME: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, "("), T_ID(TokenType.SYMBOL, "*"), epsilon
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ","), T_ID(TokenType.SYMBOL, "<"), T_ID(TokenType.SYMBOL, "=="),
            T_ID(TokenType.SYMBOL, "+"), T_ID(TokenType.SYMBOL, "-")
        ]
    ),
    NT.TERM_ZEGOND: NTerminalInfo(
        [
            TokenType.NUM, T_ID(TokenType.SYMBOL, "(")
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ","), T_ID(TokenType.SYMBOL, "<"), T_ID(TokenType.SYMBOL, "=="),
            T_ID(TokenType.SYMBOL, "+"), T_ID(TokenType.SYMBOL, "-")
        ]
    ),
    NT.G: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, "*"), epsilon
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ","), T_ID(TokenType.SYMBOL, "<"), T_ID(TokenType.SYMBOL, "=="),
            T_ID(TokenType.SYMBOL, "+"), T_ID(TokenType.SYMBOL, "-")
        ]
    ),
    NT.FACTOR: NTerminalInfo(
        [
            TokenType.ID, TokenType.NUM, T_ID(TokenType.SYMBOL, "(")
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ","), T_ID(TokenType.SYMBOL, "<"), T_ID(TokenType.SYMBOL, "=="),
            T_ID(TokenType.SYMBOL, "+"), T_ID(TokenType.SYMBOL, "-"), T_ID(TokenType.SYMBOL, "*")
        ]
    ),
    NT.VAR_CALL_PRIME: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, "["), T_ID(TokenType.SYMBOL, "("), epsilon
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ","), T_ID(TokenType.SYMBOL, "<"), T_ID(TokenType.SYMBOL, "=="),
            T_ID(TokenType.SYMBOL, "+"), T_ID(TokenType.SYMBOL, "-"), T_ID(TokenType.SYMBOL, "*")
        ]
    ),
    NT.VAR_PRIME: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, "["), epsilon
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ","), T_ID(TokenType.SYMBOL, "<"), T_ID(TokenType.SYMBOL, "=="),
            T_ID(TokenType.SYMBOL, "+"), T_ID(TokenType.SYMBOL, "-"), T_ID(TokenType.SYMBOL, "*")
        ]
    ),
    NT.FACTOR_PRIME: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, "("), epsilon
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ","), T_ID(TokenType.SYMBOL, "<"), T_ID(TokenType.SYMBOL, "=="),
            T_ID(TokenType.SYMBOL, "+"), T_ID(TokenType.SYMBOL, "-"), T_ID(TokenType.SYMBOL, "*")
        ]
    ),
    NT.FACTOR_ZEGOND: NTerminalInfo(
        [
            TokenType.NUM, T_ID(TokenType.SYMBOL, "(")
        ],
        [
            T_ID(TokenType.SYMBOL, ";"), T_ID(TokenType.SYMBOL, "]"), T_ID(TokenType.SYMBOL, ")"),
            T_ID(TokenType.SYMBOL, ","), T_ID(TokenType.SYMBOL, "<"), T_ID(TokenType.SYMBOL, "=="),
            T_ID(TokenType.SYMBOL, "+"), T_ID(TokenType.SYMBOL, "-"), T_ID(TokenType.SYMBOL, "*")
        ]
    ),
    NT.ARGS: NTerminalInfo(
        [
            TokenType.ID, TokenType.NUM, T_ID(TokenType.SYMBOL, "("), epsilon
        ],
        [
            T_ID(TokenType.SYMBOL, ")")
        ]
    ),
    NT.ARG_LIST: NTerminalInfo(
        [
            TokenType.ID, TokenType.NUM, T_ID(TokenType.SYMBOL, "(")
        ],
        [
            T_ID(TokenType.SYMBOL, ")")
        ]
    ),
    NT.ARG_LIST_PRIME: NTerminalInfo(
        [
            T_ID(TokenType.SYMBOL, ","), epsilon
        ],
        [
            T_ID(TokenType.SYMBOL, ")")
        ]
    ),
}

T_DIAGRAMS: dict[NT, list[list[Transition]]] = {
    NT.PROGRAM: [
        [Transition(1, NT.DECLARATION_LIST)],
        [Transition(2, T_ID(TokenType.EOF, "$"))],
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
        [Transition(1, T_ID(TokenType.SYMBOL, "[")), Transition(4, T_ID(TokenType.SYMBOL, ";"))],
        [Transition(2, TokenType.NUM)],
        [Transition(3, T_ID(TokenType.SYMBOL, "]"))],
        [Transition(4, T_ID(TokenType.SYMBOL, ";"))],
    ],
    NT.FUN_DECLARATION_PRIME: [
        [Transition(1, T_ID(TokenType.SYMBOL, "("))],
        [Transition(2, NT.PARAMS)],
        [Transition(3, T_ID(TokenType.SYMBOL, ")"))],
        [Transition(4, NT.COMPOUND_STMT)],
    ],
    NT.TYPE_SPECIFIER: [
        [Transition(1, T_ID(TokenType.KEYWORD, "int")), Transition(1, T_ID(TokenType.KEYWORD, "void"))],
    ],
    NT.PARAMS: [
        [Transition(1, T_ID(TokenType.KEYWORD, "int")), Transition(4, T_ID(TokenType.KEYWORD, "void"))],
        [Transition(2, TokenType.ID)],
        [Transition(3, NT.PARAM_PRIME)],
        [Transition(4, NT.PARAM_LIST)],
    ],
    NT.PARAM_LIST: [
        [Transition(1, T_ID(TokenType.SYMBOL, ",")), Transition(3, epsilon)],
        [Transition(2, NT.PARAM)],
        [Transition(3, NT.PARAM_LIST)],
    ],
    NT.PARAM: [
        [Transition(1, NT.DECLARATION_INITIAL)],
        [Transition(2, NT.PARAM_PRIME)],
    ],
    NT.PARAM_PRIME: [
        [Transition(1, T_ID(TokenType.SYMBOL, "[")), Transition(2, epsilon)],
        [Transition(2, T_ID(TokenType.SYMBOL, "]"))],
    ],
    NT.COMPOUND_STMT: [
        [Transition(1, T_ID(TokenType.SYMBOL, "{"))],
        [Transition(2, NT.DECLARATION_LIST)],
        [Transition(3, NT.STATEMENT_LIST)],
        [Transition(4, T_ID(TokenType.SYMBOL, "}"))],
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
        [Transition(1, NT.EXPRESSION), Transition(1, T_ID(TokenType.KEYWORD, "break")),
         Transition(2, T_ID(TokenType.SYMBOL, ";"))],
        [Transition(2, T_ID(TokenType.SYMBOL, ";"))]
    ],
    NT.SELECTION_STMT: [
        [Transition(1, T_ID(TokenType.KEYWORD, "if"))],
        [Transition(2, T_ID(TokenType.SYMBOL, "("))],
        [Transition(3, NT.EXPRESSION)],
        [Transition(4, T_ID(TokenType.SYMBOL, ")"))],
        [Transition(5, NT.STATEMENT)],
        [Transition(6, T_ID(TokenType.KEYWORD, "else"))],
        [Transition(7, NT.STATEMENT)],
    ],
    NT.ITERATION_STMT: [
        [Transition(1, T_ID(TokenType.KEYWORD, "repeat"))],
        [Transition(2, NT.STATEMENT)],
        [Transition(3, T_ID(TokenType.KEYWORD, "until"))],
        [Transition(4, T_ID(TokenType.SYMBOL, "("))],
        [Transition(5, NT.EXPRESSION)],
        [Transition(6, T_ID(TokenType.SYMBOL, ")"))],
    ],
    NT.RETURN_STMT: [
        [Transition(1, T_ID(TokenType.KEYWORD, "return"))],
        [Transition(2, NT.RETURN_STMT_PRIME)]
    ],
    NT.RETURN_STMT_PRIME: [
        [Transition(1, NT.EXPRESSION), Transition(2, T_ID(TokenType.SYMBOL, ";"))],
        [Transition(2, T_ID(TokenType.SYMBOL, ";"))]
    ],
    NT.EXPRESSION: [
        [Transition(1, TokenType.ID), Transition(2, NT.SIMPLE_EXPRESSION_ZEGOND)],
        [Transition(2, NT.B)]
    ],
    NT.B: [
        [Transition(1, T_ID(TokenType.SYMBOL, "=")), Transition(2, T_ID(TokenType.SYMBOL, "[")),
         Transition(5, NT.SIMPLE_EXPRESSION_PRIME)],
        [Transition(5, NT.EXPRESSION)],
        [Transition(3, NT.EXPRESSION)],
        [Transition(4, T_ID(TokenType.SYMBOL, "]"))],
        [Transition(5, NT.H)],
    ],
    NT.H: [
        [Transition(1, NT.G), Transition(3, T_ID(TokenType.SYMBOL, "="))],
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
        [Transition(1, T_ID(TokenType.SYMBOL, "<")), Transition(1, T_ID(TokenType.SYMBOL, "=="))]
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
        [Transition(1, T_ID(TokenType.SYMBOL, "+")), Transition(1, T_ID(TokenType.SYMBOL, "-"))]
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
        [Transition(1, T_ID(TokenType.SYMBOL, "*")), Transition(3, epsilon)],
        [Transition(2, NT.FACTOR)],
        [Transition(3, NT.G)],
    ],
    NT.FACTOR: [
        [Transition(1, T_ID(TokenType.SYMBOL, "(")), Transition(3, TokenType.ID), Transition(4, TokenType.NUM)],
        [Transition(2, NT.EXPRESSION)],
        [Transition(4, T_ID(TokenType.SYMBOL, ")"))],
        [Transition(4, NT.VAR_CALL_PRIME)]
    ],
    NT.VAR_CALL_PRIME: [
        [Transition(1, T_ID(TokenType.SYMBOL, "(")), Transition(3, NT.VAR_PRIME)],
        [Transition(2, NT.ARGS)],
        [Transition(3, T_ID(TokenType.SYMBOL, ")"))]
    ],
    NT.VAR_PRIME: [
        [Transition(1, T_ID(TokenType.SYMBOL, "[")), Transition(3, epsilon)],
        [Transition(2, NT.EXPRESSION)],
        [Transition(3, T_ID(TokenType.SYMBOL, "]"))]
    ],
    NT.FACTOR_PRIME: [
        [Transition(1, T_ID(TokenType.SYMBOL, "(")), Transition(3, epsilon)],
        [Transition(2, NT.ARGS)],
        [Transition(3, T_ID(TokenType.SYMBOL, ")"))]
    ],
    NT.FACTOR_ZEGOND: [
        [Transition(1, T_ID(TokenType.SYMBOL, "(")), Transition(3, TokenType.NUM)],
        [Transition(2, NT.EXPRESSION)],
        [Transition(3, T_ID(TokenType.SYMBOL, ")"))]
    ],
    NT.ARGS: [
        [Transition(1, NT.ARG_LIST), Transition(1, epsilon)]
    ],
    NT.ARG_LIST: [
        [Transition(1, NT.EXPRESSION)],
        [Transition(2, NT.ARG_LIST_PRIME)]
    ],
    NT.ARG_LIST_PRIME: [
        [Transition(1, T_ID(TokenType.SYMBOL, ",")), Transition(3, epsilon)],
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