# producer_consumer
Implementation of producer and consumer problem by using synchronization primitives, and offer three different implementations.

1. version1

    Only using mutex to protect the critical section, producers and consumers continue to check if the queue is available. The drawback of this version code is CPU wasting.

2. version2

    Compared with version 1, it solves CPU wasting problem, it uses condition variable to block the thread when the queue is not
    available, and then notify the threads when the queue is available.
    
3. version3
    
    The version2 code uses condition variable to block the thread when necessary,
    but the wait/notify methods have to be carefully programmed. 
    So version3 uses semaphores to easy the complex of programming by variable condition.
 

 
    
    