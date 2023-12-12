# -*- coding: utf-8 -*-

from collections import deque

def solution(board, moves):
    # moves를 순회하며 위치정보 move 를 가져옴 -> 큐 
    moves = deque(moves)
    doll = []
    cnt = 0

    while moves:
        move = moves.popleft() 
        # board[i][move-1] 를 순회한다 (0<= i <= board의 길이)
        for i in range(len(board)):
            # 0이 아닌 값이면, 
            if board[i][move-1] != 0:
                # doll(뽑힌 인형 정보 저장)에 해당 인형값 저장 
                # doll의 마지막 값과 같으면, pop 및 count+2 
                if doll and board[i][move-1] == doll[-1]:
                    doll.pop()
                    cnt += 2
                # 다르면, doll 에 append 
                else:
                    doll.append(board[i][move-1]) 

                board[i][move-1] = 0
                break

    return cnt
