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

    apple_sort1 = Appledata.iloc[:113]
    apple_sort2 = Appledata.iloc[113:226]
    apple_sort3 = Appledata.iloc[226:340]
    apple_sort4 = Appledata.iloc[340:]
    last_q_apple = len(Appledata.iloc[340:])-1

    a1_O = apple_sort1.iloc[:1]["Open"]
    a1_C = apple_sort1.iloc[112:]["Close"]
    a1 = round((int(a1_C)-int(a1_O))/int(a1_O)*100,2)

    a2_O = apple_sort2.iloc[:1]["Open"]
    a2_C = apple_sort2.iloc[112:]["Close"]
    a2 = round((int(a2_C)-int(a2_O))/int(a2_O)*100,2)

    a3_O = apple_sort3.iloc[:1]["Open"]
    a3_C = apple_sort3.iloc[113:]["Close"]
    a3 = round((int(a3_C)-int(a3_O))/int(a3_O)*100,2)

    a4_O = apple_sort4.iloc[:1]["Open"]
    a4_C = apple_sort4.iloc[last_q_apple:]["Close"]
    a4 = round((int(a4_C)-int(a4_O))/int(a4_O)*100,2)

    Appl_json = {
        "numbers": changes,
        "labels": labels,
        "Dates": gg,
        "Dates_Normal": ggN,
        "Volume": Volume,
        "Close": Close,
        "Qs": [a1, a2, a3, a4],
        "Qmarks": ["1","2","3","4"]
    }

    import pymongo

    # # Create connection variable
    # conn = 'mongodb://localhost:27017'
    # Create connection variable
    # conn = 'mongodb://localhost:27017' or "mongodb://heroku_8nx1c4b9:gebgv4dmtcjvsgpgq8kbdd76g3@ds117623.mlab.com:17623/heroku_8nx1c4b9"
    conn = "mongodb://heroku_8nx1c4b9:gebgv4dmtcjvsgpgq8kbdd76g3@ds117623.mlab.com:17623/heroku_8nx1c4b9"

    # Pass connection to the pymongo instance.
    client = pymongo.MongoClient(conn)

    # Connect to a database. Will create one if not already available.
    # db = client.Apple_y_y
    # Fix done by in for Heroku deployment
    db = client.heroku_8nx1c4b9

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

    ib1 = IBMdata.iloc[:170]
    ib2 = IBMdata.iloc[170:340]
    ib3 = IBMdata.iloc[340:510]
    ib4 = IBMdata.iloc[510:]
    last_q_ibm = len(IBMdata.iloc[510:])-1

    ib1_O = ib1.iloc[:1]["Open"]
    ib1_C = ib1.iloc[169:]["Close"]
    ib1D = round((int(ib1_C)-int(ib1_O))/int(ib1_O)*100,2)

    ib2_O = ib2.iloc[:1]["Open"]
    ib2_C = ib2.iloc[169:]["Close"]
    ib2D = round((int(ib2_C)-int(ib2_O))/int(ib2_O)*100,2)

    ib3_O = ib3.iloc[:1]["Open"]
    ib3_C = ib3.iloc[169:]["Close"]
    ib3D = round((int(ib3_C)-int(ib3_O))/int(ib3_O)*100,2)

    ib4_O = ib4.iloc[:1]["Open"]
    ib4_C = ib4.iloc[last_q_ibm:]["Close"]
    ib4D = round((int(ib4_C)-int(ib4_O))/int(ib4_O)*100,2)

    IBM_json = {
        "numbers": changes,
        "labels": labels,
        "Dates": gg,
        "Dates_Normal": ggN,
        "Volume": Volume,
        "Close": Close,
        "Qs": [ib1D, ib2D, ib3D, ib4D],
        "Qmarks": ["1","2","3","4"]

    }

    # #conn = 'mongodb://localhost:27017'
    # Fix done by in for Heroku deployment
    # conn = 'mongodb://localhost:27017' or "mongodb://heroku_8nx1c4b9:gebgv4dmtcjvsgpgq8kbdd76g3@ds117623.mlab.com:17623/heroku_8nx1c4b9"
 
    # Pass connection to the pymongo instance.
    client = pymongo.MongoClient(conn)

    # Connect to a database. Will create one if not already available.
    # db = client.IBM_y_y
    # Fix done by in for Heroku deployment
    db = client.heroku_8nx1c4b9

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

    in_sort1 = Inteldata.iloc[:115]
    in_sort2 = Inteldata.iloc[115:231]
    in_sort3 = Inteldata.iloc[231:347]
    in_sort4 = Inteldata.iloc[347:]
    last_q_i = len(Inteldata.iloc[347:])-1

    i1_O = in_sort1.iloc[:1]["Open"]
    i1_C = in_sort1.iloc[114:]["Close"]
    i1 = round((int(i1_C)-int(i1_O))/int(i1_O)*100,2)

    i2_O = in_sort2.iloc[:1]["Open"]
    i2_C = in_sort2.iloc[115:]["Close"]
    i2 = round((int(i2_C)-int(i2_O))/int(i2_O)*100,2)

    i3_O = in_sort3.iloc[:1]["Open"]
    i3_C = in_sort3.iloc[115:]["Close"]
    i3 = round((int(i3_C)-int(i3_O))/int(i3_O)*100,2)

    i4_O = in_sort4.iloc[:1]["Open"]
    i4_C = in_sort4.iloc[last_q_i:]["Close"]
    i4 = round((int(i4_C)-int(i4_O))/int(i4_O)*100,2)

    Intel_json = {
        "numbers": changes,
        "labels": labels,
        "Dates": gg,
        "Dates_Normal": ggN,
        "Volume": Volume,
        "Close": Close,
        "Qs": [i1, i2, i3, i4],
        "Qmarks": ["1","2","3","4"]

    }

    # Connect to a database. Will create one if not already available.
    # db = db = client.Intel_y_y
    # Fix done by in for Heroku deployment
    db = client.heroku_8nx1c4b9

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

    m_sort1 = Micodata.iloc[:98]
    m_sort2 = Micodata.iloc[98:196]
    m_sort3 = Micodata.iloc[196:293]
    m_sort4 = Micodata.iloc[293:]
    last_q_m = len(Micodata.iloc[293:])-1

    m1_O = m_sort1.iloc[:1]["Open"]
    m1_C = m_sort1.iloc[97:]["Close"]
    m1 = round((int(m1_C)-int(m1_O))/int(m1_O)*100,2)

    m2_O = m_sort2.iloc[:1]["Open"]
    m2_C = m_sort2.iloc[97:]["Close"]
    m2 = round((int(m2_C)-int(m2_O))/int(m2_O)*100,2)

    m3_O = m_sort3.iloc[:1]["Open"]
    m3_C = m_sort3.iloc[96:]["Close"]
    m3 = round((int(m3_C)-int(m3_O))/int(m3_O)*100,2)

    m4_O = m_sort4.iloc[:1]["Open"]
    m4_C = m_sort4.iloc[last_q_m:]["Close"]
    m4 = round((int(m4_C)-int(m4_O))/int(m4_O)*100,2)
    MSFT_json = {
        "numbers": changes,
        "labels": labels,
        "Dates": gg,
        "Dates_Normal": ggN,
        "Volume": Volume,
        "Close": Close,
        "Qs": [m1, m2, m3, m4],
        "Qmarks": ["1","2","3","4"]
    }

    # Connect to a database. Will create one if not already available.
    # db = client.MSFT_y_y
    # Fix done by in for Heroku deployment
    db = client.heroku_8nx1c4b9

    # Drops collection if available to remove duplicates
    db.msft_y_o_y.drop()

    # Creates a collection in the database and insert document
    db.msft_y_o_y.insert_one(
        MSFT_json
    )
    print("mongo complete")
