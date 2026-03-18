from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a circuit with 4 qubits and 4 classical bits
qc = QuantumCircuit(4, 4)

# The Hadamard gate is a 2x2 matrix that takes a qubit in definite 0,
# applies matrix multiplication, and produces equal amplitudes of 0.707
# in both slots putting the qubit into superposition. The -1 in the matrix
# encodes phase, which enables interference. It cancels out wrong answers and reinforces correct ones.

# Apply a Hadamard gate to each qubit
# This is what pushes the qubit(s) into superposition
qc.h([0, 1, 2, 3])

# The Hadamard gate pushes a qubit into superposition, producing equal amplitudes of 0.707 in both slots.
# You then apply the Born rule — squaring the amplitudes — to get the probabilities, which are 0.5 or 50% for each outcome.

# Measure all qubits into the classical bits
# To measure we use the Born rule which says that a probability of
# a particular outcome equals the square of its amplitude.
# So in this case 0.707squared=0.5 (50% chance)
# Born Rule - governs what happens when you measure a qubit.
qc.measure([0, 1, 2, 3], [0, 1, 2, 3])

# Run on the local simulator
simulator = AerSimulator()
job = simulator.run(qc, shots=1)
result = job.result()
counts = result.get_counts()

# Get the random bits
random_bits = list(counts.keys())[0]
random_number = int(random_bits, 2)

print(f"Random bits: {random_bits}")
print(f"Random number: {random_number} (0-15)")

# # The Tensor product takes two seperate 2 slot qubits and combines them into one 4 slot vector.
# We need that because 2 qubits have 4 possible outcomes. When the resulting vector cannot be refactored
# back to it's original state the result is entanglement.
