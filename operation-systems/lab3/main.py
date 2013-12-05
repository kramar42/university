#! /usr/bin/env python

class ProcessModel:
        def __init__(self):
            self.priorityNumber = 0
            self.taskNumber = []
            self.averageIntensity = []
            self.factAverageProcessingTime = []
            self.averageWaitingTime = []
            self.fullAverageProcessingTime = []

        def addPriority(self, taskNumber, averageIntensity, factAverageProcessingTime):
            self.taskNumber.append(taskNumber)
            self.averageIntensity.append(averageIntensity)
            self.factAverageProcessingTime.append(factAverageProcessingTime)
            self.priorityNumber += 1

        def addPriorityFromFile(self, fileName):
            for line in open(fileName).xreadlines():
                self.addPriority(*map(int, line.split(' ')))

        def calculateTime(self):
            sumTaskNumber = sum(self.taskNumber[i] for i in xrange(self.priorityNumber))
            sumWholeTaskIntensity = sum(self.taskNumber[i] * self.averageIntensity[i] for i in xrange(self.priorityNumber))
            sumWholeTaskFactAverageProcessingTime = sum(self.taskNumber[i] * self.factAverageProcessingTime[i] for i in xrange(self.priorityNumber))

            sumIntensity = sumWholeTaskIntensity / sumTaskNumber
            sum_v = sumWholeTaskFactAverageProcessingTime / sumTaskNumber
            sum_p = sumIntensity * sum_v

            p = [self.averageIntensity[i] * self.factAverageProcessingTime[i] for i in xrange(self.priorityNumber)]
            Pi = [0] * self.priorityNumber
            w = [0] * self.priorityNumber

            tmpSum = 1
            for i in xrange(self.priorityNumber):
                tmpMul = self.priorityNumber
                for j in xrange(i):
                    tmpMul *= (self.priorityNumber - j - 1)
                    tmpMul *= sum_p ** (i + 1)
                    tmpSum += tmpMul
            P0 = 1 / tmpSum

            for i in xrange(self.priorityNumber):
                tmpMul = self.priorityNumber
                for j in xrange(i):
                    tmpMul *= self.priorityNumber - j - 1
                    Pi[i] = tmpMul * (sum_p ** (i + 1)) * P0

            w = [self.taskNumber[i] - (1 - Pi[i]) / p[i] for i in xrange(self.priorityNumber)]
            
            self.averageWaitingTime += [0.0] * (self.priorityNumber - len(self.averageWaitingTime))
            self.fullAverageProcessingTime += [0.0] * (self.priorityNumber - len(self.fullAverageProcessingTime))

            self.fullAverageProcessingTime = [self.factAverageProcessingTime[i] * w[i] + \
                    self.factAverageProcessingTime[i] * Pi[i] \
                    for i in xrange(self.priorityNumber)]
            self.averageWaitingTime = [self.fullAverageProcessingTime[i] - \
                    self.factAverageProcessingTime[i] \
                    for i in xrange(self.priorityNumber)]

def main():
    process = ProcessModel()
    process.addPriorityFromFile('data.txt')
    process.calculateTime()
    print 'Full average processing time:', process.fullAverageProcessingTime
    print 'Average waiting time:', process.averageWaitingTime


if __name__ == '__main__':
    main()

