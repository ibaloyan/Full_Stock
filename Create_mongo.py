import quandl
from datetime import datetime
import pandas as pd

def populate():
    # pull data for microsoft, apple, google, amazon , bitcoin
    quandl.ApiConfig.api_key = "V2vzspYSYL8eenGuq8uF "
    url = 'https://www.quandl.com/api/v3/databases/EOD/metadata?api_key=V2vzspYSYL8eenGuq8uF'

    mydata = pd.DataFrame(quandl.get("EOD/AAPL",collapse="monthly"))

    Appledata = mydata[["Open","High","Low","Close","Volume","Split"]]

    Appledata.reset_index(inplace = True)

    gg = []
    ggN = []
    for hh in Appledata["Date"]:

        gg.append(f"{hh.year}-{hh.month}-{hh.day}")
        ggN.append(f"{hh.year}-{hh.month}-{hh.day}")
    #     print(hh.month)
    # gg.remove(-1)
    # print(len(ggN))
    del gg[-1]

    Volume = []
    for Vo in Appledata["Volume"]:
        Volume.append(Vo)
    len(Volume)
    Close = []
    for Co in Appledata["Close"]:
        Close.append(Co)
    len(Close)
    year = 1980

    x = 0
    changes = []
    while x < (len(Appledata)-1):
        openV = Appledata["Open"][x]

        closeV = Appledata["Close"][x+1]
        changes.append(round((closeV-openV)/openV*100, 2))

        x += 1

    months = ["January","Febuary","March","April","May","June","July","August","Septemeber","October","November","December"]
    year = 1981
    labels = []
    while year < 2018:
        for month in months:
            labels.append(str(month) + " " + str(year))
        year += 1
    labels.append("January 2018")
    labels.append("Febuary 2018")
    labels.append("March 2018")
    labels.append("April 2018")
    labels.append("May 2018")
    labels.append("June 2018")
    labels.append("July 2018")
    labels.append("August 2018")
    labels = ["Dec1980"] + labels

    Appl_json = {
        "numbers": changes,
        "labels": labels,
        "Dates": gg,
        "Dates_Normal": ggN,
        "Volume": Volume,
        "Close": Close
    }

    import pymongo

    # Create connection variable
    conn = 'mongodb://localhost:27017'

    # Pass connection to the pymongo instance.
    client = pymongo.MongoClient(conn)

    # Connect to a database. Will create one if not already available.
    db = client.Apple_y_y

    # Drops collection if available to remove duplicates
    db.apple_y_o_y.drop()

    # Creates a collection in the database and insert document
    db.apple_y_o_y.insert_one(
        Appl_json
    )

    ##### Next Stock
    mydata2 = quandl.get("EOD/IBM",collapse="monthly")

    IBMdata = mydata2[["Open","High","Low","Close","Volume","Split"]]
    IBMdata.reset_index(inplace = True)

    gg = []
    ggN = []
    for hh in IBMdata["Date"]:

        gg.append(f"{hh.year}-{hh.month}-{hh.day}")
        ggN.append(f"{hh.year}-{hh.month}-{hh.day}")
    #     print(hh.month)
    # gg.remove(-1)
    len(gg)
    del gg[-1]

    Volume = []
    for Vo in IBMdata["Volume"]:
        Volume.append(Vo)
    len(Volume)
    Close = []
    for Co in IBMdata["Close"]:
        Close.append(Co)

    year = 1962

    x = 0
    changes = []
    while x < (len(IBMdata)-1):
        openV = IBMdata["Open"][x]

        closeV = IBMdata["Close"][x+1]
        changes.append(round((closeV-openV)/openV*100,2))

        x += 1

    months = ["January","Febuary","March","April","May","June","July","August","Septemeber","October","November","December"]
    year = 1962
    labels = []
    while year < 2018:
        for month in months:
            labels.append(str(month) + " " + str(year))
        year += 1
    labels.append("January 2018")
    labels.append("Febuary 2018")
    labels.append("March 2018")
    labels.append("April 2018")
    labels.append("May 2018")
    labels.append("June 2018")
    labels.append("July 2018")
    labels.append("August 2018")

    IBM_json = {
        "numbers": changes,
        "labels": labels,
        "Dates": gg,
        "Dates_Normal": ggN,
        "Volume": Volume,
        "Close": Close
    }

    conn = 'mongodb://localhost:27017'

    # Pass connection to the pymongo instance.
    client = pymongo.MongoClient(conn)

    # Connect to a database. Will create one if not already available.
    db = client.IBM_y_y

    # Drops collection if available to remove duplicates
    db.ibm_y_o_y.drop()

    # Creates a collection in the database and insert document
    db.ibm_y_o_y.insert_one(
        IBM_json
    )

    ### Next Stock
    mydata3 = quandl.get("EOD/INTC",collapse="monthly")
    Inteldata = mydata3[["Open","High","Low","Close","Volume","Split"]]
    Inteldata.reset_index(inplace = True)

    gg = []
    ggN = []
    for hh in Inteldata["Date"]:

        gg.append(f"{hh.year}-{hh.month}-{hh.day}")
        ggN.append(f"{hh.year}-{hh.month}-{hh.day}")
    #     print(hh.month)
    # gg.remove(-1)
    len(gg)
    del gg[-1]

    Volume = []
    for Vo in Inteldata["Volume"]:
        Volume.append(Vo)
    len(Volume)
    Close = []
    for Co in Inteldata["Close"]:
        Close.append(Co)

        year = 1979

    x = 0
    changes = []
    while x < (len(Inteldata)-1):
        openV = Inteldata["Open"][x]

        closeV = Inteldata["Close"][x+1]
        changes.append(round((closeV-openV)/openV*100,2))

        x += 1
    months = ["January","Febuary","March","April","May","June","July","August","Septemeber","October","November","December"]
    year = 1980
    labels = []
    while year < 2018:
        for month in months:
            labels.append(str(month) + " " + str(year))
        year += 1
    labels.append("January 2018")
    labels.append("Febuary 2018")
    labels.append("March 2018")
    labels.append("April 2018")
    labels.append("May 2018")
    labels.append("June 2018")
    labels.append("July 2018")
    labels.append("August 2018")
    labels.pop(0)
    labels.pop(0)

    Intel_json = {
        "numbers": changes,
        "labels": labels,
        "Dates": gg,
        "Dates_Normal": ggN,
        "Volume": Volume,
        "Close": Close
    }

    db = client.Intel_y_y

    # Drops collection if available to remove duplicates
    db.intel_y_o_y.drop()

    # Creates a collection in the database and insert document
    db.intel_y_o_y.insert_one(
        Intel_json
    )


    mydata1 = quandl.get("EOD/MSFT",collapse="monthly")
    Micodata = mydata1[["Open","High","Low","Close","Volume","Split"]]
    Micodata.reset_index(inplace = True)

    gg = []
    ggN = []
    for hh in Micodata["Date"]:

        gg.append(f"{hh.year}-{hh.month}-{hh.day}")
        ggN.append(f"{hh.year}-{hh.month}-{hh.day}")
    #     print(hh.month)
    # gg.remove(-1)
    len(gg)
    del gg[-1]

    Volume = []
    for Vo in Micodata["Volume"]:
        Volume.append(Vo)
    len(Volume)
    Close = []
    for Co in Micodata["Close"]:
        Close.append(Co)

    year = 1980

    x = 0
    changes = []
    while x < (len(Micodata)-1):
        openV = Micodata["Open"][x]

        closeV = Micodata["Close"][x+1]
        changes.append(round((closeV-openV)/openV*100,2))

        x += 1

    months = ["January","Febuary","March","April","May","June","July","August","Septemeber","October","November","December"]
    year = 1986
    labels = []
    while year < 2018:
        for month in months:
            labels.append(str(month) + " " + str(year))
        year += 1
    labels.append("January 2018")
    labels.append("Febuary 2018")
    labels.append("March 2018")
    labels.append("April 2018")
    labels.append("May 2018")
    labels.append("June 2018")
    labels.append("July 2018")
    labels.append("August 2018")
    labels.pop(0)
    labels.pop(0)

    MSFT_json = {
        "numbers": changes,
        "labels": labels,
        "Dates": gg,
        "Dates_Normal": ggN,
        "Volume": Volume,
        "Close": Close
    }

    db = client.MSFT_y_y

    # Drops collection if available to remove duplicates
    db.msft_y_o_y.drop()

    # Creates a collection in the database and insert document
    db.msft_y_o_y.insert_one(
        MSFT_json
    )
    print("mongo complete")
