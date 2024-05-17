import instaloader
import os

def InstagramBot():
    bot = instaloader.Instaloader()

    profile = instaloader.Profile.from_username(bot.context, 'name of the public account')

    # posts = profile.get_posts()
    # for index, post in enumerate(posts, 1):
    #     bot.download_post(post, target=f"{profile.username}_{index}")
    #print('profile: ',profile, ' followers:', profile.followers)

    posts = profile.get_posts() # Get the user's feed

    #print(posts)
    for post in posts:
        print(f"https://www.instagram.com/p/{post.shortcode}") # Print each post's url
        bot.download_post(post,target=f"{post.shortcode}")
        #print(post)
        break

InstagramBot()
