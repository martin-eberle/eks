# Python EKS Library

Based on <https://github.com/olisim/eks>; modified to python3 compatibility.

Works with Euchner EKS Ethernet TCP/IP electronic key adapter (see <https://www.euchner.de/de-de/produkte/transpondercodierte-schluesselsysteme/electronic-key-system-eks2/>). Manuals from Euchner can be found here: <https://assets2.euchner.de/Downloads/Betriebsanleitung/de/MAN_Handbuch-EKS-und-EKS-FSA-mit-Ethernet-TCP…_DE_2547185.pdf>

## Usage

See example code in demo.py. Hostname needs to be set (default 192.168.1.1), port is 2444 by default.
You need to implement a callback class to receive notitications from the eks library.
