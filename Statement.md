AI ROCK PAPER SCISSORS

--------------------------------------------------

1. PROJECT OVERVIEW

- Rock-Paper-Scissors game with an AI opponent
- Built using CustomTkinter in Python
- AI adapts to player behavior using pattern recognition and frequency analysis

--------------------------------------------------

2. AI LOGIC

2.1 Pattern Recognition

- Tracks last two user moves
- Predicts next move based on previous patterns
- Stores patterns in `pattern_memory`

2.2 Frequency Analysis

- Counts how often each move is played
- Predicts the most frequent move

2.3 Decision Making

- 80% chance to counter predicted move
- 20% chance to choose a random move

--------------------------------------------------

3. FEATURES

- Interactive GUI using CustomTkinter
- Dark mode interface
- AI opponent
- Real-time result display
- Adaptive gameplay

--------------------------------------------------

4. HOW TO PLAY

1. Run the Python script  
2. Click one option:
   - Rock
   - Paper
   - Scissors  
3. AI makes its move  
4. Result is displayed:
   - You Win
   - AI Wins
   - Draw  

--------------------------------------------------

5. TECHNOLOGIES USED

- Python  
- CustomTkinter  
- Random module  

--------------------------------------------------

6. CODE STRUCTURE

- `user_history` : Stores player moves  
- `pattern_memory` : Stores learned patterns  
- `predict_by_pattern()` : Pattern-based prediction  
- `predict_by_frequency()` : Frequency-based prediction  
- `get_ai_move()` : AI decision logic  
- `get_winner()` : Determines winner  

--------------------------------------------------

7. FUTURE IMPROVEMENTS

- Score tracking  
- Difficulty levels  
- Improved AI models  
- Sound effects  
- Game history  

--------------------------------------------------

8. AUTHOR

- Developed to demonstrate:
  - Pattern recognition  
  - Basic AI concepts  
  - GUI development in Python  

--------------------------------------------------

9. CONCLUSION

- This project demonstrates how simple AI techniques can be used to create an adaptive game  
- It combines logic, probability, and user interaction in an easy-to-understand way  
- The project also highlights the use of GUI development in Python for creating interactive applications  
- It can be further enhanced to build more advanced and intelligent systems
