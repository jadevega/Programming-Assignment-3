def lcs():
    import sys
    lines = [line.strip() for line in sys.stdin if line.strip()]
    line_index = 0;
    K = int(lines[0]);
    line_index += 1;

    vals = {}
    for _ in range (K):
        char, val = lines[line_index].split()
        line_index+=1;

    A = lines[line_index]
    line_index+=1
    B = lines[line_index]
    line_index +=1

    n = len(A)
    m = len(B)

    dp_table = [[0] * (m + 1) for _ in range (n + 1)]

    for i in range(1, n+ 1):
        for j in range(1, m+ 1):
            if (A[i-1] == B[i-1]):
                take = vals[A[i-1]] + dp_table[i-1][j-1] #if match take
                skip_A = dp_table[i-1][j] #up
                skip_B = dp_table[i][j-1] #left
                dp_table[i][j] = max(take, skip_A, skip_B) #take max value
            else:
                dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1]) #either skip from A, skip from B, up or left



