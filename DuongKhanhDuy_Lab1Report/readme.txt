Python Version checked: 3.9+

Command format: python pacman.py -l {layout} -p {agent name} -a fn={search function} -z {zoom factor}
Ex: python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

The Agents.py file contain RandomAgent, BetterRandomAgent, and ReflexAgent.

The myLayout.lay in layout folder is a customized layout. You can make new environment for Pacman by creating new layout in layout folder.


Example Command:
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs 

python pacman.py -l bigMaze -p SearchAgent -a fn=dfs -z .5
python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs 

python pacman.py -l bigMaze -p SearchAgent -a fn=ucs -z .5
python pacman.py -l tinyMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs 