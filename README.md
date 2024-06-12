# Autonomous Agent Valory X-Y-Z Challenge

# Author/Candidate: Iván Jiménez Utiel


### Assumptions and decisions

- The code is decoupled in agent, behaviours and handlers modules with its respectives Interfaces/Abstract clases
- Each module has an implementation of an agent, handler or behaviour given in the current challenge.
- The architecture to run and manage agents is based on asyncrhounous queues (asyncio.queue) and tasks (asyncio).
- Not threads or multiprocesses are used, but these options could be used in the future to take advantage of multicore/multiprocess arquitectures. 
- `simple_agent.py`
- `main.py` is the main point to run the application. I think there are comments in each module but I would make some explanations in RUN section

### RUN

* Just execute main.py: 'python main.py' (a console output is provided below)
* Two agents are running in asynchronous tasks.
*

```bash
2024-06-12 13:01:50 INFO     Agent 1 sending: ocean ocean id e76dad6fb0
2024-06-12 13:01:50 INFO     Agent 2 sending: ocean ocean id 34f096c2b3
2024-06-12 13:01:50 INFO     Agent 2 receiving: <NOT FOUND: ocean ocean id e76dad6fb0>
2024-06-12 13:01:50 INFO     Agent 1 receiving: <NOT FOUND: ocean ocean id 34f096c2b3>
2024-06-12 13:01:52 INFO     Agent 1 sending: sun hello id 2dd827df6f
2024-06-12 13:01:52 INFO     Agent 2 sending: universe world id 842b0317da
2024-06-12 13:01:52 INFO     Agent 2 receiving: <FOUND: sun hello id 2dd827df6f>
2024-06-12 13:01:52 INFO     Agent 1 receiving: <NOT FOUND: universe world id 842b0317da>
2024-06-12 13:01:54 INFO     Agent 1 sending: moon hello id e1dfa52338
2024-06-12 13:01:54 INFO     Agent 2 sending: sun space id ad33c29c2d
2024-06-12 13:01:54 INFO     Agent 2 receiving: <FOUND: moon hello id e1dfa52338>
2024-06-12 13:01:54 INFO     Agent 1 receiving: <NOT FOUND: sun space id ad33c29c2d>
2024-06-12 13:01:56 INFO     Agent 1 sending: universe space id 924f809d98
2024-06-12 13:01:56 INFO     Agent 2 sending: sun moon id 0d5b1362c3
2024-06-12 13:01:56 INFO     Agent 2 receiving: <NOT FOUND: universe space id 924f809d98>
2024-06-12 13:01:56 INFO     Agent 1 receiving: <NOT FOUND: sun moon id 0d5b1362c3>
2024-06-12 13:01:59 INFO     Agent 1 sending: universe ocean id 15ee49fbb3
2024-06-12 13:01:59 INFO     Agent 2 sending: moon sun id cbd1f0ec45
2024-06-12 13:01:59 INFO     Agent 2 receiving: <NOT FOUND: universe ocean id 15ee49fbb3>
2024-06-12 13:01:59 INFO     Agent 1 receiving: <NOT FOUND: moon sun id cbd1f0ec45>
Callback executed! Updated behaviour and handle.
2024-06-12 13:02:01 INFO     Agent 1 sending: Manchester Milan id f0676d4382
2024-06-12 13:02:01 INFO     Agent 2 sending: Berlin Liverpool id 6abe9b33d1
2024-06-12 13:02:01 INFO     Agent 2 receiving: <NOT FOUND: Manchester Milan id f0676d4382>
2024-06-12 13:02:01 INFO     Agent 1 receiving: <NOT FOUND: Berlin Liverpool id 6abe9b33d1>
2024-06-12 13:02:03 INFO     Agent 1 sending: Manchester Liverpool id 1e2b18db64
2024-06-12 13:02:03 INFO     Agent 2 sending: Manchester Milan id 608775691b
```


### Improvements

- Task Runner Class
- Thread Executor