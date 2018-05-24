# Multilevel-Feedback-Queue-Sheduling
#### Planning using a multi-level queue with reverse links

Normal multi-level queue does not allow moving the application between queues. 
The multi-level queue with reverse links assumes that applications under certain conditions can move between queues.
The processes initially fall into the queue 0, where each of them has a quantum of time equal to 8 ms. 
Those processes that have not been executed during this time are moved to the queue 1. 
Processes from queue 1 begin to be processed only when the queue 0 becomes empty. 
Those processes that are not executed in queue 1 (q = 16 ms) are moved to queue 2. 
Processes from queue 2 will only be processed if the queues 0 and 1 become blank.

The strategy combines the properties of SJF (Shortest Job First)
#
Data is read from "process.txt".  
First line: n - number of queues  
Line x + 1 (0 <= x <= 32): time of execution of queue x processes [t1, t2, ..., tn]
***
#### Планування з використанням багаторівневої черги з оберненими зв’язками
Звичайна багаторівнева черга не допускає переміщення заявки між чергами. 
Багаторівнева черга з оберненими зв'язками передбачає, що заявки при певних умовах можуть переміщатися між чергами.
Процеси початково потрапляють в чергу 0, де кожному із них надається квант часу, рівний 8 мс. 
Ті процеси, котрі не  встигли виконатися протягом цього часу, переміщаються в чергу 1. 
Процеси із черги  1  починають оброблятися тільки тоді, коли  черга 0 стає пустою. 
Ті процеси, котрі не виконались в черзі 1 (q=16 мс) переміщаються в чергу 2. 
Процеси із черги 2 будуть оброблятися тільки в тому випадку, якщо стають  пустими черги  0 та 1.

Cтратегія поєднує в собі властивості SJF (Shortest Job First)
#
Дані зчитуються з файлу "processes.txt".  
Перший рядок: n - кількість черг  
Рядок x+1 (0<=x<=32): час виконання процесів черги x [t1, t2, ..., tn]
