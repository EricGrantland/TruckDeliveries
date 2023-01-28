# Eric Grantland - id: 004612770

import csv
import datetime

# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, key, item):
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        #update key if it is already in bucket
        for kv in bucket_list:
            #print (key_value)
            if kv[0] == key:
                key[1] = item
                return True

        #if not, insert item to the end of the bucket list
        key_value = [key, item]
        bucket_list.append([item.ID, item])
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for key_value in bucket_list:
            #print key_value
            if key_value[0] == key:
                return key_value[1]
        return None

    def getAddress(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for key_value in bucket_list:
            # print key_value
            if key_value[0] == key:
                return key_value[1]
        return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

    def setStatusDelivered(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # change status to delivered.
        for kv in bucket_list:
            if kv[0] == key:
                kv[1].setStatus("Delivered!")

    def setDeliveryTime(self, key, time):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # change status to delivered.
        for kv in bucket_list:
            if kv[0] == key:
                kv[1].setDeliveryTime(time)

    def setInRouteTime(self, key, time):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # change status to delivered.
        for kv in bucket_list:
            if kv[0] == key:
                kv[1].setInRouteTime(time)

    def getDeliveryTime(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # change status to delivered.
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1].getDeliveryTime()

    def getDeadline(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # change status to delivered.
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1].getDeadline()

    def getInRouteTime(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # change status to delivered.
        for kv in bucket_list:
            if kv[0] == key:
                time = datetime.datetime.strptime(str(kv[1].getInRouteTime()), '%H:%M:%S')
                return datetime.timedelta(0, 0, 0, time.second, time.minute, time.hour, 0)

    def getStatus(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # change status to delivered.
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1].getStatus()

# Hash table instance
packageHashMap = ChainingHashTable()

class Package:
    def __init__(self, ID, address, city, zipCode, deadline, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.zipCode = zipCode
        self.deadline = deadline
        self.deliveryTime = None
        self.inRouteTime = None
        self.weight = weight
        self.status = status

    def __str__(self):  # overwite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.zipCode,
                                               self.deadline, self.weight, self.status)
    def getId(self):
        return self.ID

    def getAddress(self):
        return self.address

    def getWeight(self):
        return self.weight

    def getDeadline(self):
        return self.deadline

    def setDeliveryTime(self, time):
        self.deliveryTime = time

    def getDeliveryTime(self):
        return self.deliveryTime

    def setInRouteTime(self, time):
        self.inRouteTime = time

    def getInRouteTime(self):
        return self.inRouteTime

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

#load data from Packges csv file into the packageHashMap
def loadPackageData(fileName):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=",")
        next(packageData)  # skip header
        for package in packageData:
            iD = int(package[0])
            address = package[1]
            city = package[2]
            zipCode = package[3]
            deadline = package[4]
            weight = package[5]
            status = "Loaded"

            # package object
            p = Package(iD, address, city, zipCode, deadline, weight, status)
            # print(p)

            # insert it into the hash table
            packageHashMap.insert(iD, p)

class Truck:
    def __init__ (self, capacity, speed, load, packages):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages

    def getPackages(self):
        return self.packages

    def setLoad(self, load):
        self.load = load



# Load packages to Hash Table
loadPackageData('Packages.csv')

#load data from Distances2 csv file into the distanceData array
def loadDistanceData(fileName):
    distanceArray = []
    finalArray = []
    with open(fileName) as distances:
        distanceData = csv.reader(distances, delimiter="\n")
        next(distanceData)  # skip header
        for distance in distanceData:

            distanceArray.append(distance)
            #print(distance)
        for x in distanceArray:
            for y in x:
                num = y.split(",")
                for z in range(len(num)):
                    num[z] = float(num[z])

                finalArray.append(num)
        return finalArray

distanceData = loadDistanceData('Distances2.csv')

#load data from Distances2 csv file into the addressData array
def loadAddressData(fileName):
    addressArray = []
    with open(fileName) as addresses:
        addressData = csv.reader(addresses, delimiter="\n")
        next(addressData)  # skip header
        for address in addressData:
            addressArray.append(address[0])
        return addressArray

addressData = loadAddressData('Addresses.csv')

#find distance between 2 addresses using distanceData array
def distanceBetween(address1, address2):
    index1 = addressData.index(address1)
    index2 = addressData.index(address2)
    if index1 > index2:
        distance = distanceData[index1][index2]
    else:
        distance = distanceData[index2][index1]
    return float(distance)

#Use nearest neighbor ideology to find nearest next address within an array of packages
def minDistanceFromAddress(address, packages):
    min = 1000.0
    nextAddress = None
    nextPackageId = 0
    for package in packages:
        distance =distanceBetween(address, packageHashMap.search(package).getAddress())
        if distance < min and distance >= 0.0:
            min = distance
            nextAddress = packageHashMap.search(package).getAddress()
            nextPackageId = packageHashMap.search(package).getId()

    return nextAddress, nextPackageId, min

#create truck objects
truck1 = Truck(16, 18.0, 16, [1, 4, 7, 13, 14, 15, 16, 19, 20, 21, 29, 30, 33, 37, 40])
truck2 = Truck(16, 18.0, 16, [2, 3, 5, 6, 8, 9, 12, 17, 18, 25, 26, 31, 32, 34, 36, 38])
truck3 = Truck(16, 18.0, 8, [10, 11, 22, 23, 24, 27, 28, 35, 39])

#track truck routing, mileage, and information on status and delivery time of packages
def deliveringPackages(truck, startTime):
    miles = 0
    time = startTime
    packages = truck.getPackages()
    for package in packages:
        packageHashMap.setInRouteTime(package, startTime)
    currentAddress = "HUB"
    while len(packages) > 0:
        nextAddress = minDistanceFromAddress(currentAddress, packages)[0]
        nextPackageId = minDistanceFromAddress(currentAddress, packages)[1]
        nextTrip = minDistanceFromAddress(currentAddress, packages)[2]
        miles = miles + nextTrip
        packageHashMap.setStatusDelivered(nextPackageId)
        time = time + datetime.timedelta(minutes=(nextTrip * (60.0 / 18.0)))
        packageHashMap.setDeliveryTime(nextPackageId, time)
        currentAddress = nextAddress
        packages.remove(nextPackageId)

    miles = miles + float(distanceData[0][addressData.index(currentAddress)])

    time = time + datetime.timedelta(minutes=(miles / 18.0 * 60))
    return miles, time

#each truck departs at given time. returns mileage for each truck
t1 = deliveringPackages(truck1, datetime.timedelta(0, 0, 0, 0, 0, 8, 0))[0]
t2 = deliveringPackages(truck2, datetime.timedelta(0, 0, 0, 0, 15, 9, 0))[0]
t3 = deliveringPackages(truck3, datetime.timedelta(0, 0, 0, 0, 0, 10, 0))[0]

totalMiles = round(t1 + t2 + t3, 2)

#user interface
exit = True
while (exit):
    option = input("What information would you like to see? Please select an option. Type 'quit' to exit\n"
      "1) Package Information\n"
      "2) Truck Information\n"
      "Category Number > ")
    if option == "1":
        option2 = input("How would you like to view the package info?\n"
              "1) A single package at a specific time of day\n"
              "2) All packages at a specific time of day\n"
              "Category number > ")
        if option2 == "1":
            time = input("Enter a time (HH:MM) > ")
            time2 = datetime.datetime.strptime(time, '%H:%M')
            time3 = datetime.timedelta(0, 0, 0, 0, time2.minute, time2.hour, 0)
            packageCheckId = input("Package ID > ")
            if time3 < packageHashMap.getInRouteTime(int(packageCheckId)):
                print("Package ", packageCheckId, " status: at the HUB and ready for delivery!")
            elif time3 < packageHashMap.getDeliveryTime(int(packageCheckId)):
                print("Package ", packageCheckId, " status: In Route!")
            else:
                print("Package ", packageCheckId, " status: Delivered at ", packageHashMap.getDeliveryTime(int(packageCheckId)),
                          " | Deadline: ", packageHashMap.getDeadline(int(packageCheckId)))
        elif option2 == "2":
            time = input("Enter a time (HH:MM) > ")
            time2 = datetime.datetime.strptime(time, '%H:%M')
            time3 = datetime.timedelta(0, 0, 0, 0, time2.minute, time2.hour, 0)
            for i in range(0, 40):
                if time3 < packageHashMap.getInRouteTime(i + 1):
                    print("Package ", i + 1, " status: At the HUB and ready for delivery!")
                elif time3 < packageHashMap.getDeliveryTime(i + 1):
                    print("Package ", i + 1, " status: In Route!")
                else:
                    print("Package ", i + 1, " status: Delivered at ", packageHashMap.getDeliveryTime(i + 1),
                          " | Deadline: ", packageHashMap.getDeadline(i + 1))
        else:
            print("please select a valid option")

    elif option == "2":
        option2 = input("How would you like to view the truck info?\n"
                        "1) View the total mileage on a single truck\n"
                        "2) View the total mileage on ALL trucks\n"
                        "Category number > ")
        if option2 == "1":
            option3 = input("Which truck's mileage would you like to view? (1, 2, or 3)\n"
                            "Truck number > ")
            if option3 == "1":
                print("Total mileage for truck 1: ", t1, " miles")
            elif option3 == "2":
                print("Total mileage for truck 2: ", t2, " miles")
            elif option3 == "3":
                print("Total mileage for truck 3: ", t3, " miles")
            else:
                print("Invalid selection")

        elif option2 == "2":
            print("Truck 1: ", t1, "\nTruck 2: ", t2, "\n"
                    "Truck 3: ", t3, "\nTotal mileage: ", totalMiles, " miles")
        else:
            print("invalid selection")
    elif option == "quit":
        print("Goodbye")
        exit = False
    else:
        print("invalid selection")