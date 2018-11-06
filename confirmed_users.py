unConfirmed_users = ['alice','brian','candace']
confirmed_users = []
while unConfirmed_users:
    user = unConfirmed_users.pop()
    print("Verify user:"+user.title())
    confirmed_users.append(user)
print("Unconfirmed_user:"+str(unConfirmed_users))

print("\nConfirme_user:")
for user in confirmed_users:
    print(user.title())

