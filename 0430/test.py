players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

# ----------------------------------------------------------------
# 배열 통해 계산 -> 테스트 미통과!

for i in range(len(callings)):
	player = callings[i]
	# print(players.index(player)) # 이름이 호명된 애들의 위치
	# print(players.index(player)-1)
	idx = players.index(player)
	players[idx-1], players[idx] = players[idx], players[idx-1]
	# print(players)

def solution(players, callings):
	for c in callings :
		idx = players.index(c)
		players[idx-1], players[idx] = players[idx], players[idx-1]
	
	return players



# ----------------------------------------------------------------
# dict 풀이

player_dict = {}
for i in range(len(players)):  # O(N)
	player_dict[players[i]] = i



idx_dict = {}
for i in range(len(players)):
	idx_dict[i] = players[i]

def solution(players, callings):
	for c in callings :
		cur_player = c  # 현재 선수의 이름
		cur_idx = player_dict[c]    #현재 선수의 등수

		# 앞의 선수의 정보 가져오기
		front_idx = cur_idx -1 # 앞 선수의 등수
		front_player = idx_dict[front_idx]  # 앞 선수의 이름

		# 두 선수의 정보를 바꿔치기
		player_dict[cur_player], player_dict[front_player] = front_idx, cur_idx # 등수 정보 바꿔치기
		idx_dict[cur_idx], idx_dict[front_idx] = front_player, cur_player # 선수명 정보 바꿔치기
	
	return (idx_dict)


# ----------------------------------------------------------------
# 각각 합쳐보자

def solution(players, callings):
	player_dict = {}
	idx_dict = {}
	for i in range(len(players)):  # O(N)
		player_dict[players[i]] = i
		idx_dict[i] = players[i]

	for c in callings :
		cur_player = c  # 현재 선수의 이름
		cur_idx = player_dict[c]    #현재 선수의 등수

		# 앞의 선수의 정보 가져오기
		front_idx = cur_idx -1 # 앞 선수의 등수
		front_player = idx_dict[front_idx]  # 앞 선수의 이름

		# 두 선수의 정보를 바꿔치기
		player_dict[cur_player], player_dict[front_player] = front_idx, cur_idx # 등수 정보 바꿔치기
		idx_dict[cur_idx], idx_dict[front_idx] = front_player, cur_player # 선수명 정보 바꿔치기
	
	return list(idx_dict.values())


# ----------------------------------------------------------------
# 범T code_1

def solution(players, callings) :
	dic = {}
	for i, player in enumerate(players) :
		dic[player] = i

	for c in callings:
		tmp  = players[dic[c] - 1]
		players[dic[c]], players[dic[c] - 1] =  players[dic[c] - 1], players[dic[c]]
		dic[c] -= 1
		dic[tmp] += 1

	return players

# ----------------------------------------------------------------
# 범T code_2

def solution(players, callings) :
	dic = {}
	for i, player in enumerate(players) :
		dic[player] = i

	for c in callings:
		tmp  = players[dic[c] - 1]
		players[dic[c]], players[dic[c] - 1] =  players[dic[c] - 1], players[dic[c]]
		dic[c] , dic[tmp] = dic[tmp], dic[c]

	return players

# ----------------------------------------------------------------
# 범T code_3

players = ["mumu", "seo", "poe", "kai", "mine"]
callings = ["kai","kai", "mine", "mine"]

def solution(players, callings) :
	dic = dict(zip(players, list(range(len(players)))))

	for c in callings:
		tmp = players[dic[c] - 1]
		players[dic[c]], players[dic[c] - 1] =  players[dic[c] - 1], players[dic[c]]
		dic[c] , dic[tmp] = dic[tmp], dic[c]

	return players
