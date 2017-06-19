#https://www.codewars.com/kata/temperature-converter/train/python

def convert_temp(temp, from_scale, to_scale):

    if from_scale == 'C' and to_scale == 'F':
        converted = ((9 * temp)/5)+32
        converted = int(round(converted))
        return converted
    elif from_scale == 'C' and to_scale == 'K':
        converted = (273.15 + temp)
        converted = int(round(converted))
        return converted
    elif from_scale == 'C' and to_scale == 'R':
        converted = ((273.15 + temp)*9)/5
        converted = int(round(converted))
        return converted  
    elif from_scale == 'C' and to_scale == 'De':
        converted = ((100 - temp)*3)/2
        converted = int(round(converted))
        return converted
    elif from_scale == 'C' and to_scale == 'N':
        converted = (temp * 0.33)
        converted = int(round(converted))
        return converted 
    elif from_scale == 'C' and to_scale == 'Re':
        converted = (temp * 0.8)
        converted = int(round(converted))
        return converted
    elif from_scale == 'C' and to_scale == 'Ro':
        converted = ((temp * 21)/40)+7.5
        converted = int(round(converted))
        return converted

    elif from_scale == 'F' and to_scale == 'C':
        converted = ((temp - 32)*5)/9
        converted = int(round(converted))
        return converted
    elif from_scale == 'F' and to_scale == 'K':
        converted = ((temp + 459.67)*5)/9
        converted = int(round(converted))
        return converted
    elif from_scale == 'F' and to_scale == 'R':
        converted = (temp + 459.67)
        converted = int(round(converted))
        return converted  
    elif from_scale == 'F' and to_scale == 'De':
        converted = ((212-temp)*5)/6
        converted = int(round(converted))
        return converted
    elif from_scale == 'F' and to_scale == 'N':
        converted = ((temp-32)*11)/60
        converted = int(round(converted))
        return converted 
    elif from_scale == 'F' and to_scale == 'Re':
        converted = ((temp - 32)*4)/9
        converted = int(round(converted))
        return converted
    elif from_scale == 'F' and to_scale == 'Ro':
        converted = (((temp-32)*7)/24)+7.5
        converted = int(round(converted))
        return converted

    elif from_scale == 'K' and to_scale == 'C':
        converted = (temp - 273.15)
        converted = int(round(converted))
        return converted
    elif from_scale == 'K' and to_scale == 'F':
        converted = ((temp * 9)/5)-459.67
        converted = int(round(converted))
        return converted
    elif from_scale == 'K' and to_scale == 'R':
        converted = ((temp * 9)/5)
        converted = int(round(converted))
        return converted  
    elif from_scale == 'K' and to_scale == 'De':
        converted = ((373.15 - temp) *3)/2
        converted = int(round(converted))
        return converted
    elif from_scale == 'K' and to_scale == 'N':
        converted = ((temp-273.13)*0.33)
        converted = int(round(converted))
        return converted 
    elif from_scale == 'K' and to_scale == 'Re':
        converted =  ((temp - 273.15)*4)/5
        converted = int(round(converted))
        return converted
    elif from_scale == 'K' and to_scale == 'Ro':
        converted = (((temp - 273.15)*21)/40)+7.5
        converted = int(round(converted))
        return converted

    elif from_scale == 'R' and to_scale == 'C':
        converted = ((temp - 491.67)*5)/9
        converted = int(round(converted))
        return converted
    elif from_scale == 'R' and to_scale == 'F':
        converted = (temp - 459.67)
        converted = int(round(converted))
        return converted
    elif from_scale == 'R' and to_scale == 'K':
        converted = (temp * 5)/9
        converted = int(round(converted))
        return converted  
    elif from_scale == 'R' and to_scale == 'N':
        converted = ((temp - 491.67)*11)/60
        converted = int(round(converted))
        return converted
    elif from_scale == 'R' and to_scale == 'De':
        converted = ((671.67 - temp)*5)/6
        converted = int(round(converted))
        return converted 
    elif from_scale == 'R' and to_scale == 'Re':
        converted = ((temp - 491.67)*4)/9
        converted = int(round(converted))
        return converted
    elif from_scale == 'R' and to_scale == 'Ro':
        converted = (((temp - 491.67)*7)/24)+7.5
        converted = int(round(converted))
        return converted

    elif from_scale == 'De' and to_scale == 'C':
        converted = (100 - (temp * 2)/3)
        converted = int(round(converted))
        return converted
    elif from_scale == 'De' and to_scale == 'F':
        converted = 212-(1.2*temp)
        converted = int(round(converted))
        return converted
    elif from_scale == 'De' and to_scale == 'K':
        converted = 373.15-((2*temp)/3)
        converted = int(round(converted))
        return converted  
    elif from_scale == 'De' and to_scale == 'R':
        converted = 671.67 - (temp * 1.2)
        converted = int(round(converted))
        return converted
    elif from_scale == 'De' and to_scale == 'N':
        converted = 33 - ((temp * 11)/50)
        converted = int(round(converted))
        return converted 
    elif from_scale == 'De' and to_scale == 'Re':
        converted = 80 - ((temp * 8)/15)
        converted = int(round(converted))
        return converted
    elif from_scale == 'De' and to_scale == 'Ro':
        converted = 60 - ((temp * 7)/20)
        converted = int(round(converted))
        return converted

    elif from_scale == 'N' and to_scale == 'C':
        converted = ((temp * 100)/33)
        converted = int(round(converted))
        return converted
    elif from_scale == 'N' and to_scale == 'F':
        converted = ((temp * 60)/11) + 32
        converted = int(round(converted))
        return converted
    elif from_scale == 'N' and to_scale == 'K':
        converted = ((temp * 100)/33) + 273.15
        converted = int(round(converted))
        return converted  
    elif from_scale == 'N' and to_scale == 'R':
        converted = ((temp * 60)/11) + 491.67
        converted = int(round(converted))
        return converted
    elif from_scale == 'N' and to_scale == 'De':
        converted = ((33 - temp) * 50)/11
        converted = int(round(converted))
        return converted 
    elif from_scale == 'N' and to_scale == 'Re':
        converted = (temp * 80)/33
        converted = int(round(converted))
        return converted
    elif from_scale == 'N' and to_scale == 'Ro':
        converted = ((temp * 35)/22) + 7.5
        converted = int(round(converted))
        return converted

    elif from_scale == 'Re' and to_scale == 'C':
        converted = temp*1.25
        converted = int(round(converted))
        return converted
    elif from_scale == 'Re' and to_scale == 'F':
        converted = (temp * 2.25) + 32
        converted = int(round(converted))
        return converted
    elif from_scale == 'Re' and to_scale == 'K':
        converted = (temp * 1.25) + 273.15
        converted = int(round(converted))
        return converted  
    elif from_scale == 'Re' and to_scale == 'R':
        converted = (temp * 2.25) + 491.67
        converted = int(round(converted))
        return converted
    elif from_scale == 'Re' and to_scale == 'De':
        converted = ((80 - temp)*15)/8
        converted = int(round(converted))
        return converted 
    elif from_scale == 'Re' and to_scale == 'N':
        converted = (temp * 33)/80
        converted = int(round(converted))
        return converted
    elif from_scale == 'Re' and to_scale == 'Ro':
        converted = ((21 * temp)/32) + 7.5
        converted = int(round(converted))
        return converted

    elif from_scale == 'Ro' and to_scale == 'C':
        converted = ((temp - 7.5)*40)/21
        converted = int(round(converted))
        return converted
    elif from_scale == 'Ro' and to_scale == 'F':
        converted = (((temp -7.5)*24)/7) + 32
        converted = int(round(converted))
        return converted
    elif from_scale == 'Ro' and to_scale == 'K':
        converted = (((temp - 7.5)*40)/21) + 273.15
        converted = int(round(converted))
        return converted  
    elif from_scale == 'Ro' and to_scale == 'R':
        converted = (((temp -7.5)*24)/7) + 491.67
        converted = int(round(converted))
        return converted
    elif from_scale == 'Ro' and to_scale == 'De':
        converted = ((60 - temp)*20)/7
        converted = int(round(converted))
        return converted 
    elif from_scale == 'Ro' and to_scale == 'N':
        converted = ((temp - 7.5)*22)/35
        converted = int(round(converted))
        return converted
    elif from_scale == 'Ro' and to_scale == 'Re':
        converted = ((temp - 7.5)*32)/21
        converted = int(round(converted))
        return converted  
    else:
        return temp
