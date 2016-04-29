def transitionState(command, state):
	if command.name == "clicked":
		if state.name == "closed":
			return {"name": "opening"}
		elif state.name == "opened":
			return {"name": "closing"}
		elif state.name == "opening":
			return {"name": "stoppedopening"}
		elif state.name == "closing":
			return {"name": "stoppedclosing"}
		elif state.name == "stoppedopening":
			return {"name": "closing"}
		elif state.name == "stoppedclosing":
			return {"name": "opening"}
		# elif state.name == "emergencyopening":
		# 	return {name: "opening"
		# elif state.name == "openblocked":
		# 	return {name: 
	elif command.name == "complete":
		if state.name == "opening":
			return {"name": "opened"}
		elif state.name == "closing":
			return {"name": "closed"}
		else: 
			return {"name": state}


commandlist = [{"name":"clicked"}, {"name":"complete"}, {"name":"clicked"}, {"name":"clicked"}, {"name":"clicked"}, {"name":"clicked"}, {"name":"clicked"}, {"name":"complete"}]
previousState = {"name":"closed"}
for command in commandlist:
	newState = transitionState(command, previousState)
	print(newState)
	previousState = newState




# # garagedoorcommands
# buttonclicked
# cyclecomplete

# garagedoorstates
# opening
# closing
# stoppedopening
# stoppedclosing
# opened
# closed