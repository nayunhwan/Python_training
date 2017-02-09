import random;

def getRandomRange(seedValue):
	return random.uniform(seedValue/1.5, seedValue);

def checkHomerun(control, speed, contact, power):
	return (control < contact && speed < power);

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
		self.contact = contact;
		self.power = power;

	def batting():
		contact = getRandomRange(self.contact);
		power = getRandomRange(self.power);
		
		
playerList = [{
	'name': '김태균',
	'team': '한화',
	'speed': 140,
	'control': 95,
	'type': 'Pitcher'
}]
na = Pitcher("nayunhwan", "hyu", 100, 100);
na.pitching();
