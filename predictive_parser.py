from anytree import Node
from constants import epsilon
from first_follow import LANG_RULES_INFO
from transition import T_DIAGRAMS
from scanner import get_next_token
from declarations import Nonterminalstates as NT, Token, State, TokenType, Token_ID, Syntax_Error
from helper import check_in_first, check_in_follow, finalize_tree, save_syntax_errors


def all_terminal_states(state_transitions):
    for transition in state_transitions:
        if (isinstance(transition.identifier, NT) or transition.identifier == epsilon) \
                or (isinstance(transition.identifier, Token_ID) and transition.identifier.type == TokenType.EOF):
            return False
    return True


def check_follows(nt_transitions, curr_token, syntax_errors):
    for transition in nt_transitions:
        if check_in_follow(transition.identifier, curr_token):
            syntax_errors.append(Syntax_Error(curr_token.line_num, f'missing {transition.identifier.value}'))
            return transition.dest_state

    syntax_errors.append(
        Syntax_Error(curr_token.line_num,
                     f'illegal {curr_token.type.value if curr_token.type == TokenType.NUM or curr_token.type == TokenType.ID else curr_token.lexeme}'))
    return get_next_token()


def get_related_transition(transitions, curr_token):
    for transition in transitions:
        if match(transition.identifier, curr_token):
            return transition
    return None


def parse():
    syntax_errors: list[Syntax_Error] = []
    accepted = False
    head = Node(NT.PROGRAM.value)
    stack = []
    curr_state = State(NT.PROGRAM, 0)
    curr_token = get_next_token()

    while not accepted:
        if len(T_DIAGRAMS[curr_state.nonterminal]) == curr_state.state:
            if len(stack) == 0:
                accepted = True
            else:
                curr_state = stack.pop()
                head = head.parent
        else:
            state_transitions = T_DIAGRAMS[curr_state.nonterminal][curr_state.state]
            transition = get_related_transition(state_transitions, curr_token)
            if transition is not None:
                identifier = transition.identifier
                if isinstance(identifier, TokenType) or isinstance(identifier, Token_ID):
                    curr_state.state = transition.dest_state
                    Node(str(curr_token), parent=head)
                    curr_token = get_next_token()
                elif isinstance(identifier, NT):
                    stack.append(State(curr_state.nonterminal, transition.dest_state))
                    curr_state = State(identifier, 0)
                    head = Node(identifier.value, head)
                else:
                    Node(epsilon, parent=head)
                    curr_state.state = transition.dest_state
            else:
                if curr_token.type == TokenType.EOF:
                    syntax_errors.append(
                        Syntax_Error(curr_token.line_num, f'Unexpected EOF'))
                    while head.parent is not None:
                        head = head.parent
                    break
                if all_terminal_states(state_transitions):
                    syntax_errors.append(
                        Syntax_Error(curr_token.line_num, f'missing {extract_token(state_transitions[0].identifier)}'))
                    curr_state.state = state_transitions[0].dest_state
                else:
                    nt_transitions = filter(lambda tr: isinstance(tr.identifier, NT), state_transitions)
                    token_or_state = check_follows(nt_transitions, curr_token, syntax_errors)
                    if isinstance(token_or_state, Token):
                        curr_token = token_or_state
                    else:
                        curr_state.state = token_or_state

    finalize_tree(head)
    save_syntax_errors(syntax_errors)
    return head


def extract_token(identifier):
    if isinstance(identifier, Token_ID):
        return identifier.lexeme
    else:
        return identifier.value


def match(identifier, curr_token: Token):
    if isinstance(identifier, TokenType):
        return curr_token.type == identifier
    elif isinstance(identifier, Token_ID):
        return curr_token.type == identifier.type and curr_token.lexeme == identifier.lexeme
    elif identifier == epsilon:
        return True
    elif isinstance(identifier, NT):
        cond = False
        if epsilon in LANG_RULES_INFO[identifier].first:
            cond = curr_token.type in LANG_RULES_INFO[identifier].follow \
                   or Token_ID(curr_token.type, curr_token.lexeme) in LANG_RULES_INFO[identifier].follow
        return check_in_first(identifier, curr_token) or cond
    else:
        return False
