# HackCambridge2021
## Inspiration
Right from the beginning our team decided we will do a little something to raise the public's awareness of the environment we live in, and we did! This project integrates the fun challenge of discovering local plants into daily walks. It encourages users to not only learn more about our amazing green neighbours, but also to keep active in the lockdown.

Honestly, plants deserve much more recognition than they currently receive. They play such important roles in our ecosystem – they are the foundation of nearly every food chain, act as carbon storages through photosynthesis, prevent soil degradation, retain underground water, regulate global climate and local air quality, and provide a safe shelter for the native faunas like birds and insects. While there are plenty of bird watchers and bug collectors that relishes the capture of new specimens and photos around the globe (narcissistic-but-not-really fact: did you know that **none** of them would exist if not for our incredible plants?), we figured, why not make plant hunting the next big hit? And that is where the “Flora Quest” began. 

## What it does
Users may enter their postcode and how far they are willing to go on their next walk on the web app.The app would generate a list of local landmark plants within the radius range to discover (i.e. a chestnut tree opposite from Domino) and create a personalised walking route. A reference picture of the species (scraped from the internet) will be provided to help users identify the plants. Users can then take and upload a picture of the specimen, while our app, made powerful through machine learning, will determine if the right species is found. Upon confirmation, the user will be awarded Flora points, which can be used to unlock trophies or new features.

## Challenges we ran into
1. Finding a dataset that's publicly available and has a reasonable number of datapoints in a given geographical area is a pain. We had to switch demo region a few times due to unsuitable data – we doubt our users can find that patch of moss on the on the verge of the sidewalk recorded in 1998. 
2. The database is slow and has limited capacity.
3. Integrating the different tools like the scraper that is written in Python with the Angular frontend was tricky.
4. We ran into trouble evaluating the model.
5. Understanding the best configurations and parameters for the resnet50.
6. Using a new platform efficiently, especially when ran into installation problems and limited documentation in English.

## What's next for Flora Quest
1. Expand region
2. Gamify it more. The leveling up system, a collector album or journal, discovery map etc.
3. Optimisation. E.g. data scraping from the NBN site is slow; model needs more training.
4. Potentially include animal recognition.
5. Educational/charity aspect - use flora points to unlock fun plant facts or for fund raising
6. More references besides photo to help user identify species.

![first_page](https://github.com/alicebarbe/HackCambridge2021/blob/webapp/first_page.png)
