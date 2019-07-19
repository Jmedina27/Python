import webbrowser
import time
import random

#while the program is runnig 
while True:
    #create a varaible that contains the google search link
    url = "https://www.google.com/search?client=safari&rls=en&ei=rWUVXbX2K7Gx0PEPqoaLmAE&q=you+are+being+hacked&oq=you+are+being+hacked&gs_l=psy-ab.3..0l2j0i22i30l4j0i22i10i30j0i22i30l3.30495.33262..33502...0.0..0.107.1621.17j3......0....1..gws-wiz.......0i71j35i39j0i131j0i131i67j0i67j0i20i263.pM3sDBKIJ4Q"
    #create a variable called sites that holds a list of choices in which we use the random module to randomly select which site to go in the list
    sites = random.choice(["craigslist.com", "reddit.com", "betaprofiles.com", "ansible.com", 
    "bing.com", "yahoo.com", url])

    #format the websites in the list so that they are in http form
    visit = "http://{}".format(sites)

    #use the webbrowser module to open the specified formatted sites in the variable visit
    webbrowser.open(visit)

    #create a variable seconds to randomly determine the range of seconds to have the program sleep 
    seconds = random.randrange(20, 60)
    time.sleep(seconds)
