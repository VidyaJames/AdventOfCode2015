f = open('day15-input.txt', 'r')

ingredients = []
capacity = {}
durability = {}
flavor = {}
texture = {}
calories = {}

for i in f.readlines():
	i = i.split(" ")
	ingredient = i[0][0:-1]
	ingredients.append(ingredient)
	capacity[ingredient] = int(i[2][0:-1])
	durability[ingredient] = int(i[4][0:-1])
	flavor[ingredient] = int(i[6][0:-1])
	texture[ingredient] = int(i[8][0:-1])
	calories[ingredient] = int(i[10][0:-1])

permutations = []
for i in ingredients:
	permutations.append(1)

goodPermutations = []
while permutations[0] != 101 - len(permutations):
	permutations[-1] += 1
	index = len(permutations) - 1
	while permutations[index] > 101 - len(permutations):
		permutations[index] = 1
		index -= 1
		permutations[index] += 1
	if sum(permutations) == 100:
		goodPermutations.append(permutations[:])

best = 0
for i in goodPermutations:
	calorieCount = 0
	j = 0
	while j < len(ingredients):
		calorieCount += i[j] * calories[ingredients[j]]
		j += 1
	if calorieCount != 500:
		continue
	score = 0
	j = 0
	capacityScore = 0
	durabilityScore = 0
	flavorScore = 0
	textureScore = 0
	while j < len(ingredients):
		capacityScore += i[j] * capacity[ingredients[j]]
		durabilityScore += i[j] * durability[ingredients[j]]
		flavorScore += i[j] * flavor[ingredients[j]]
		textureScore += i[j] * texture[ingredients[j]]
		j += 1
	if capacityScore < 0 or durabilityScore < 0 or flavorScore < 0 or textureScore < 0:
		continue
	score = capacityScore * durabilityScore * flavorScore * textureScore
	if score > best:
		best = score
print "The best possible score is " + str(best) + "."
