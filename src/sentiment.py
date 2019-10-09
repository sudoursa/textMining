import sentiment_run as s

# pos = "This movie was awesome! The acting was great, plot was wonderful, and there were pythons...so yea!"
# neg = "This movie was utter junk. There were absolutely 0 pythons. I don't see what the point was at all. Horrible movie, 0/10"

pos = input("Please type a short POSITIVE review of something: ")
neg = input("Please type a short NEGATIVE review of something: ")

print("Positive Review: \n\t",pos,"\n\t\t",s.sentiment(pos))
print("Negative Review: \n\t",neg,"\n\t\t",s.sentiment(neg))
