empty_board =[' ']*9

def print_board(board):
    print('[{}]\n[{}]\n[{}]'.format(']['.join(board[:3]),']['.join(board[3:6]),']['.join(board[6:])))

def get_play(player,board):
  try:
    play = int(input('Player {}, Make a play: '.format(player)))
    if play in range(1,10):
      if board[play-1] == ' ':
        return play
  except ValueError:
    pass
  print('That is not a valid play!')
  play = get_play(player,board)
  return play
  
def update_board(board,player,play):
  if player==1:
    board[play-1] = 'X'
  else:
    board[play-1] = 'O'
  return board

def check_win(board):
  wins = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]
  plays = [set([n for n,x in enumerate(board) if x == 'X']),set([n for n,x in enumerate(board) if x == 'X'])]
  for w in wins:
    if w <= plays[0] or w <= plays[1]
  
  return any((i in w for i in plays))

def play():
  board = empty_board
  player = 1
  for n in range(9):
    print_board(board)
    play = get_play(player,board)
    board = update_board(board,player,play)
    if n>3 and check_win(board):
      print_board(board)
      print('Player {} won!'.format(player))
      play_again = input('Do you want to play again? (Y/N): ').upper() == 'Y'
    player ^= 0b11
  else:
    print_board(board)
    print('No winner.')
    play_again = input('Do you want to play again? (Y/N): ').upper() == 'Y'
  
  if play_again:
    play()

play()
