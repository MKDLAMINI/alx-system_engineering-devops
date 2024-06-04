#!/usr/bin/python3
"""Contains count_words function"""
import requests


def count_words(subreddit, word_list, after="", word_count={}):
    """Prints a sorted count of given keywords in hot posts of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "limit": 100
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code != 200:
            return

        results = response.json().get("data")
        if results is None:
            return

        after = results.get("after")
        posts = results.get("children")

        for post in posts:
            title = post.get("data").get("title").lower()
            for word in word_list:
                lower_word = word.lower()
                word_count[lower_word] = word_count.get(lower_word, 0) + title.split().count(lower_word)

        if after is not None:
            return count_words(subreddit, word_list, after, word_count)
        
        if not word_count:
            return

        sorted_words = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))

        for word, count in sorted_words:
            if count > 0:
                print(f"{word}: {count}")

    except requests.RequestException:
        return


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        count_words(subreddit, word_list)
    else:
        print("Please provide a subreddit name and a list of keywords.")

