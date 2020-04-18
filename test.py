# import twint


# c = twint.Config()
# c.Username = "@Greschinov"
# c.Custom["tweet"] = ["tweet", "replies_count"]
# c.Output = "tweets.csv"
# c.Store_csv = True

# twint.run.Search(c)


import twint

c = twint.Config()
c.Username = "@Greschinov"
c.Output = "tweets.csv"
c.Store_csv = True

twint.run.Search(c)