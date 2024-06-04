#!/usr/bin/python3
"""Contains recurse function"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code != 200:
            return None

        results = response.json().get("data")
        if results is None:
            return None

        after = results.get("after")
        count += results.get("dist")
        for c in results.get("children"):
            hot_list.append(c.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except ValueError:
        print("Failed to decode JSON response")
        return None


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result:
            for title in result:
                print(title)
        else:
            print("None")
    else:
        print("Please provide a subreddit name.")

