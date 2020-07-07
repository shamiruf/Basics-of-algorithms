def sortNumbers(data, condition):
    new_list = []
    for item in data:
        new_list.append(float(item))
    if (condition == 'ASC') :
        for last in range(len(data)-1, 0, -1):
            for i in range(last):
                if data[i]>data[i+1]:
                    data[i],data[i+1]=data[i+1],data[i]
        return data
    elif(condition == 'DESC'):
        for last in range(len(data)-1, 0, -1):
            for i in range(last):
                if data[i]<data[i+1]:
                    data[i],data[i+1]=data[i+1],data[i]
        return data
    else:
        return False

def sortData(weights, data, condition):
    if len(weights) != len(data):
        raise ValueError('Invalid input data')
    else:
        if (condition == 'ASC') :
            for last in range(len(weights)-1, 0, -1):
                for i in range(last):
                    if weights[i]>weights[i+1]:
                        weights[i],weights[i+1]=weights[i+1],weights[i]
                        data[i],data[i+1]=data[i+1],data[i]
            return data
        elif(condition == 'DESC'):
            for last in range(len(weights)-1, 0, -1):
                for i in range(last):
                    if weights[i]<weights[i+1]:
                        weights[i],weights[i+1]=weights[i+1],weights[i]
                        data[i],data[i+1]=data[i+1],data[i]
            return data
        else:
            return False