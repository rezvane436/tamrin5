def q1(s, i):

	if (i == len(s)):
		print("Yes");
		return;
	
	
	if (s[i] == 'a'):
		q1(s, i + 1);
	else:
		q2(s, i + 1);

def q2(s, i):
	
	
	if (i == len(s)):
		print("No");
		return;
	
	if (s[i] == 'a'):
		q1(s, i + 1);
	else:
		q2(s, i + 1);

def q3(s, i):
	
	if (i == len(s)):
		print("Yes");
		return;
	

	if (s[i] == 'a'):
		q4(s, i + 1);
	else:
		q3(s, i + 1);


def q4(s, i):
	
	if (i == s.length()):
		print("No");
		return;
	
	
	if (s[i] == 'a'):
		q4(s, i + 1);
	else:
		q3(s, i + 1);


def q0(s, i):

	if (i == len(s)):
		print("No");
		return;
	
	
	if (s[i] == 'a'):
		q1(s, i + 1);
	else:
		q3(s, i + 1);


if __name__ == '__main__':
	s = "abbaabb";


	q0(s, 0);
	
