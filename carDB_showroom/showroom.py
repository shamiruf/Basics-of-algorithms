class Node:
    def __init__(self, nextNode, prevNode, data):
        self.nextNode = None
        self.prevNode = None
        self.data = data 


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0


class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active
    def __str__(self):
        return '<Car: id = ' + str(self.identification) +  '; name = ' + str(self.name) + ' ; brand = ' + str(self.brand) +  '; price = ' + str(self.price) +  '; active = ' + str(self.active) + '>'



db = LinkedList()


def init(cars):
    for car in cars:
        add(car)

def add(car):
    cur_node = Node(None, None, car)
    first = db.head

    if (first is None):
        db.head = cur_node
       # print('Head is ' + str(db.head.data.price) + '') 
    elif (car.price < first.data.price):
        db.head.prevNode = cur_node
        cur_node.nextNode = db.head
        db.head = cur_node
    else:
        while (first.nextNode is not None) and (car.price >= first.nextNode.data.price):
            first = first.nextNode

        cur_node.nextNode = first.nextNode
        first.nextNode = cur_node
        cur_node.prevNode = first

        if (first.nextNode is None):
            #print('NEXXT NODE NONE')
            if (car.price >= first.data.price):
                cur_node.prevNode = first
                first.nextNode = cur_node
                #print('Now head is ' + str(db.head.data.price) + 'and next one is ' + str(db.head.nextNode.data.price) + '')
            else:
                db.head = cur_node
                cur_node.nextNode = first
                first.prevNode = cur_node
            

    db.count += 1
    print(db.count)
 
#cars = [ Car(1,'x','bmw',300, True),  Car(2,'y','toyota',1000, True), Car(3,"z", "audi",3000, True)]
#init(cars)

 
#head = db.head


#for i in range(0, db.count):
    #print(head.data.price)
    #head = head.nextNode


def updateName(identification, name):
    while (db.head != None):
        if (db.head.data.identification == identification):
            db.head.data.name = name
            return
        else:
            db.head = db.head.nextNode


def updateBrand(identification, brand):
    while (db.head != None):
        if (db.head.data.identification == identification):
            db.head.data.brand = brand
            return
        else:
            db.head = db.head.nextNode


def activateCar(identification):
    while (db.head != None):
        if (db.head.data.identification == identification):
            db.head.data.active == True
        db.head = db.head.nextNode


def deactivateCar(identification):
    while (db.head != None):
        if (db.head.data.identification == identification):
            db.head.data.active == False
        db.head = db.head.nextNode


def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    sumPrice = 0
    while (db.head != None):
        if (db.head.data.active == True):
            sumPrice += db.head.data.price
        db.head = db.head.nextNode
    return sumPrice


def clean():
    db.head = None
    db.end = None
    db.count = 0
