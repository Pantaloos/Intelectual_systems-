from random import shuffle
import numpy as np

class Eight:
    def rand_matrix(self): # creating random matrix
        start_matrix = list(range(0,9)) # creating list of 8 numbers
        shuffle(start_matrix) # shuffling numbers
        return (start_matrix)

    move = {"up": -3, "down": 3, "left": -1, "right": 1} # movement rules

    def possible_positions(self, matrix): # function to determin next possible positions
        zero_index = matrix.index(0) # index of 0
        zero_row = zero_index // 3 # horizontal movement
        zero_column = zero_index % 3 # vertical movement
        pos_positions = [] # array of next possible position

        if zero_row == 0: # when we can move down
            pos_positions.append(self.move["down"]) 
        elif zero_row == 1: # when we can move up and down
            pos_positions.append(self.move["up"])
            pos_positions.append(self.move["down"])
        elif zero_row == 2: #when we can move up
            pos_positions.append(self.move["up"])
        if zero_column == 0: #when we can move right
            pos_positions.append(self.move["right"])
        elif zero_column == 1: #when we can right and left
            pos_positions.append(self.move["right"])
            pos_positions.append(self.move["left"])
        elif zero_column == 2: #when we can move left
            pos_positions.append(self.move["left"])

        return pos_positions

    def possible_next_position(self, matrix): # function to get next possible move
        zero_index = matrix.index(0) # index of 0
        pos_next_pos = [] # array of next possible position
        pos_position = self.possible_positions(matrix) # array of possible next position for current position

        for i in pos_position:
            new_pos = zero_index + i # changing index of 0
            temp_matrix = matrix.copy() # creating new matrix to change indexes
            temp_value = temp_matrix[new_pos] # index of 0's new position is stored in temp_value
            temp_matrix[new_pos] = temp_matrix[zero_index] # X number's index is replaced by 0's index
            temp_matrix[zero_index] = temp_value # 0's index is replaced by X's index
            pos_next_pos.append(temp_matrix) # adding temp_matrix to array of possible next positions
            temp_value = "" # making temp_value blank again

        return pos_next_pos

    def print_pos(self, matrix): # showing matrix as 3x3
        array_2d = np.reshape(matrix, (3,3)) # reshaping matrix as 3x3
        print (array_2d) # printing array

    def bfs(self, start_matrix, final_matrix): # BFS
        visited_pos = [] # array of visited positions
        posistion_queu = [] # array of positions queus
        visited_pos.append(str(start_matrix)) # adding start matrix to visidet positions
        posistion_queu.append(start_matrix) # adding start matrix to the queu

        print ("Start matrix =", start_matrix, "Final matrix =", final_matrix) #showing our start and final matrix
        while posistion_queu: # while queu isn't empty
            i = posistion_queu.pop(0) # taking out element with index 0 from queu
            if str(i) == str(final_matrix): # checking if current position is our final position
                return f"we found your solution for  {start_matrix} --> {final_matrix}, \nVisited Nodes = {len(visited_pos)}, \t Closed Nodes = {len(posistion_queu)}" # priting answer

            for neighbour in self.possible_next_position(i): # if current position isn't final position check neighbours
                if str(neighbour) not in visited_pos: # if neighbour isn't visited do next
                    visited_pos.append(str(neighbour)) # add neighbour to array of visited positions
                    posistion_queu.append(neighbour) # add neighbour to queu
                    print (self.possible_next_position(neighbour)) # printing possible next moves for current array

    def dfs(self, start_matrix, final_matrix): # DFS
        visited_nodes = {str(start_matrix): True} # adding start matrix to the visited nodes
        stack = [] # array of 
        stack.append(start_matrix) # adding start matrix to the stack

        print ("Start matrix =", start_matrix, "Final matrix =", final_matrix) # printing starting and final matrix
        while stack: # while stack isn't empty
            current_pos = stack.pop(0) # taking array with index 0 from the stack

            if current_pos == final_matrix: # if current array is our final array
                return f"We found solution for {start_matrix} --> {final_matrix}, \nVisited Nodes = {len(visited_nodes)}, \t Closed Nodes = {len(stack)}" # printing our result
            else:
                for next_pos in self.possible_next_position(current_pos): # taking next possible position for current position
                    next_state = str(next_pos) # saving next position as string
                    if not visited_nodes.get(next_state, False): # if our position isn't visited
                        stack.append(next_pos) # add it to the stack
                        visited_nodes[next_state] = True # declare next state as visited position
                        print (self.possible_next_position(next_pos)) # printing next possible positions for the current one


k = Eight()

rand_start = k.rand_matrix()
rand_finish = k.rand_matrix()

# p = k.bfs([2,8,3,1,6,4,7,0,5],[1,2,3,8,0,4,7,6,5])
# p = k.dfs([2,8,3,1,6,4,7,0,5],[1,2,3,8,0,4,7,6,5])
# p = k.bfs(rand_start, rand_finish)
p = k.dfs(rand_start, rand_finish)


print(p)