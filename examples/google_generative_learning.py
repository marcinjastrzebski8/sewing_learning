"""
Minimal demo of a google-type generative learning experiment. 
Based on "Generative quantum advantage for classical and quantum problems"
TODO: starting hardcoded, expand general
"""

import pennylane as qml
import matplotlib.pyplot as plt
from src.circuit_utils import circuit2d, sew_two_circuits


def target_circuit():
    """
    For now simple entangler
    """
    device = qml.device('default.qubit', wires=range(2))
    @qml.qnode(device)
    def circuit():
        qml.H(0)
        qml.CNOT([0,1])
        return qml.probs()
    drawer = qml.draw_mpl(circuit, show_all_wires = True)
    return circuit(), drawer

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
    probs_target, target_diagram = target_circuit()
    target_diagram().savefig("target_diagram", dpi = 300)

    #baseline train the circuit - results in model

    #divide circuit

    #train each piece
    v1, v2 = target_local_inverse()

    #sewing - results in model
    probs_sewed, sewed_diagram = sew_two_circuits(v1, v2)
    sewed_diagram().savefig("sewed_diagram", dpi=300)
    #compare two trained models

