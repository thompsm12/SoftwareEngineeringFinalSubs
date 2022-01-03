from github import Github
import json
import pygal

g = Github("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")
usr = g.get_user()
print("user: " + usr.login)


try:
	g.get_user("github")
except:
	print("Invalid token!")
	sys.exit()

userInput=input("Enter a Github username to visualise data for: ")
try:
	usr=g.get_user(userInput)
except:
	print("User does not exist!")
	sys.exit()
print("###### profile: "+ usr.login +" ######")
print("Information from github profile from url: " + "https://api.github.com/users/" + usr.login)


repositoriesDict={}
profilesOfFollowers={}
Userslanguages={}
UserRepoDeets={}
dct_follower_info={}
profilesOfFollowers={}
infoOfTheFollowersRepos={}
FollowersRepos={}
FollowersLanguages={}
UsersMainLanguages = {}
FollowersMainLanguages = {}
followersLocations = {}
followersPublicRepos = {}
sameLanguageCount = 0
notSameLanguage = 0
avgFollowers = 0
commonLanguages = 0

i=0
m=0
for repo in usr.get_repos():
	Userslanguages[i]=repo.get_languages()
	UserRepoDeets['languages']=Userslanguages[i]

	if repo.language is not None:
		UsersMainLanguages[m]=repo.language
		m+=1
	i+=1

k=0
m=0
pie_chart1 = pygal.Pie()
pie_chart1.title = 'Number of repositories user has versus their followers'
for follower in usr.get_followers():

	j=0
	for repo in follower.get_repos():

		if repo.language is not None:
			FollowersMainLanguages[m] = repo.language
			for language in UsersMainLanguages:

				if language == repo.language:
					commonLanguages += 1
					m += 1

		FollowersRepos[repo.full_name]=dict(infoOfTheFollowersRepos)
		j+=1

	dct_follower_info['followers']=follower.followers
	avgFollowers = avgFollowers + follower.followers 
	followersLocations[k] = follower.location
	followersPublicRepos[k]= follower.public_repos

	pie_chart1.add(follower.name, follower.public_repos)

	k+=1


avgFollowers = avgFollowers / k
pie_chart1.add(usr.name, usr.public_repos)
pie_chart1.render_in_browser()





pie_chart = pygal.Pie()
pie_chart.title = 'Followers User has verus Average number of Followers for their Followers'
pie_chart.add('Users followers', usr.followers)
pie_chart.add('Average followers of the followers', avgFollowers)

pie_chart.render_in_browser()


# pie_chart = pygal.Pie()
# pie_chart.title = 'Locations'

# pie_chart.add('Users Repos', usr.public_repos)
# for int in followersPublicRepos:
# 	print(repo)
# 	pie_chart.add('Other Repos', repo)


# pie_chart.render_in_browser()

