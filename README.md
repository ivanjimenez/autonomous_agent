# Autonomous Agent Valory X-Y-Z Challenge

# Author/Candidate: Iván Jiménez Utiel


### Assumptions and decisions

- The code is decoupled in agent, behaviours and handlers modules with its respectives Interfaces/Abstract clases
- Each module has an implementation of an agent, handler or behaviour given in the current challenge.
- The architecture to run and manage agents is based on asyncrhounous queues (asyncio.queue) and tasks (asyncio).
- Not threads or multiprocesses are used, but these options could be used in the future to take advantage of multicore/multiprocess arquitectures. 
- `simple_agent.py` works with the AbstractClasses to decouple any implementation. 
- `main.py` is the main point to run the application. I think there are comments in each module but I would make some explanations in RUN section

### RUN

* Just execute main.py: `python main.py` (a console output is provided below)
* Two agents are running in asynchronous tasks.

* Every message create has the following format:
    - <date> <loglevel> <agent_name> <sending/receiven> <message> id <unique_id>
* Unique id is created when a message is generated and after is sent to the queue. The other agente receives the 
message and print it. **This is because the output is showed clearly and any message are checekd if it is lost or wrong/not sent/not received**.

* There is a callback called in 10 seconds once. This is because I want to demonstrate that handle or/and 
behaviours could be updated in agents while they are running without cancelling tasks or creating new instances.
* In the example below you can see the behaviour/handle given in the current challenge and after the callback is called, behaviour/handle are setted to new values. You can pass any implementation of handle/behaviour.

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

* Tasks could be stop comfortably and safely in console with CTRL+C keys.
* After that you will obtain some performance and time stats.
* Performance and time stats are calculated when agents are executing. 
```
    Closing event loop correctly
                     Time: 14.86 seconds

    ##################### Some Stats ########################
    Current memory usage: 9861 bytes | Peak: 38938 bytes
    CPU User: 7.81 % | CPU System 6.25 %
    IO Read Bytes: 2689972.00 | IO Write Bytes: 0.00
```
 

### Tests

- Test framework used for testing: `unittest`
- For some issues (needing of improvements), please run each test separately as follows:
    
    * Unit Test both agents: there are other tests in test folder to check behaviour and handle it is necessary. 
    ```
    python -m unittest .\tests\test_agents.py                
    ######### Starting Unit Tests
    Configured Agent1 and Agent2.
    .Agent1 behaviour configured
    .Agent2 behaviour configured
    .Agent1 handle configured
    .Agent1 handle configured
    .
    ----------------------------------------------------------------------
    Ran 5 tests in 0.006s

    OK
    ```
    ---
    * Integration Test: agent1 and agent2 are instantiated and runned with asyncronous tasks in the event loop. 
    The standard output of these tasks are recorded in `agent_logs.log` for testing purposes. The aim of the test is checking if behaviours and handles are working in real time while agents are sending/receiving messages. The execution of these tasks are limited to 10 secondes and then tasks are cancelled. The file has the output and after FOUND/NOT FOUND are counted to verify handle/behaviour are working.

    Sure Tests can be improved to check real scenarios properly. But I think this test could be fine by now. 
    ```
    $ python -m unittest .\tests\test_integration.py         
    #### Starting TEST AGENTS INTEGRATION

    >>> Tests Results
    FOUND count: 1
    NOT FOUND count: 5

                >>> The previous stdout is recorded in the following stdouput <<<
                >>> Just compare the resultos above and below                 <<<
                >>> Integration Tests improvements in future versions :-> !!  <<<

    2024-06-12 13:20:00,024 - root - INFO - Agent 1 sending: ocean ocean id 5803e91e01
    2024-06-12 13:20:00,024 - root - INFO - Agent 2 sending: space ocean id 41b52c881e
    2024-06-12 13:20:00,025 - root - INFO - Agent 2 receiving: <NOT FOUND: ocean ocean id 5803e91e01>
    2024-06-12 13:20:00,025 - root - INFO - Agent 1 receiving: <NOT FOUND: space ocean id 41b52c881e>
    2024-06-12 13:20:02,037 - root - INFO - Agent 1 sending: sun crypto id 3305e9c4b3
    2024-06-12 13:20:02,037 - root - INFO - Agent 2 sending: world world id 7ef9a170d9
    2024-06-12 13:20:02,037 - root - INFO - Agent 2 receiving: <NOT FOUND: sun crypto id 3305e9c4b3>
    2024-06-12 13:20:02,037 - root - INFO - Agent 1 receiving: <NOT FOUND: world world id 7ef9a170d9>
    2024-06-12 13:20:04,053 - root - INFO - Agent 1 sending: universe hello id daea7bbcc6
    2024-06-12 13:20:04,053 - root - INFO - Agent 2 sending: crypto space id ea290a7d02
    2024-06-12 13:20:04,053 - root - INFO - Agent 2 receiving: <FOUND: universe hello id daea7bbcc6>
    2024-06-12 13:20:04,053 - root - INFO - Agent 1 receiving: <NOT FOUND: crypto space id ea290a7d02>

    .
    ----------------------------------------------------------------------
    Ran 2 tests in 5.036s

    OK
    ```

### Improvements

- To create a Task Runner Class
- To create Thread Executor/Multiprocessing to take advantage of multicore architectures.
- To improve unit/integration tests. 