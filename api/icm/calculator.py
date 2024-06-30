from random import random

class Calculator():

	def trial(weights, payouts):
		scores = sorted((random() ** weight, i) for i, weight in enumerate(weights))
		results = [0] * len(payouts)
		for payout, score in zip(payouts, scores): results[score[1]] = payout
		return results

	def sicm(stacks, payouts, trials):
		avg = sum(stacks) / float(len(stacks))
		payouts += [0] * (len(stacks) - len(payouts))
		payouts.sort()
		weights = [avg / s for s in stacks]
		return [sum(player) / float(trials) for player in zip(*(
			Calculator.trial(weights, payouts) for i in range(trials)
		))]