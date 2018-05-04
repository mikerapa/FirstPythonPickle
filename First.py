import pickle

print("starting...")

# pickle a string
a = "mike was here"
pickle.dump(a, open("first.pickle", "wb"))
returnedString = pickle.load(open("first.pickle", "rb"))
print("returned : " + returnedString )

print("Ending")
