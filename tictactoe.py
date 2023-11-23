import os
import time
class Table:
  def __init__(self):
    self.table = ""
    self.turn = 1
    self.cross_list = []
    self.circle_list = []
    self.rows = []
    self.player = ""
    self.check_table = []
    square = 1

    for row in range(3):
      a = ""
      for num in range(1, 4):
          a += ("|" + str(square))
          square += 1
      a += "|"
      self.rows.append(a)
    self.table = "\n".join(self.rows)
    print(self.table)

    for row in self.rows:
      self.check_table.append(row.split("|")[1:4])
    #print(self.check_table)


  def play(self):
    if self.turn % 2 == 1:
      self.player = "X"
    else:
      self.player = "O"
    
    square = input(f"{self.player} turn: ")
    if square in self.table:
      os.system('clear')
      self.table = self.table.replace(square, self.player)
      self.update_check_table(square)

      if self.player == "X":
        self.cross_list.append(int(square))
        # print(self.check_table)
      else:
        self.circle_list.append(int(square))

      print("cross:", self.cross_list)
      print("circle:", self.circle_list)
      self.turn += 1
      print(self.table)

      if self.draw():
        print("Draw")

      if self.check(self.player):
        print(self.player, "Wins")

      if self.play_again():
        os.system("clear")
        new_game = Table()
        new_game.play()

      self.play()

    else:
      print("Error")
      self.play()

  #replace the list with X O
  def update_check_table(self, square):
    for row in range(3):
      for col in range(3):
        if self.check_table[row][col] == square:
          self.check_table[row][col] = self.player


  #check row
  def check(self, player):
    for row in self.check_table:
      if row.count(self.player) == 3:
        return True

    #check column
    for column in range(3):
      if all(row[column] == self.player for row in self.check_table):
        return True

    #check diagnol    
    for i in range(3):
      if all(self.check_table[i][i]) == self.player or all(self.check_table[i][2-i]) == self.player:
        return True

  #check Draw condition
  def draw(self):
    if self.turn == 10:
      return True
      
  def play_again(self):
    if self.check(self.player):
      print("Wanna play again? (yes/no)")
      choice = input().lower().strip()
      if choice == "yes":
        return True
      else:
        print("Ok bái bai")
        time.sleep(3)
        os._exit(0)

att_1 = Table()
att_1.play()