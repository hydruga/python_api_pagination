import requests


def getTotalCharactersGender():
    baseurl = 'https://rickandmortyapi.com/api/character' 
    r = requests.get(baseurl)
    d = r.json()
    pages = d['info']['pages']
    male=0
    female=0
    for count in range(0, pages):
        print("Accessing page ", count+1, "of pages ", pages)
        data = r.json()
        for item in data['results']:
            name = item['name']
            gender = item['gender']
            if gender == 'Female':
                female+=1
            else:
                male+=1
        # Count starts at zero but pages counts from 1.
        if count < pages-1:
            # Once we've gone through all items on page, reassign request to next page.
            r = requests.get(data['info']['next'])
            


    print("Total male characters in Rick and Morty ", male)
    print("Total female characters in Rick and Morty ", female)

getTotalCharactersGender()
    
