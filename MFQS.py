"""
SERVICE PROCESS STRATEGY
MFQS (MULTILEVEL FEEDBACK QUEUE SHEDULING)
"""

class Queue:
    """
    Queue with the implementation of (SJF)Shortest Job First
    """
    def __init__(self, quantum, num, curQueue, processes = []):
        self.processes = []
        self.quantum = quantum              #quantum time
        self.performed = []                 #list of performed processes
        self.nonPerformed = []              #list of uncompleted processes
        self.num = num                      #number of processes in the higher priority queues(for numbering)
        self.curQueue = curQueue
        
        for i in range(len(processes)):
            self.processes.append([self.num+i, processes[i]])    #list of processes [number, run-time]
        self.sortProcesses()                #sort processes

    def __str__(self):
        return "{0}\nQUEUE {1}\n{2}\nquantum = {3} ms\nPerformed processes: {4}\nNonperformed processes: {5}".format(
            "="*60, self.curQueue,"-"*60, self.quantum, [process for process in self.performed], [process for process in self.nonPerformed])

    def __iter__(self):
        return self
    
    def addProcesses(self, elem):
        """
        Add processes not performed in the previous queue to the current queue
        """
        for el in elem:
            self.processes.append(el)
        self.sortProcesses()

    def insertProcesses(self, process):
        """
        Add processes to the current queue
        """
        self.processes = process

    def addWT(self):
        """
        Add a wait time for each process
        """
        for process in self.processes:
            global totalTime
            WaitTime[process[0]] = totalTime
            totalTime += process[1]
    
    def sortProcesses(self):
        """Sort process by lead time"""
        self.processes = sorted(self.processes, key = lambda x: x[-1])     #отсортировать по времени выполнения
        
    def perform(self):
        """
        Perform processes in one quantum
        """
        for process in self.processes:
            process[-1] -= self.quantum
            if process[-1] > 0:
                self.nonPerformed.append(process)
            else:
                process[-1] = 0
                self.performed.append(process)
            
    def giveProcesses(self):
        """Get the executed and not executed processes of the current queue of the current quantum"""
        return self.performed, self.nonPerformed


def readFile(listQueues):
    """
    Read the file and distribute the processes in queues
    """
    f = open('processes.txt', 'r')

    global maxQueues
    global k
    global q
    global num
    global currentQueue
    maxQueues = int(f.readline()) #number of queues
    q = 2                   #time of one quantum
    num = 1                 #process number
    for line in f:
        lineProcesses = []
        q*=2                #increase the quantum time for the next turn
        for i in line.split():
            if i.isdigit():
                lineProcesses.append(int(i))
        que = Queue(q, num, currentQueue, lineProcesses)
        listQueues.append(que)

        currentQueue+=1         #increase queue number
        num += len(line.split())  #initial value for the process numbers of the trace queue
        k+=1
    return [queue for queue in listQueues]

if __name__ == "__main__":
    nonPerformed = []
    listQueues = []         #queue list
    WaitTime = {}
    totalTime = 0
    q = 0
    k = 0                   #number of queues
    currentQueue = 0
    num = 0
    maxQueues = 0
    listQueues = readFile(listQueues)
    i = 0

    while True:
        que = Queue(q, num, k-1)
        if i < k:
            if nonPerformed:
                listQueues[i].addProcesses(nonPerformed)
        else:
            if nonPerformed:
                que.insertProcesses(nonPerformed)
                listQueues.insert(i, que)

        listQueues[i].addWT()
        listQueues[i].perform()
        print(listQueues[i])
        nonPerformed = listQueues[i].giveProcesses()[-1]
        i+=1
        if not nonPerformed and i >= k: break
    print("="*60)
    print("Process => Wait Time")
    WaitTime = dict(sorted(WaitTime.items(), key = lambda x: x[-1])) #sort wait time

    sum = 0
    for process in WaitTime:
        sum += WaitTime[process]
        print("{0:5}   => {1:7}".format(process, WaitTime[process]))
    print("="*50)
    print("Average wait time = {0:.3f}".format(sum/len(WaitTime)))
    print("="*50)
