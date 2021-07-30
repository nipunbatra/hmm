import numpy as np
np.random.seed(10)

# def compute_likelihood(sequence):
	

def forward_algorithm(sequence):

	l = len(sequence)
	ans = np.zeros((l,k))
	for i in range(l):
		for j in range(k):
			if i==0:
				# print (pi[j], B[j, sequence[i]])
				ans[i][j] = pi[j] * B[j, sequence[i]]
			else:
				res = 0
				for q in range(k):
					res+=ans[i-1][q] * A[q][j] * B[j,sequence[i]]
					# res = round(res,4)
				ans[i][j] = res
				
	return ans

def backward_algorithm(sequence):

	l = len(sequence)
	ans = np.ones((l,k))
	i = l-2
	while i>=0:
		for j in range(k):
			res=0
			for q in range(k):
				# print (i,j,k, ans[i+1][q], A[j,q], B[q,sequence[i+1]])
				res+=ans[i+1][q] * A[j,q] * B[q,sequence[i+1]]
				# res = round(res,4)
			ans[i][j]=res
		i-=1
	return ans


def epsilon_algorithm(forward,backward,sequence):

	l = len(sequence)
	ans = np.zeros((l-1, k, k))

	for t in range(l-1):
		for i in range(k):
			for j in range(k):


				res = forward[t][i] * A[i,j] * B[j, sequence[t]] * backward[t][j] 
				# print(t,i,j, forward[t][i] , A[i,j] , B[j, sequence[t+1]] , backward[t+1][j],res )
				# res = round(res,4)
				ans[t][i][j] = res


	ans = ans/np.sum(np.sum(ans,axis=2),axis=1).reshape((ans.shape[0],1,1))

	return ans

def gamma_algorithm(epsilon):

	res = np.zeros((len(epsilon),k))

	# print (res.shape, epsilon.shape)

	for t in range(len(epsilon)):
		for i in range(k):
			res[t][i] = np.sum(epsilon[t][i])

	return res


sequence = np.array([0,1,0,0])

k = 2

# pi = np.random.random((k,1))
pi = np.array([[0.9],[0.1]])
pi  = pi/np.sum(pi,axis=0).reshape((-1,1))

# A  = np.random.random((k,k))
A  = np.array([[0.7,0.3],[0.3,0.7]])
A  = A/np.sum(A,axis=1).reshape((-1,1))

# B = np.random.random((k,k))
B  = np.array([[0.8,0.2],[0.4,0.6]])
B = B/np.sum(B,axis=1).reshape((-1,1))


# print (pi.shape,A.shape,B.shape)


for  epoch in range(2):
	

	forward = forward_algorithm(sequence)

	backward = backward_algorithm(sequence)

	epsilon = epsilon_algorithm(forward,backward,sequence)

	gamma = gamma_algorithm(epsilon)

	epsilon = np.round(epsilon,3)
	gamma =   np.round(gamma,3)

	s="""<div class="em_example" style="display: none">
            <b>Iteration-%s: Expectation Step</b><br><br>

            <table>
              <tbody>
                
                <tr>
                  <td>\\(\\epsilon_{1}(B,B) = %s\\)</td>
                  <td>\\(\\epsilon_{1}(B,F) = %s\\)</td>
                  <td>\\(\\epsilon_{1}(F,B) = %s\\)</td>
                  <td>\\(\\epsilon_{1}(F,F) = %s\\)</td>
                </tr>
                <tr>
                  <td>\\(\\epsilon_{2}(B,B) = %s\\)</td>
                  <td>\\(\\epsilon_{2}(B,F) = %s\\)</td>
                  <td>\\(\\epsilon_{2}(F,B) = %s\\)</td>
                  <td>\\(\\epsilon_{2}(F,F) = %s\\)</td>
                </tr>

                <tr>
                  <td>\\(\\epsilon_{3}(B,B) = %s\\)</td>
                  <td>\\(\\epsilon_{3}(B,F) = %s\\)</td>
                  <td>\\(\\epsilon_{3}(F,B) = %s\\)</td>
                  <td>\\(\\epsilon_{3}(F,F) = %s\\)</td>
                </tr>
              </tbody>
            </table>

            
          <table>
              <tbody>                
                <tr>
                  <td>\\(\\gamma_{1}(B) = %s\\)</td>
                  <td>\\(\\gamma_{2}(B) = %s\\)</td>
                  <td>\\(\\gamma_{3}(B) = %s\\)</td>
                  
                </tr>
                <tr>
                  <td>\\(\\gamma_{1}(F) = %s\\)</td>
                  <td>\\(\\gamma_{2}(F) = %s\\)</td>
                  <td>\\(\\gamma_{3}(F) = %s\\)</td>
                  
                </tr>                
              </tbody>
            </table>
        </div>
        """ %(epoch+1,epsilon[0,0,0],epsilon[0,0,1],epsilon[0,1,0],epsilon[0,1,0], 
          	  epsilon[1,0,0],epsilon[1,0,1],epsilon[1,1,0],epsilon[1,1,0], 
          	  epsilon[2,0,0],epsilon[2,0,1],epsilon[2,1,0],epsilon[2,1,0], 
          	  gamma[0,0],gamma[1,0],gamma[2,0],gamma[0,1],gamma[1,1],gamma[2,1]
          	  )


	# print (epsilon)

	print (s)
	
	if 1:

		for i in range(k):
			pi[i]=gamma[0][i]

		for i in range(k):
			for j in range(k):

				# for t in range(len(epsilon)):

					ans = np.sum(epsilon[:,i,j])/np.sum(epsilon[:,i,:])

					A[i,j] = ans
					# print ('crap')
					# print (epsilon[:,i,j])
					# print (epsilon[:,i,:])
					# print (ans)


		for i in range(k):
			for j in range(2):
				
				mask = np.where(sequence==j,True,False)

				# print (mask.shape, gamma.shape)

				B[i,j] = np.sum(gamma[mask[:-1],i])/np.sum(gamma[:,i])

		pi = np.round(pi,3)
		A = np.round(A,3)
		B = np.round(B,3)
				
	s = """
 <div class="em_example" style="display: none">
            <b>Iteration-%s: Maximization Step</b><br><br>
            \\(
            \\pi = \\begin{bmatrix}
                    %s & %s
                  \\end{bmatrix}

            \\)
            <br><br>
            \\(
            A = \\begin{bmatrix}
                     %s & %s\\\\
                     %s & %s
                  \\end{bmatrix}
            \\)
            <br><br>
            \\(
            \\phi_B = \\begin{bmatrix}
                     %s & %s\\\\
                     \\end{bmatrix}
            \\)            
            <br><br>

            \\(
            \\phi_F = \\begin{bmatrix}
                     %s & %s\\\\
                     \\end{bmatrix}
            \\)                      
        </div>
	"""%(epoch+1,pi[0][0],pi[1][0],A[0,0],A[0,1],A[1,0],A[1,1],B[0,0],B[0,1],B[1,0],B[1,1])

	print (s)


	# print (epoch,np.sum(forward[-2]))
	# print ('Epoch :',epoch)
	# print(A)
	# print (B)
	# print (pi)
	# print (epsilon.shape)
	# print (np.sum(forward[-1]))

# print (B)