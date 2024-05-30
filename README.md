<h1>Tic Tac Toe Game</h1>
<p>This repository contains two versions of the classic Tic Tac Toe game: a 2-player game and a 1-player game with an optimized AI using the minimax algorithm.</p>

<h2>Files</h2>
<ul>
    <li><code>tictactoe_2player.py</code>: Play against another human.</li>
    <li><code>tictactoe_1player.py</code>: Play against an AI opponent.</li>
</ul>

<h2>Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li>os module (standard in Python)</li>
</ul>

<h2>How to Run</h2>
<ol>
    <li>Clone this repository or download the files.</li>
    <li>Navigate to the directory containing the files.</li>
    <li>Run the desired game file:</li>
</ol>
<pre><code>python tictactoe_2player.py</code></pre>
<p>or</p>
<pre><code>python tictactoe_1player.py</code></pre>

<h2>Game Instructions</h2>

<h3>2-Player Game (<code>tictactoe_2player.py</code>)</h3>
<ul>
    <li>Players take turns to choose a spot on the board.</li>
    <li>Enter the number corresponding to the desired spot or press <code>q</code> to quit.</li>
    <li>The game ends when one player wins or there is a draw.</li>
</ul>

<h3>1-Player Game (<code>tictactoe_1player.py</code>)</h3>
<ul>
    <li>Player 1 (human) goes first, then the AI takes its turn.</li>
    <li>Enter the number corresponding to the desired spot or press <code>q</code> to quit.</li>
    <li>The AI uses the minimax algorithm to choose the optimal move.</li>
    <li>The game ends when one player wins or there is a draw.</li>
</ul>

<h2>Minimax Algorithm</h2>
<p>The 1-player game uses the minimax algorithm to determine the best move for the AI. The algorithm works as follows:</p>
<ul>
    <li><strong>Maximizing Player (AI)</strong>: The AI aims to maximize its score by choosing the move that leads to the highest score.</li>
    <li><strong>Minimizing Player (Human)</strong>: The human player aims to minimize the AI's score by choosing the move that leads to the lowest score for the AI.</li>
    <li>The algorithm recursively evaluates all possible moves and selects the optimal one.</li>
</ul>

<h2>Features</h2>
<ul>
    <li>2-Player Game: Simple turn-based gameplay for two human players.</li>
    <li>1-Player Game: Compete against an AI that uses the minimax algorithm for optimal moves.</li>
    <li>Board Drawing: Visual representation of the board after each move.</li>
    <li>Win and Draw Detection: Automatically checks for win conditions and draws.</li>
</ul>

<h2>License</h2>
<p>This project is open source and available under the MIT License.</p>

<p>Enjoy playing Tic Tac Toe!</p>

