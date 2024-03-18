queue = []
op = input()
while(op != 'END'):
  if ',' in op:
    L=[]
    L = L + op.split(',')
    if( L[0] == 'JOIN'):
      queue.append(L[1])    
    elif ( L[0] == 'MOVE'):
      if( L[2] == 'HEAD'):
        queue.remove(L[1])
        queue.insert(0, L[1])
      elif ( L[2] == 'TAIL'):
        queue.remove(L[1])
        queue.append(L[1])
  elif ( op == 'PRINT'):
    print(','.join(map(str, queue)))
  elif ( op == 'LEAVE'):
    queue.pop(0)
  op = input()