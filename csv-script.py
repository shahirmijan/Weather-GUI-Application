import requests, csv

outputarray = []
count = 0
with open("world-universities-csv/world-universities.csv", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        count += 1
        if count < 6499:
            pass
        else:
            country = row[0]
            uni = row[1]
            uni = uni.replace(" ","+")
            r = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json?query="+uni+"&region="+country+"&key=AIzaSyCLdqdKX89O6AK2y5MYEDmDba6bg4jYx-E")
            obj = r.json()
            try:
                outputarray.append([row[1],obj["results"][0]["geometry"]["location"]["lat"],obj["results"][0]["geometry"]["location"]["lng"]])
            except:
                print(uni)
    csvfile.close()
with open("uni-locations1.csv","w",newline='',encoding="utf8") as csvfile:
    writer = csv.writer(csvfile)
    for row in outputarray:
        try:
            writer.writerow(row)
        except:
            print(row[0])
    csvfile.close()
