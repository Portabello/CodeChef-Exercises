numRounds = int(input())
maxLead = 0
winner = None
for x in range(0,numRounds):
	score = input().split()
	player1 = int(score[0])
	player2 = int(score[1])
	lead = abs(player1 - player2)
	if lead > maxLead:	
		if player1 > player2:
			winner = 1
			maxLead = lead
		if player1 < player2:
			winner = 2
			maxLead = lead	
print(str(winner) + " "+str(maxLead))
	