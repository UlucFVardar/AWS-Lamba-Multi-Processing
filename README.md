# Our Dream
###### First of all, let us explain where we will implement this concept.
###### We are setting up this architecture to capture all player information from  [Transfermarkt](https://www.transfermarkt.com.tr/)
---
###### This website contains all the information we need under different pages. We have to regularly navigate through these pages to get the information of teams of all leagues in these leagues and players playing on these teams.

 ![architecture](https://raw.githubusercontent.com/UlucFVardar/AWS-Lamba-Multi-Processing/master/SS/AWS%20Lambda%20Multi%20%202.png)

### As you can see, there is a lambda architecture with 4 Layers.
<details open>
<summary open>Layer Documentation </summary>
Let's start with the 1st layer.

---
###### Lambda in layer 1 will be triggered with AWS CloudWach and will parse the page where all leagues are listed on the site and find the names of the leagues and the URL's with the information of those leagues. Names of leaguw will place on the AWS RDS Database and with using the AWS API GateWay to trigger. for every league a sublayer lambda will invoked with the parameter of *league_id and league_url.*
--
###### Lambda functions in layer 2 will be run by different lambda parameters from a top layer. This lambda will be tasked to parse the information within the league url and find names and URLs of all teams in that league. Team names will be inserted into DB. Than for every team_url a subLayer Lambda will be invoked with the paramaters of team_url,team_id
--
###### Lambda functions in layer 3 work by taking parameters of the team url and team_id. The task of these functions is to find URLs for all players playing on that team. After insering Player name to DB, player_id and player_url are placed in a lower layer.
--
###### Lambda functions in layer 4 work by taking parameters of the player_url and player_id. The task of these lambdas are to update players info from the DB.
</details>
---
# How to invoke A Lambda From another Lambda 
<details open>
<summary open>API Documentation </summary>
</details>


