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
            sumTaskNumber = 0
            sumWholeTaskIntensity = 0
            sumWholeTaskFactAverageProcessingTime = 0

            p = [0] * self.priorityNumber
            Pi = [0] * self.priorityNumber
            w = [0] * self.priorityNumber

            for i in xrange(self.priorityNumber):
                sumTaskNumber += self.taskNumber[i]
                sumWholeTaskIntensity += self.taskNumber[i] * self.averageIntensity[i]
                sumWholeTaskFactAverageProcessingTime += self.taskNumber[i] * self.factAverageProcessingTime[i]
                p[i] = self.averageIntensity[i] * self.factAverageProcessingTime[i]

            sumIntensity = sumWholeTaskIntensity / sumTaskNumber
            sum_v = sumWholeTaskFactAverageProcessingTime / sumTaskNumber
            sum_p = sumIntensity * sum_v

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
                    tmpMul *= (self.priorityNumber - j - 1)
                    Pi[i] = tmpMul * (sum_p ** (i + 1)) * P0

            for i in xrange(self.priorityNumber):
                w[i] = self.taskNumber[i] - (1 - Pi[i]) / p[i]

            while len(self.averageWaitingTime) < self.priorityNumber:
                self.averageWaitingTime.append(0.0);

            while len(self.fullAverageProcessingTime) < self.priorityNumber:
                self.fullAverageProcessingTime.append(0.0)

            for i in xrange(self.priorityNumber):
                self.fullAverageProcessingTime[i] = self.factAverageProcessingTime[i] * w[i] + \
                                                    self.factAverageProcessingTime[i] * Pi[i]
                self.averageWaitingTime[i] = self.fullAverageProcessingTime[i] - \
                                             self.factAverageProcessingTime[i]

def main():
    process = ProcessModel()
    process.addPriorityFromFile('data.txt')
    process.calculateTime()
    print process.fullAverageProcessingTime
    print process.averageWaitingTime


if __name__ == '__main__':
    main()

