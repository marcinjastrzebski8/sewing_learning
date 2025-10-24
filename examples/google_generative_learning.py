"""
Minimal demo of a google-type generative learning experiment. 
Based on "Generative quantum advantage for classical and quantum problems"
TODO: starting hardcoded, expand general
"""

import pennylane as qml
from src.circuit_utils import circuit2d, sew_two_circuits


def target_circuit():
    """
    For now simple entangler
    """
    device = []
    @qml.qnode(device)
    def target_circuit():
        qml.H(0)
        qml.CNOT([0,1])
        return qml.probs()
    return target_circuit()

def target_local_inverse():
    """
    For now just random one-qubit circuits.
    DOES NOT REPRODUCE TARGET ATM.
    """
    def v1(qubit):
        """
        first circuit as oplist
        """
        op_list = []
        op_list.append(qml.X(wires = qubit))
        return op_list

    def v2(qubit):
        """
        first circuit as oplist
        """
        op_list = []
        op_list.append(qml.Y(wires = qubit))
        return op_list
    return v1, v2



if __name__ == '__main__':

    #define shallow circuit
    probs_target = target_circuit()

    #baseline train the circuit - results in model

    #divide circuit

    #train each piece
    v1, v2 = target_local_inverse()

    #sewing - results in model
    probs_sewed = sew_two_circuits(v1, v2)

    #compare two trained models

