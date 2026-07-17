from enum import Enum, auto


class State(Enum):
    START = auto()
    STANDING = auto()
    DAMPING = auto()
    CUSTOM_RL_POLICY = auto()
    DEFAULT_CONTROLLER = auto()
    valid_transitions = {
        START: {STANDING},
        STANDING: {
            DAMPING,
            CUSTOM_RL_POLICY,
            DEFAULT_CONTROLLER,
        },
        DAMPING: {STANDING},
        CUSTOM_RL_POLICY: {DAMPING},
        DEFAULT_CONTROLLER: {DAMPING},
    }


class StateMachine:
    def __init__(self):
        self._state = State.START

    def get_state(self):
        return self._state

    def transition(self, new_state):
        if new_state in State.valid_transitions[self._state]:
            self._state = new_state
            return True
        else:
            return False
