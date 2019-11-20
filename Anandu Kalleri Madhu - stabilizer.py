#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import *
import numpy as np
from qiskit.providers.aer.extensions import *


# In[ ]:





# In[2]:


stabs=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])


# In[3]:


class Initialize_Stabilizer(Instruction):
    def __init__(self, stabs):
        num_qubits = int (stabs.shape[1]/2)
        
        #stabs.append(destabs)
        
        
        
        stab_string=[]
        for i in range(stabs.shape[0]):
            temp=''
            #convert to string
            for j in range(0,num_qubits): 
                qi=[stabs[i,j],stabs[i,j+num_qubits]]
                if qi==[0,0]:
                    temp=temp+'I'
                elif qi==[0,1]:
                    temp= temp+'Z'
                elif qi==[1,0]:
                    temp=temp+'X'
                else:
                    temp=temp+'Y'
    
            stab_string.append(temp)
        
        
        param = np.array(stab_string)    # np.array is a hack to make non-float params work
        super().__init__("initialize_stabilizer", num_qubits, 0, [param])


# In[ ]:


instr=Initialize_Stabilizer(stabs)
qc=QuantumCircuit(2)
#qc.h(0)
qc.append(instr, [0, 1])
backend_options = {"method": "stabilizer"}

job = execute(qc, Aer.get_backend('qasm_simulator'), basis_gates=['initialize_stabilizer'],
              backend_options=backend_options)


# In[ ]:


job.result().to_dict()


# In[7]:


assemble(qc).experiments[0].instructions


# In[ ]:


#std::vector<std::vector<std::string>> tmp = js["params"]
#op.string_params = tmp[0]

