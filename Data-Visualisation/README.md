# DAN-Data Visualisation
**Summary:**
<br>
This Data Visualization helps us analyze the goal-scoring ratio per game for football (soccer) players across the Spanish La Liga. It was desiged to show that other players are either getting closer to the performances as Christiano Ronaldo and Lionel Messi. 
<br>
<br>
**Design:**
<br>
The dataset being used in this project was collected via Wikipedia and it is a pretty straightforward dataset with 7 fields and 36 rows. I’ve collected for six different players from the years 2010 to 2015.  Since I’m new to the data visualization and javascript domain, I tried having the whole experience of collecting the data and try telling the story of goal scoring, assists to goals across seasons for the top football players in the Spanish league. 
I chose the Spanish league because they have witnessed the best footballers in the world and won the Ballon D'or every time since 2010, the year from the trophies' introduction. Since I wanted to show the players’ performance across the years, I chose line chart to display the trends in time. The feature that we are trying to compare is that of goals scored per season by the top goal scorers. The number of goals in a season is defined by the number of goals scored in that season to the total number of appearances in that season. Another feature we can used for comparision is the assists per season. These statistics help us understand that other players are coming closer to the best players in the world.
<br>
I used Dimple.js and D3.js to create my visualizations. The first chart I came up is drawn below and this chart was created with the expectation that the user understands the idea behind the line chart being displayed. Below is the image of index_trial1.html, which shows the basic outlay of the chart.
<br>
![alt tag](https://raw.githubusercontent.com/baidrahul9/DAN-Data-Visualisation/master/images/Initial.png)
<br>
<br>
**Feedback #1:**
<br>
Although the scatterplot dots show the name of the players, year and goals per game, it would be better to show the name of the player corresponding to the color of the line.
<br>
*Implementation:*
I added legend to the chart and made it more interactive and precise.
<br>
<br>
**Feedback #2:**
<br>
The chart seems pretty ‘bland’ and lacks interaction. It could be more animated and interactive to put forth the idea of comparison between players.
<br>
*Implementation:*
I added animation to the chart, which helps select 0-all players at a time for comparison and I also added more information in the tool-tip box that when a scatterplot is hovered on, it shows all the details from the data (csv) file.
<br>
<br>
**Feedback #3:**
<br>
The title doesn’t match and the interaction isn’t there.
<br>
<br>
**Feedback #4:**
<br>
The visualization isn't really explanatory yet.
<br>
<br>
*Implementation:*
Added a more story based approach to the project giving it a sense of direction.
<br>
<br>
**Feedback #5:**
<br>
Currently it's not an explanatory visualization.
<br>
*Implementation:*
I came to realize that I wasn't maybe asking the right questions from the visualization. I changed my question to the problem and put it as 'Have the players in the La-Liga come closer in performance to the likes of Ronaldo and Messi?'
<br>
<br>
**Feedback #6:**
<br>
![alt tag](https://raw.githubusercontent.com/baidrahul9/DAN-Data-Visualisation/master/images/Goals_Bar_Plot.png)<br/>
This doesn't convey the message quite clearly. The task is to figure out how to make sure that this story is getting across to the chart reader.
<br>
*Implementation:*
I changed my bar plots to line charts and added mouseover events to make it stand out. I also added description to the charts and the page so that it is more readable and comprehendable. 
<br/>
**Conclusion from the Plot:**
<br>
Since this was my first D3 and Dimple project, I believe I have added enough interaction, kept the comparison open ended (more like the Martini glass concept). The users can now compare the players that they want and have better understanding of my story. Below are some sample charts from the visalization:
<br>
Assists Distribution:
<br>
![alt tag](https://raw.githubusercontent.com/baidrahul9/DAN-Data-Visualisation/master/images/Assists_Per_Game.png)
<br>
Final Line Chart
<br>
![alt tag](https://raw.githubusercontent.com/baidrahul9/DAN-Data-Visualisation/master/images/Line_chart.png)
<br>
As we can see, it was always either Christiano or Lionel Messi that had the best goals per game ratio across all season but 2015-16 during which Luis Suarez scored more goals and had more assists than any other top player in the League. We can see the difference in goals per season coming close as the years progress. I would not call it a dip in performance from the 2 best footballers in the world but other players just performing better.<br>
The first plot shows the goals distribution throughtout the years. It is evident that the majority of goals scored in 2010-13 are either Ronaldo or Messi. But things start to get interesting with other players, who in their early career did not perform as well as they are performing now. The second plot displays the assists distribution each season and we can see that the trends are changing from the early years to present time. It may not be clear to the eye to make a conclusion from the earlier line chart plots of goals and assists and that is why my final chart is the line chart with scatterplots which clearly shows that the differene in goals per season has come down significantly and in fact Luis Suarez has surpassed everyone on goal scoring in 2015. Since Ronaldo and Messi have both been very consistent throughout the years according to the line chart, their peers have only grown better thus decreasing the 'variance' in the latter years. Now, it is up to the user to decide whether age or other issues are causing this closeness of plots and I would want to leave the question open-ended here.
<br>
<br>
**Resources:**
<br>
1. Dimple.js
<br>2. D3.js
<br>3. Udacity Nanodegree
<br>
<br>
**Files:**
<br>
1. index.html
<br>2. Football_Data.csv
<br>3. index_trial1.html
<br>4. /images/


