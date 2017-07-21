import paramiko, time, sudoku_class

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("ringzer0team.com", username="sudoku",password="dg43zz6R0E", port=12643)
print("[+] Connected!")
shell = ssh.invoke_shell()

def printPuzzle( puzzle ):
	for row in puzzle:
		print( row )

while not shell.recv_ready():
    time.sleep(0.6)

server_answer = shell.recv(4094)
resp = server_answer.decode("utf-8")
print("[+] %s" % resp)
input_sudoku = resp[resp.find("The sudoku challenge")+len("The sudoku challenge"):resp.find("Solve this sudoku in less than 10")]
input_sudoku = input_sudoku.replace("+","").replace("\r", "").replace("+", "").replace("   ", "0").replace("-", "").replace("|", "").replace(" ", "").replace("\n\n", "\n").strip()

strings = input_sudoku.split("\n")
null_positions = []
puzzle = []

for each_string in range(9):
	string = []
	for each_number in range(9):
		string.append(int(strings[each_string][each_number]))
		if int(strings[each_string][each_number]) == 0:
			null_positions.append(str(each_string) + ";" + str(each_number))
	puzzle.append(string)

solution = sudoku_class.SudokuSolver.solve(puzzle)
answ = ""

for each_string in range(9):
	for each_number in range(9):
		if (each_number == 8) and (each_string == 8):
			answ += str(solution[each_string][each_number])
		else:
			answ += str(solution[each_string][each_number]) + ","

shell.send(answ + "\r\n")
printPuzzle(solution)

while not shell.recv_ready():
	time.sleep(0.6)
server_answer = shell.recv(4094)

print("\n[+] %s" % server_answer.decode("utf-8").replace("\r\n", " "))
ssh.close()