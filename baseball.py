import random;

def getRandomRange(seedValue):
	return random.uniform(seedValue/1.5, seedValue);

def checkHomerun(control, speed, contact, power):
	control = getRandomRange(control);
	speed = getRandomRange(speed);
	contact = getRandomRange(contact);
	power = getRandomRange(power);

	msgStr = "control: %f speed: %f, contact: %f, power: %f" % (control, speed, contact, power);
	if(control < contact):
		if(speed < power):
			return { "result": "Homerun", "msg": msgStr };
		return { "result": "Hit", "msg": msgStr };
	return { "result": "Miss", "msg": msgStr };

def playball(pitcher, batter):
	checkResult = checkHomerun(pitcher.control, pitcher.speed, batter.contact, batter.power);
	condition = checkResult["result"];
	msgStr = checkResult["msg"]

	if (condition == "Homerun"):
		batter.addHomerunCount();
	elif (condition == "Hit"):
		batter.addHitCount();

	return msgStr + ' 판정: ' + condition + '\n';

def divider():
	return("------------------------------------------------\n");

class Player:
	def __init__(self, name, team):
		self.name = name;
		self.team = team;

class Pitcher(Player):
	def __init__(self, name, team, control, speed):
		super(Pitcher, self).__init__(name, team);
		self.control = control;
		self.speed = speed;

	def pitching(self):
		control = getRandomRange(self.control);
		speed = getRandomRange(self.speed);
		print(control, speed);

class Batter(Player):
	def __init__(self, name, team, contact, power):
		super(Batter, self).__init__(name, team);
		self.homerunCount = 0;
		self.hitCount = 0;
		self.contact = contact;
		self.power = power;

	def batting(self):
		contact = getRandomRange(self.contact);
		power = getRandomRange(self.power);

	def addHomerunCount(self):
		self.addHitCount();
		self.homerunCount += 1;

	def addHitCount(self):
		self.hitCount += 1;
		
	def printHomerunCount(self):
		msgStr = ("%s 타자는 %d 번 안타와 %d 개의 홈런을 쳤습니다." % (self.name, self.hitCount, self.homerunCount));
		print(msgStr);
		return msgStr+'\n';

		
# Player Data Set
playerList = [
	{
		'name': '김태균',
		'team': '한화',
		'type': 'Pitcher',
		'speed': 140,
		'control': 95
	},
	{
		'name': '류현진',
		'team': '한화',
		'type': 'Batter',
		'contact': 160,
		'power': 95
	},
	{
		'name': '이대호',
		'team': '롯데',
		'type': 'Batter',
		'contact': 85,
		'power': 190
	}
];

pitcherList = [];
batterList = [];

for player in playerList:
	if (player["type"] == "Pitcher"):
		pitcherList.append(Pitcher(player["name"], player["team"], player["speed"], player["control"]));
	elif (player):
		batterList.append(Batter(player["name"], player["team"], player["contact"], player["power"]));

file = open("result.txt", "w", encoding="UTF-8")
for pitcher in pitcherList:
	for batter in batterList:
		msgStr = ("투수: %s\t소속: %s\n타자: %s\t소속: %s\n" % (pitcher.name, pitcher.team, batter.name, batter.team));
		print(msgStr);
		file.writelines(msgStr);
		file.writelines(divider());
		for i in range(0, 10):
			file.writelines(str(i+1) + '.\t' + playball(pitcher, batter));
		file.writelines('\n'+batter.printHomerunCount()+'\n');
file.close();
