# This script contains code to fill empty data using statistical methods

def cleanGender(x):
    if x in ['female', 'mostly_female']:
        return 'female'
    if x in ['male', 'mostly_male']:
        return 'male'
    if x in ['couple']:
        return 'couple'
    else:
        return 'unknownGender'

def cleanBathRoom(x):
    if x == '7+':
        return 7
    if float(x) < 7:
        return x
    else:
        return 1


def cleanBedrooms(x):
    if float(x) <= 7:
        return x
    else:
        return 1


def cleanNumBeds(x):
    if float(x) <= 7:
        return x
    else:
        return 1


def cleanNumberBed(x):
    if float(x) <= 7:
        return x
    else:
        return 1


def cleanRespRate(x):
    val = str(x).replace('%', '').replace('$', '').strip()
    if str(x) == 'nan':
        return 92.1
    else:
        return val


def dummyCode(x, cols=[u'BookInstantly', u'Cancellation', u'RespTime', u'S_BedType', u'S_PropType', u'SD_PropType',
                       'HostGender']):
    import pandas as pd

    dfCopy = x[:]

    dfCopy.RespRate = x.RespRate.apply(cleanRespRate)
    dfCopy.Price = x.Price.apply(cleanRespRate)
    dfCopy.HostGender = x.HostGender.apply(cleanGender)
    dfCopy.S_Bathrooms = x.S_Bathrooms.apply(cleanBathRoom)
    dfCopy.S_Bedrooms = x.S_Bedrooms.apply(cleanBedrooms)
    dfCopy.S_NumBeds = x.S_NumBeds.apply(cleanNumBeds)

    for col in cols:
        DC = pd.get_dummies(x[col], col)
        dfCopy = pd.concat([dfCopy, DC], axis=1)

    retainedCols = [a for a in dfCopy.columns if a not in cols]

    return dfCopy[retainedCols]