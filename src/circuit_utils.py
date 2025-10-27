"""
Useful pieces of code related to the circuits used in the google generative experiment
"""
import numpy as np
import pennylane as qml
from typing import List

def circuit2d(graph, input_bitstring: List, angles):
    """
    Wrapper around qnode for circuit 2d.
    NOTE: just a sketch for now, needs developing
    """
    device = [] #TODO
    qubits = [] #TODO
    @qml.qnode(device)
    def circuit2d(graph, input_bitstring):
        #initialise in all-0

        #layer of hadamards
        for i, bit in enumerate(input_bitstring):
            if bit:
                qml.H(i)
        #layer of RZs
        for i, angle in enumerate(angles):
            qml.RZ(angle, wires = i)
        #layer of CZs - based on graph
        for connection in graph:
            #TODO: figure out graph argtype
            qml.CZ(connection[0], connection[1])
        #TODO: think about best measurement type, for now i think probs works
        return qml.probs(wires = qubits)
    return circuit2d(graph, input_bitstring)

def circuit1plus1d():
    """
    Wrapper around qnode for cicuit 1+1d.
    NOTE: sketch, needs developing.
    """
    pass
    
def heisenberg_learning():
    """
    TODO: implement simple version (hardcode a lot) of S.2.5.
    It's a least square optimisation of a Pauli decomposition of a heisenberg-evolved Pauli meas.
    """
    dataset = make_U_evolution_dataset()
    pass

def make_U_evolution_dataset():
    """
    TODO: this to implement a simple instance of S.1.1. dataset for some simple U.
    Hard code a lot for now.
    """
    pass

def sew_two_circuits(V1,V2):
    """
    implements two-qubit local sewing on 1-qubit circuits V1, V2
    The circuits are local inversions of target U on qubits 1 and 2.
    SUPER HARDCODED FOR NOW
    V1, V2 - functions returning a list of qml operations with one argument - qubit to act on
    """
    qubits = np.arange(4)
    device = qml.device('default.qubit', wires=qubits)
    
    #divide the two register blocks for clarity
    reg1 = qubits[:2]
    reg2 = qubits[2:]
    @qml.qnode(device)
    def sewed_circuit():

        #order of implementation of locals should not matter
        V2(reg1[1]) #this should be an adjoint
        qml.SWAP([reg1[1],reg2[1]])
        V2(reg1[1])

        V1(reg1[0]) #thi should be an adjoint
        qml.SWAP([reg1[0], reg2[0]])
        V1(reg1[0])

        qml.SWAP([reg1[1],reg2[1]])
        qml.SWAP([reg1[0], reg2[0]])
        return qml.probs(reg1)
    drawer = qml.draw_mpl(sewed_circuit, show_all_wires = True)
    return sewed_circuit(), drawer





