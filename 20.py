with open("input/20.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    
modules = dict()
    
def parse_module(line):
    name, destinations = line.split(" -> ")
    destinations = destinations.split(", ")
    type = None
    if name[0] == "%":
        type = "flipflop"
        name = name[1:]
    elif name[0] == "&":
        type = "conjunction"
        name = name[1:]
    modules[name] = (name, type, destinations)

for line in lines:
    parse_module(line)
    
module_states = {}

for (name, type, destinations) in modules.values():
    if type == "flipflop":
        module_states[name] = False
    elif type == "conjunction":
        input_modules = [n for (n, t, d) in modules.values() if name in d]
        state = {}
        for m in input_modules:
            state[m] = "low"
        module_states[name] = state

def push_button():
    global button_pushes     
    signal_queue = [("broadcaster", "low", "button")]
    low_pulses = 0
    high_pulses = 0
    while len(signal_queue) > 0:
        name, signal, from_name = signal_queue.pop(0)
        if signal == "low":
            low_pulses += 1
        else:
            high_pulses += 1
        if name not in modules:
            continue
        name, type, destinations = modules[name]
        if type == "flipflop":
            if signal == "high":
                continue
            module_states[name] = not module_states[name]
            signal_to_send = "high" if module_states[name] else "low"
            for destination in destinations:
                signal_queue.append((destination, signal_to_send, name))
            continue
        if type == "conjunction":
            state = module_states[name]
            state[from_name] = signal
            if "low" in state.values():
                for destination in destinations:
                    signal_queue.append((destination, "high", name))
                continue
            for destination in destinations:
                signal_queue.append((destination, "low", name))
            continue
        for destination in destinations:
            signal_queue.append((destination, signal, name))
    return low_pulses, high_pulses

l = 0
h = 0
for i in range(1000):
    low_pulses, high_pulses = push_button()
    l += low_pulses
    h += high_pulses
print(l * h)