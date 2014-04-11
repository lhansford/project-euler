from collections import Counter

SCORE = {
	'rflush':9,
	'sflush':8,
	'four':7,
	'full':6,
	'flush':5,
	'straight':4,
	'three':3,
	'twopairs':2,
	'pair':1,
	'high':0
}

def has_royal_flush(cards):
	flush = ['T','J','Q','K','A']
	for c in cards:
		if c[1] != cards[0][1]:
			return False
		elif c[0] not in flush:
			return False
	return True

def has_straight_flush(cards):
	if has_flush(cards):
		return has_straight(cards)
	return False

def has_flush(cards):
	for c in cards:
		if c[1] != cards[0][1]:
			return False
	return True

def has_straight(cards):
	order = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
	ordered_hand = sorted([c[0] for c in cards], cmp=card_order)
	if ordered_hand == ['A','2','3','4','5']:
		return True 
	i = order.index(ordered_hand.pop(0))
	for c in ordered_hand:
		i+=1
		if order.index(c) != i:
			return False
	return True

def has_full_house(cards):
	return len(set([c[0] for c in cards])) == 2 and not has_four_of_kind(cards)

def has_four_of_kind(cards):
	values = {}
	for c in cards:
		if values.get(c[0]):
			values[c[0]] += 1
		else:
			values[c[0]] = 1
	if values[cards[0][0]] == 4:
		return True, [cards[0] for x in xrange(4)], [c for c in cards if c[0] != cards[0][0]]
	elif values[cards[1][0]] == 4:
		return True, [cards[1] for x in xrange(4)], [c for c in cards if c[0] != cards[1][0]]
	return False, [], cards

def has_three_of_kind(cards):
	values = {}
	for c in cards:
		if values.get(c[0]):
			values[c[0]] += 1
		else:
			values[c[0]] = 1
	if values[cards[0][0]] == 3:
		return True, [cards[0] for x in xrange(3)], [c for c in cards if c[0] != cards[0][0]]
	elif values[cards[1][0]] == 3:
		return True, [cards[1] for x in xrange(3)], [c for c in cards if c[0] != cards[1][0]]
	elif values[cards[2][0]] == 3:
		return True, [cards[2] for x in xrange(3)], [c for c in cards if c[0] != cards[2][0]]
	return False, [], cards

def has_two_pairs(cards):
	counted = Counter([c[0] for c in cards])
	if sorted(counted.values()) == [1,2,2]:
		singleton = [c for c in cards if counted[c[0]] == 1]
		return True, [c for c in cards if c != singleton[0]], singleton
	return False, [], cards

def has_pair(cards):
	counted = Counter([c[0] for c in cards])
	if sorted(counted.values()) == [1,1,1,2]:
		pair = [c for c in cards if counted[c[0]] == 2]
		return True, pair, [c for c in cards if c not in pair]
	return False, [], cards

def get_highest(p1,p2):
	if p1[0] == 9:
		return None
	if p1[0] == 8 or p1[0] == 7 or p1[0] == 5:
		p1_highest = sort_hand(p1[1])[4][0]
		p2_highest = sort_hand(p2[1])[4][0]
		if p1_highest == p2_highest:
			return None
		return higher_card(p1_highest, p2_highest)
	if p1[0] == 6:
		p1_counted = Counter([c[0] for c in p1[1]])
		p2_counted = Counter([c[0] for c in p2[1]])
		p1_three = [c for c in p1_counted.keys() if p1_counted[c] == 3]
		p2_three = [c for c in p2_counted.keys() if p2_counted[c] == 3]
		if p1_three[0] == p2_three[0]:
			return None
		return higher_card(p1_three[0], p2_three[0])
	if p1[0] == 4:
		if 'A' in [c[0] for c in p1[1]] and 'A' in [c[0] for c in p2[1]]:
			if 'K' in [c[0] for c in p1[1]] and 'K' in [c[0] for c in p2[1]]:
				return None
			elif 'K' in [c[0] for c in p1[1]]:
				return True
			else:
				return False
		else:
			p1_highest = sort_hand(p1[1])[4][0]
			p2_highest = sort_hand(p2[1])[4][0]
			if p1_highest == p2_highest:
				return None
			return higher_card(p1_highest, p2_highest)
	if p1[0] == 3:
		if p1[1][0] == p2[1][0]:
			return None
		return higher_card(p1[1][0], p2[1][0])
	if p1[0] == 2:
		p1_sorted = sort_hand(p1[1])
		p2_sorted = sort_hand(p2[1])
		if p1_sorted[4][0] == p2_sorted[4][0]:
			if p1_sorted[2][0] == p2_sorted[2][0]:
				if p1[2][0] == p2[2][0]:
					return None
				else:
					return higher_card(p1[2][0], p2[2][0])
			else:
				return higher_card(p1_sorted[2][0], p2_sorted[2][0])
		else:
			return higher_card(p1_sorted[4][0], p2_sorted[4][0])
	if p1[0] == 1:
		if p1[1][1][0] == p2[1][1][0]:
			return get_highest_card(p1[2],p2[2])
		else:
			return higher_card(p1[1][1][0], p2[1][1][0])
	else:
		return get_highest_card(p1[2],p2[2])

def sort_hand(cards):
	return sorted([c[0] for c in cards], cmp=card_order)

def card_order(x, y):
	order = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
	return order.index(x) - order.index(y)

def higher_card(c1,c2):
	order = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
	return order.index(c1) > order.index(c2)

def get_highest_card(h1,h2):
	h1 = sort_hand(h1)[::-1]
	h2 = sort_hand(h2)[::-1]
	for x in xrange(0,len(h1)):
		if not h1[x] == h2[x]:
			return higher_card(h1[x], h2[x])
	return None

def get_hands(line):
	hands = [(c[0],c[1]) for c in line.split(" ")]
	return hands[:5], hands[5:]

def test_hands(hand1, hand2):
	p1 = get_result(hand1)
	p2 = get_result(hand2)
	if p1[0] == p2[0]:
		return get_highest(p1,p2)
	elif p1[0] < p2[0]:
		return False
	else:
		return True

def get_result(hand):
	if has_royal_flush(hand):
		return SCORE['rflush'],hand,[]
	if has_straight_flush(hand):
		return SCORE['rflush'],hand,[]
	four, win, rem = has_four_of_kind(hand)
	if four:
		return SCORE['four'],win,rem
	if has_full_house(hand):
		return SCORE['full'],hand,[]
	if has_flush(hand):
		return SCORE['flush'],hand,[]
	if has_straight(hand):
		return SCORE['straight'],hand,[]
	three, win, rem = has_three_of_kind(hand)
	if three:
		return SCORE['three'],win,rem
	twopairs, win, rem = has_two_pairs(hand)
	if twopairs:
		return SCORE['twopairs'],win,rem
	pair, win, rem = has_pair(hand)
	if pair:
		return SCORE['pair'],win,rem
	else:
		return SCORE['high'],[],hand


def tally_results(file):
	results = {'p1':0,'p2':0,'tie':0}
	with open(file,'r') as hands:
		for line in hands.readlines():
			h1,h2 = get_hands(line)
			r = test_hands(h1,h2)
			if r == True:
				results['p1'] += 1
			elif r == False:
				results['p2'] += 1
			else:
				results['tie'] += 1
	return results

print tally_results('resources/poker.txt')