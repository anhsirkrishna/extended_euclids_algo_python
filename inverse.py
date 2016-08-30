import argparse

def GCD(a,b):
	if(b == 0):
		return a
	
	return GCD(b,a%b)
	
def ext_eu_inverse(b,m):
	if(b<0):
		b = b % m
	
	A = [1,0,m]
	B = [0,1,b]
	T = [0,0,0]

	while(1):
		if(B[2] == 0):
			return null
			#print("There is no inverse")
			break
		
		if(B[2] == 1):
			bi = B[1]%m
			return bi
			#print("Inverse of ",b," w.r.t ",m," is ",bi)
			break
			
		Q = int(A[2]/B[2])
		#print("Q = ",Q)
		
		for i in range(3):
			T[i] = A[i] - (Q * B[i])
			A[i] = B[i]
			B[i] = T[i]
		
		#print("T = ",T)
		#print("________________________")

def main():
	parser =  argparse.ArgumentParser()
	parser.add_argument("b", help="Enter b, the number to find the inverse of")
	parser.add_argument("m", help="Enter m, the number relative to the inverse")
	args = parser.parse_args()

	b = int(args.b)
	m = int(args.m)
	
	print("Inverse of ",b," with respect to ",m," is ",ext_eu_inverse(b,m))

if(__name__=="__main__"):
	main()
	