# MLA0201
.. 


## 1. Minimax Algorithm

**Objective:** Determine optimal move in game tree using recursive evaluation

```
ALGORITHM MINIMAX(node, depth, maximizingPlayer)
    IF depth = MAX_DEPTH OR node is terminal THEN
        RETURN heuristic_value(node)
    END IF
    
    IF maximizingPlayer THEN
        maxEval ← negative infinity
        FOR EACH child IN node.children DO
            eval ← MINIMAX(child, depth + 1, FALSE)
            maxEval ← MAX(maxEval, eval)
        END FOR
        RETURN maxEval
    ELSE
        minEval ← positive infinity
        FOR EACH child IN node.children DO
            eval ← MINIMAX(child, depth + 1, TRUE)
            minEval ← MIN(minEval, eval)
        END FOR
        RETURN minEval
    END IF
END ALGORITHM
```

---

## 2. Tic Tac Toe Game

**Objective:** Implement complete game flow with win condition detection

```
ALGORITHM TicTacToe()
    board ← Initialize 3×3 empty grid
    currentPlayer ← "X"
    gameActive ← TRUE
    
    WHILE gameActive = TRUE DO
        DISPLAY board to user
        move ← GetPlayerMove(currentPlayer)
        
        IF IsValidMove(board, move) THEN
            board[move] ← currentPlayer
        ELSE
            DISPLAY "Invalid move. Try again."
            CONTINUE
        END IF
        
        IF CheckWinCondition(board, currentPlayer) THEN
            DISPLAY "Player " + currentPlayer + " wins!"
            gameActive ← FALSE
        ELSE IF IsBoardFull(board) THEN
            DISPLAY "Game is a draw."
            gameActive ← FALSE
        ELSE
            currentPlayer ← (currentPlayer = "X") ? "O" : "X"
        END IF
    END WHILE
    
    RETURN game result
END ALGORITHM
```

---

## 3. Eight Queens Problem

**Objective:** Place 8 queens on chessboard using backtracking without mutual attack

```
ALGORITHM SolveEightQueens()
    board ← Initialize 8×8 empty grid
    solutions ← empty list
    
    FUNCTION PlaceQueens(column)
        IF column = 8 THEN
            solutions.append(COPY(board))
            RETURN TRUE
        END IF
        
        FOR row ← 0 TO 7 DO
            IF IsSafePosition(board, row, column) THEN
                board[row][column] ← "Q"
                
                IF PlaceQueens(column + 1) THEN
                    // Continue searching for other solutions
                END IF
                
                board[row][column] ← empty  // Backtrack
            END IF
        END FOR
        
        RETURN FALSE
    END FUNCTION
    
    PlaceQueens(0)
    RETURN solutions
END ALGORITHM
```

---

## 4. Alpha-Beta Pruning

**Objective:** Optimize minimax by eliminating non-promising branches

```
ALGORITHM AlphaBetaPruning(node, depth, alpha, beta, maximizingPlayer)
    IF depth = 0 OR node is terminal THEN
        RETURN evaluate(node)
    END IF
    
    IF maximizingPlayer THEN
        maxEval ← negative infinity
        FOR EACH child IN node.children DO
            eval ← AlphaBetaPruning(child, depth - 1, alpha, beta, FALSE)
            maxEval ← MAX(maxEval, eval)
            alpha ← MAX(alpha, eval)
            IF alpha ≥ beta THEN
                BREAK  // Beta cutoff: prune remaining branches
            END IF
        END FOR
        RETURN maxEval
    ELSE
        minEval ← positive infinity
        FOR EACH child IN node.children DO
            eval ← AlphaBetaPruning(child, depth - 1, alpha, beta, TRUE)
            minEval ← MIN(minEval, eval)
            beta ← MIN(beta, eval)
            IF alpha ≥ beta THEN
                BREAK  // Alpha cutoff: prune remaining branches
            END IF
        END FOR
        RETURN minEval
    END IF
END ALGORITHM
```

---

## 5. Map Coloring Problem

**Objective:** Color regions with minimum colors ensuring no adjacent regions share same color

```
ALGORITHM MapColoring(graph, numColors)
    colors ← empty array of size graph.numRegions
    colorSet ← {1, 2, ..., numColors}
    
    FUNCTION AssignColors(region)
        IF region = graph.numRegions THEN
            RETURN TRUE
        END IF
        
        FOR color IN colorSet DO
            IF IsSafeColor(graph, colors, region, color) THEN
                colors[region] ← color
                
                IF AssignColors(region + 1) THEN
                    RETURN TRUE
                END IF
                
                colors[region] ← UNASSIGNED  // Backtrack
            END IF
        END FOR
        
        RETURN FALSE
    END FUNCTION
    
    IF AssignColors(0) THEN
        RETURN colors
    ELSE
        RETURN "No solution with " + numColors + " colors"
    END IF
END ALGORITHM
```

---

## 6. Missionaries and Cannibals Problem

**Objective:** Transport all missionaries and cannibals across river safely using BFS

```
ALGORITHM MissionariesAndCannibals()
    initialState ← (3, 3, 1)  // (missionaries, cannibals, boat position)
    goalState ← (0, 0, 0)
    queue ← [initialState]
    visited ← {initialState}
    parent ← empty dictionary
    
    WHILE queue is not empty DO
        currentState ← queue.dequeue()
        
        IF currentState = goalState THEN
            path ← ReconstructPath(currentState, parent)
            RETURN path
        END IF
        
        FOR EACH nextState IN GenerateMoves(currentState) DO
            IF IsValidState(nextState) AND nextState NOT IN visited THEN
                visited.add(nextState)
                parent[nextState] ← currentState
                queue.enqueue(nextState)
            END IF
        END FOR
    END WHILE
    
    RETURN "No solution found"
END ALGORITHM
```

---

## 7. Cryptarithmetic

**Objective:** Find digit assignments to letters satisfying arithmetic equation

```
ALGORITHM CryptarithmeticSolver(equation)
    letters ← ExtractUniqueLetters(equation)
    leadingLetters ← ExtractLeadingLetters(equation)
    
    FOR EACH permutation IN GeneratePermutations(0-9, length=letters) DO
        assignment ← MapLettersToDigits(letters, permutation)
        
        // Validate leading zeros constraint
        validAssignment ← TRUE
        FOR EACH letter IN leadingLetters DO
            IF assignment[letter] = 0 THEN
                validAssignment ← FALSE
                BREAK
            END IF
        END FOR
        
        IF validAssignment THEN
            result ← EvaluateEquation(equation, assignment)
            IF result = TRUE THEN
                DISPLAY "Solution found: " + assignment
                RETURN assignment
            END IF
        END IF
    END FOR
    
    RETURN "No solution exists"
END ALGORITHM
```

---

## 8. Breadth-First Search (BFS)

**Objective:** Explore graph level-by-level to find shortest path to goal

```
ALGORITHM BreadthFirstSearch(graph, startNode, goalNode)
    IF startNode = goalNode THEN
        RETURN [startNode]
    END IF
    
    queue ← [startNode]
    visited ← {startNode}
    parent ← empty dictionary
    
    WHILE queue is not empty DO
        currentNode ← queue.dequeue()
        
        FOR EACH neighbor IN graph.getNeighbors(currentNode) DO
            IF neighbor NOT IN visited THEN
                visited.add(neighbor)
                parent[neighbor] ← currentNode
                queue.enqueue(neighbor)
                
                IF neighbor = goalNode THEN
                    path ← ReconstructPath(goalNode, parent)
                    RETURN path
                END IF
            END IF
        END FOR
    END WHILE
    
    RETURN "Goal not reachable"
END ALGORITHM
```

---

## 9. Depth-First Search (DFS)

**Objective:** Explore graph by recursively visiting nodes to maximum depth

```
ALGORITHM DepthFirstSearch(graph, startNode, goalNode)
    visited ← empty set
    path ← empty list
    
    FUNCTION DFS(currentNode, goalNode, path)
        visited.add(currentNode)
        path.append(currentNode)
        
        IF currentNode = goalNode THEN
            RETURN path
        END IF
        
        FOR EACH neighbor IN graph.getNeighbors(currentNode) DO
            IF neighbor NOT IN visited THEN
                result ← DFS(neighbor, goalNode, path)
                IF result ≠ NULL THEN
                    RETURN result
                END IF
            END IF
        END FOR
        
        path.removeLast()  // Backtrack
        RETURN NULL
    END FUNCTION
    
    result ← DFS(startNode, goalNode, path)
    RETURN result IF result ≠ NULL ELSE "Goal not found"
END ALGORITHM
```

---

## 10. Uniform Cost Search (UCS)

**Objective:** Find lowest-cost path using priority queue ordered by path cost

```
ALGORITHM UniformCostSearch(graph, startNode, goalNode)
    priorityQueue ← PriorityQueue()
    priorityQueue.insert(startNode, cost=0)
    visited ← empty set
    costMap ← {startNode: 0}
    parent ← empty dictionary
    
    WHILE priorityQueue is not empty DO
        currentNode ← priorityQueue.extractMin()
        
        IF currentNode IN visited THEN
            CONTINUE
        END IF
        
        visited.add(currentNode)
        
        IF currentNode = goalNode THEN
            path ← ReconstructPath(goalNode, parent)
            RETURN (path, costMap[goalNode])
        END IF
        
        FOR EACH (neighbor, edgeCost) IN graph.getNeighbors(currentNode) DO
            newCost ← costMap[currentNode] + edgeCost
            IF neighbor NOT IN visited AND newCost < costMap.get(neighbor, ∞) THEN
                costMap[neighbor] ← newCost
                parent[neighbor] ← currentNode
                priorityQueue.insert(neighbor, newCost)
            END IF
        END FOR
    END WHILE
    
    RETURN "Goal not reachable"
END ALGORITHM
```

---

## 11. A* Search Algorithm

**Objective:** Find optimal path using heuristic-guided evaluation (g + h)

```
ALGORITHM AStarSearch(graph, startNode, goalNode, heuristic)
    openSet ← PriorityQueue()
    closedSet ← empty set
    parent ← empty dictionary
    gScore ← {startNode: 0}
    fScore ← {startNode: heuristic(startNode, goalNode)}
    openSet.insert(startNode, fScore[startNode])
    
    WHILE openSet is not empty DO
        currentNode ← openSet.extractMin()
        
        IF currentNode = goalNode THEN
            path ← ReconstructPath(goalNode, parent)
            RETURN path
        END IF
        
        closedSet.add(currentNode)
        
        FOR EACH neighbor IN graph.getNeighbors(currentNode) DO
            IF neighbor IN closedSet THEN
                CONTINUE
            END IF
            
            newGScore ← gScore[currentNode] + graph.getCost(currentNode, neighbor)
            
            IF neighbor NOT IN gScore OR newGScore < gScore[neighbor] THEN
                parent[neighbor] ← currentNode
                gScore[neighbor] ← newGScore
                fScore[neighbor] ← gScore[neighbor] + heuristic(neighbor, goalNode)
                
                IF neighbor NOT IN openSet THEN
                    openSet.insert(neighbor, fScore[neighbor])
                END IF
            END IF
        END FOR
    END WHILE
    
    RETURN "Goal not found"
END ALGORITHM
```

---

## 12. Greedy Best-First Search (GBFS)

**Objective:** Find path by selecting node with lowest heuristic value

```
ALGORITHM GreedyBestFirstSearch(graph, startNode, goalNode, heuristic)
    priorityQueue ← PriorityQueue()
    visited ← empty set
    parent ← empty dictionary
    priorityQueue.insert(startNode, heuristic(startNode, goalNode))
    
    WHILE priorityQueue is not empty DO
        currentNode ← priorityQueue.extractMin()
        
        IF currentNode IN visited THEN
            CONTINUE
        END IF
        
        visited.add(currentNode)
        
        IF currentNode = goalNode THEN
            path ← ReconstructPath(goalNode, parent)
            RETURN path
        END IF
        
        FOR EACH neighbor IN graph.getNeighbors(currentNode) DO
            IF neighbor NOT IN visited THEN
                heuristicValue ← heuristic(neighbor, goalNode)
                parent[neighbor] ← currentNode
                priorityQueue.insert(neighbor, heuristicValue)
            END IF
        END FOR
    END WHILE
    
    RETURN "Goal not found"
END ALGORITHM
```

---

## 13. Hill Climbing Algorithm

**Objective:** Find local optimum by iteratively moving to best neighboring state

```
ALGORITHM HillClimbing(initialState, objectiveFunction)
    currentState ← initialState
    currentValue ← objectiveFunction(currentState)
    iterationCount ← 0
    maxIterations ← 1000
    
    WHILE iterationCount < maxIterations DO
        neighbors ← GenerateNeighbors(currentState)
        
        IF neighbors is empty THEN
            RETURN currentState  // Local optimum reached
        END IF
        
        bestNeighbor ← FindBestNeighbor(neighbors, objectiveFunction)
        bestValue ← objectiveFunction(bestNeighbor)
        
        IF bestValue > currentValue THEN
            currentState ← bestNeighbor
            currentValue ← bestValue
            iterationCount ← iterationCount + 1
        ELSE
            RETURN currentState  // No improvement found - local maximum
        END IF
    END WHILE
    
    RETURN currentState
END ALGORITHM
```

---

## 14. Fuzzy Set Operations

**Objective:** Perform union, intersection, and complement on fuzzy sets

```
ALGORITHM FuzzySetOperations(fuzzySetA, fuzzySetB)
    unionSet ← empty dictionary
    intersectionSet ← empty dictionary
    complementSetA ← empty dictionary
    
    FOR EACH element IN fuzzySetA.getElements() DO
        membershipA ← fuzzySetA.getMembership(element)
        membershipB ← fuzzySetB.getMembership(element)
        
        // Union: max(μA(x), μB(x))
        unionSet[element] ← MAX(membershipA, membershipB)
        
        // Intersection: min(μA(x), μB(x))
        intersectionSet[element] ← MIN(membershipA, membershipB)
        
        // Complement of A: 1 - μA(x)
        complementSetA[element] ← 1 - membershipA
    END FOR
    
    DISPLAY "Union Set: " + unionSet
    DISPLAY "Intersection Set: " + intersectionSet
    DISPLAY "Complement of A: " + complementSetA
    
    RETURN (unionSet, intersectionSet, complementSetA)
END ALGORITHM
```

---

## 15. Decision Tree Classification

**Objective:** Classify data based on nested conditional logic derived from features

```
ALGORITHM DecisionTreeClassification(inputFeatures)
    weather ← inputFeatures.weather
    temperature ← inputFeatures.temperature
    humidity ← inputFeatures.humidity
    windSpeed ← inputFeatures.windSpeed
    
    IF weather = "Sunny" THEN
        IF humidity > 75 THEN
            RETURN "Don't Play"
        ELSE IF windSpeed > 25 THEN
            RETURN "Don't Play"
        ELSE
            RETURN "Play"
        END IF
    
    ELSE IF weather = "Rainy" THEN
        IF temperature < 5 THEN
            RETURN "Don't Play"
        ELSE IF windSpeed > 40 THEN
            RETURN "Don't Play"
        ELSE
            RETURN "Play"
        END IF
    
    ELSE IF weather = "Cloudy" THEN
        IF temperature > 15 AND temperature < 35 THEN
            RETURN "Play"
        ELSE
            RETURN "Don't Play"
        END IF
    
    ELSE
        RETURN "Unknown condition"
    END IF
END ALGORITHM
```
