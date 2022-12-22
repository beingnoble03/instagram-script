from instabot import Bot
from keys import USERNAME, PASSWORD

bot = Bot()
bot.login(username=USERNAME, password=PASSWORD, ask_for_code=True)

# Fetching followers
followers = bot.get_user_followers(USERNAME)
followers_count = len(followers)
followers_username = []

print("----Your Followers----")
count = 0
for follower in followers:
    count = count + 1
    user_info = bot.get_user_info(follower)
    followers_username.append(user_info["username"])
    print(f"[{count}/{followers_count}] ", user_info["username"])

# Fetching following
following_users = bot.get_user_following(USERNAME)
following_count = len(following_users)
following_users_username = []

print("----Your Followings----")
count = 0
for following_user in following_users:
    count = count+1
    user_info = bot.get_user_info(following_user)
    following_users_username.append(user_info["username"])
    print(f"[{count}/{following_count}] ",user_info["username"])

# Comparing followers and followings
users_followed_but_not_following_you = []
for following_user_username in following_users_username:
    if not following_user_username in followers_username:
        users_followed_but_not_following_you.append(following_user_username)

count = 0
print("----Users followed but not following you----")
for user_followed_but_not_following_you in users_followed_but_not_following_you:
    count = count + 1
    print(f"[{count}] " ,user_followed_but_not_following_you)