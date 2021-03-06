import math


class GNB(object):
    def __init__(self):
        self.possible_labels = ['left', 'keep', 'right']

    def train(self, data, labels):
        """
		Trains the classifier with N data points and labels.

		INPUTS
		data - array of N observations
		  - Each observation is a tuple with 4 values: s, d,
			s_dot and d_dot.
		  - Example : [
				[3.5, 0.1, 5.9, -0.02],
				[8.0, -0.3, 3.0, 2.2],
				...
			]

		labels - array of N labels
		  - Each label is one of "left", "keep", or "right".

		"""

        ## Here we separate data according to classes
        def separateByClass(data, labels):
            separated = {}
            for i in range(len(data)):
                vector = data[i]
                if (labels[i] not in separated):
                    separated[labels[i]] = []
                separated[labels[i]].append(vector)
            return separated

        ## Calculate mean and standard deviation of the data
        def mean(numbers):
            return sum(numbers) / float(len(numbers))

        def stdev(numbers):
            avg = mean(numbers)
            variance = sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers) - 1)
            return math.sqrt(variance)

        def summarize(data):
            summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*data)]
            return summaries

        def summarizeByClass(data, labels):
            separated = separateByClass(data, labels)
            summaries = {}
            for direction, locationVector in separated.items():
                summaries[direction] = summarize(locationVector)
            return summaries

        self.trainedData = summarizeByClass(data, labels)

    def predict(self, observation):
        """
		Once trained, this method is called and expected to return
		a predicted behavior for the given observation.

		INPUTS

		observation - a 4 tuple with s, d, s_dot, d_dot.
		  - Example: [3.5, 0.1, 8.5, -0.2]

		OUTPUT

		A label representing the best guess of the classifier. Can
		be one of "left", "keep" or "right".
		"""

        # TODO - complete this


        def calculateProbability(observation, mean, stdev):
            exponent = math.exp(-(math.pow(observation - mean, 2) / (2 * math.pow(stdev, 2))))
            return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent

        def calculateClassProbabilities(trainedData, observation):
            probabilities = {}
            for classValue, classSummaries in trainedData.items():
                probabilities[classValue] = 1
                for i in range(len(classSummaries)):
                    mean, stdev = classSummaries[i]
                    x = observation[i]
                    probabilities[classValue] *= calculateProbability(x, mean, stdev)
            return probabilities

        def predictLabel(trainedData, observation):
            probabilities = calculateClassProbabilities(trainedData, observation)
            bestLabel, bestProb = None, -1
            for classValue, probability in probabilities.items():
                if bestLabel is None or probability > bestProb:
                    bestProb = probability
                    bestLabel = classValue
            return bestLabel

        self.possible_labels = predictLabel(self.trainedData, observation)
        return self.possible_labels
