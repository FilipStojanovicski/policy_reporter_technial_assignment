#!/usr/bin/env python
# coding: utf-8

# In[149]:


class FSM():
    def __init__(self, 
                 states: list = [], 
                 valid_inputs: list = [], 
                 initial_state = None, 
                 accepting_states: list = [], 
                 transition_function = lambda x,y: None):
        self.states = states
        self.valid_inputs = valid_inputs
        self.initial_state = initial_state
        self.current_state = initial_state
        self.accepting_states = accepting_states
        self.transition_function = transition_function
        
        if not initial_state in states:
            raise ValueError("The initial_state must be contained in the set of states")
        
        if not set(accepting_states).issubset(set(states)):
            raise ValueError("The set of accepting_states must be contained in the set of states")
        
    def run(self, inputs):
        self.current_state = self.initial_state
        for i in inputs:
            next_state = self.transition_function(self.current_state, i)
            self.current_state = next_state
        
        if next_state not in self.accepting_states:
            raise ValueError("The final state is not one of the accepting_states")
            
        return next_state


# In[150]:


def transition_func_div_mod3(current_state, i):
    if current_state == "S0":
        if i == "0":
            return "S0"
        elif i == "1":
            return "S1"
        else:
            raise ValueError(f"The input {i} is not valid")
    elif current_state == "S1":
        if i == "0":
            return "S2"
        elif i == "1":
            return "S0"
        else:
            raise ValueError(f"The input {i} is not valid")
    elif current_state == "S2":
        if i == "0":
            return "S1"
        elif i == "1":
            return "S2"
        else:
            raise ValueError(f"The input {i} is not valid")
    else:
        raise ValueError(f"The current_state {current} is not valid")


# In[151]:


fsm_division_mod3 = FSM(states = ["S0", "S1", "S2"], 
                        valid_inputs = ["0","1"], 
                        initial_state = "S0", 
                        accepting_states = ["S0", "S1", "S2"],
                        transition_function = transition_func_div_mod3
                       )


# In[152]:


test_cases = {"1101": "S1", "1110": "S2", "1111": "S0", "110": "S0", "1010": "S1"}


# In[153]:


for _input, expected_output in test_cases.items():
    _output = fsm_division_mod3.run(_input)
    assert _output == expected_output


# In[ ]:




