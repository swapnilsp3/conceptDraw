graph.add_edge('immediateconsequences','actions',label='affects',horiz=False)
graph.add_edge('evaluationofothers','actions',label='affects',horiz=False)
graph.add_edge('habit','actions',label='affects',horiz=False)
graph.add_edge('actions','attitude',label='express',horiz=False)
graph.add_edge('beliefs','attitude',label='express',horiz=False)
graph.add_edge('emotions','attitude',label='express',horiz=False)
graph.add_edge('attitude','referencegroups',label='influencedby',horiz=False)
graph.add_edge('attitude','directcontact',label='formedby',horiz=False)
graph.add_edge('attitude','chancecondidtioning',label='formedby',horiz=False)
graph.add_edge('attitude','interaction',label='formedby',horiz=False)
graph.add_edge('attitude','media',label='formedby',horiz=False)
