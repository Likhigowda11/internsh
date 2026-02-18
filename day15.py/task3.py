#The Bayesian Filter (Conditional Probability & Bayes’ Theorem)
P_spam = 0.1
P_ham = 0.9

P_free_given_spam = 0.9
P_free_given_ham = 0.05

P_free = (P_free_given_spam * P_spam) + (P_free_given_ham * P_ham)
print(f"Total probability of 'Free' appearing in any email: {P_free:.4f}")

P_spam_given_free = (P_free_given_spam * P_spam) / P_free
print(f"Probability that an email is Spam given it contains 'Free': {P_spam_given_free:.4f}")