import time
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, BasicAer


def randomNum():
    num = ''
    max = 5
    for i in range(max):
        q = QuantumRegister(1)
        c = ClassicalRegister(1)
        qc = QuantumCircuit(q, c)
        backend = BasicAer.get_backend('qasm_simulator')

        qc.h(q[0])
        qc.measure(q, c)
        result = execute(qc, backend, shots=10).result()
        count = result.get_counts(qc)
        k = count.keys()
        if '0' in count.keys():
            num += '0'
        else:
            num += '1'

    print(num)
    print(int(num, 2))

def hitman_game():
    print(" Welcome to the what hitman move game ????")
    hitman = input("Enter your hitman qubit number (1-5): ")
    while int(hitman) < 1 or int(hitman) > 5:
        print('Not a valid input')
        hitman = input("Enter your hitman qubit number (1-5): ")
    #hitman = 2
    hitman = int(hitman) - 1

    you = input('Enter your qubit number (1-5 but not same as hitman): ')
    while int(you) - 1 == hitman or int(you) < 0 or int(you) > 5:
        print('Not a valid input')
        you = input('Enter your qubit number (1-5 but not same as hitman): ')
    you = int(you) - 1
    print("There is a hitman trying to shoot at you")
    print("You have a choice to move to the left or to the right")
    player = input("Your move [L]eft or [R]ight : ")
    #player = 'L'

    # prepare qubits
    q = QuantumRegister(5)
    c = ClassicalRegister(5)  # using classical bits to measure the outcome
    qc = QuantumCircuit(q,c)
    backend = BasicAer.get_backend('qasm_simulator')

    qc.h(q[you])
    if player == 'L':
      qc.s(q[hitman])
    else:
      qc.y(q[you])
    qc.h(q[hitman])
    qc.s(q[you])
    qc.cx(q[hitman], q[you]) #entagglement
    qc.h(q[you])
    qc.measure(q,c)
    result = execute(qc, backend, shots=1000).result()
    count = result.get_counts(qc)
    outcome = max(count, key=count.get)
    print("The hitman is shooting...")
    time.sleep(1)

    if int(outcome[4 - you]) != int(outcome[4 - hitman]):
        print('The hitman missed. You survive')
    else:
        print('Oops you died...')

hitman_game()