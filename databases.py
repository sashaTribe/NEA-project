import sqlite3

def create_database():
    with sqlite3.connect("NEA_sqlite_create.sql") as db:
        cursor = db.cursor()

#table describing the contents of each user's table
        individualTestTable = """
    CREATE TABLE individualTestTable (
	tableID integer PRIMARY KEY ,
	tablename string  ,
	observedFreqValueID integer ,
	UserID integer,
	Success boolean,
	NumberOfRows integer,
	NumberOfColumns integer,
	ModifyDate datetime,
	df integer,
  FOREIGN KEY(UserID) REFERENCES UserTable(id),
  FOREIGN KEY(observedFreqValueID) REFERENCES observedfrequencyValues(id),
  FOREIGN KEY(df) REFERENCES chiSquareDistribution(id)
);
"""

#table holding value for observed frequency table

    observedFreqTable = """

    CREATE TABLE observedfrequencyValues (
	observedFreqValueID integer PRIMARY KEY,
	obFreqColID integer,
	obFreqRowID integer,
	Value real,
	FOREIGN KEY(obFreqColID) REFERENCES observedFreqColumns(id),
	FOREIGN KEY(obFreqRowID) REFERENCES observedFreqRow(id)
    );"""

#stores the category name
    observedFreqColumns = """
    CREATE TABLE observedFrequencyColumn (
	obFreqColID integer PRIMARY KEY ,
	categoryName text
    ); """

#stores the group name
    observedFreqRow = """
    CREATE TABLE observedFrequencyRow (
	obFreqRowID integer PRIMARY KEY,
	groupName text
    ); """

#stores details about user
    userTable = """
    CREATE TABLE UserTable (
	UserID integer PRIMARY KEY,
	userName text,
	NumberOfTables INTEGER,
	firstName text,
	surname text,
	password text,
	timeCreated datetime
    ); """
#chi-square distribution table
    chiSquareDistribution = """
    CREATE TABLE ChiSquare_distribution (
	df integer PRIMARY KEY,
    sig0_5 real,
	sig1 real,
	sig2_5 real,
	sig5 real,
	sig10 real,
	sig99_5 real,
	sig97_5 real,
	sig99 real,
	sig95 real,
	sig90 real
);
"""
#tables can now be run
    cursor.execute(individualTestTable)
    cursor.execute(observedFreqTable)
    cursor.execute(observedFreqColumns)
    cursor.execute(observedFreqRow)
    cursor.execute(userTable)
    cursor.execute(chiSquareDistribution)

create_database()

def query_observedValues():
    with sqlite3.connect("NEA_sqlite_create.sql"):
        cursor = db.cursor()
        observedFreqValues = """ SELECT observedFreqColumns.obFreqColID, observedFreqRow.obFreqRowID,observedFreqTable.Value
s"""


def insert_critical_values():
    with sqlite3.connect("NEA_sqlite_create.sql") as db:
        cursor = db.cursor()
        sql = """SELECT df FROM ChiSquare_distribution;"""
        cursor.execute(sql)
        result = cursor.fetchone()
        df = result[0]
        sql = "INSERT INTO chiSquare_Distribution(df, sig0_5,sig1,sig2_5,sig5,sig10)
                VALUES (?,?,?,?,?,?,?,?,?,?);"
        records = [(1,7.879,6.635,5.024,3.841,2.706,0.158,0.0039,0.001,0.001),
                    (2,10.6,9.21,7.378,5.991,4.605)(1,2.706, 3.841, 5.024, 6.635, 10.828),
 (2, 4.605, 5.991, 7.378, 9.210, 13.816),
 (3, 6.251, 7.815, 9.348, 11.345, 16.266),
 (4, 7.779, 9.488, 11.143, 13.277, 18.467),
 (5, 9.236, 11.070, 12.833, 15.086, 20.515),
 (6, 10.645, 12.592, 14.449, 16.812, 22.458),
 (7, 12.017, 14.067, 16.013, 18.475, 24.322),
 (8, 13.362, 15.507, 17.535, 20.090, 26.125),
 (9 ,14.684, 16.919, 19.023, 21.666, 27.877),
 (10, 15.987, 18.307, 20.483, 23.209, 29.588),
 (11, 17.275, 19.675, 21.920, 24.725, 31.264),
 (12, 18.549, 21.026, 23.337, 26.217, 32.910),
 (13, 19.812, 22.362, 24.736, 27.688, 34.528),
 (14, 21.064, 23.685, 26.119, 29.141, 36.123),
 (15, 22.307, 24.996, 27.488, 30.578, 37.697),
 (16, 23.542, 26.296, 28.845, 32.000, 39.252),
 (17 ,24.769, 27.587, 30.191, 33.409, 40.790),
 (18, 25.989, 28.869, 31.526, 34.805, 42.312),
 (19, 27.204, 30.144, 32.852, 36.191, 43.820),
 (20, 28.412, 31.410, 34.170, 37.566, 45.315),
 (21, 29.615, 32.671, 35.479, 38.932, 46.797),
 (22, 30.813, 33.924, 36.781, 40.289, 48.268),
 (23, 32.007, 35.172, 38.076, 41.638, 49.728),
 (24, 33.196, 36.415, 39.364, 42.980, 51.179),
 (25, 34.382, 37.652, 40.646, 44.314, 52.620),
 (26, 35.563, 38.885, 41.923, 45.642, 54.052),
 (27, 36.741, 40.113, 43.195, 46.963, 55.476),
 (28, 37.916, 41.337, 44.461, 48.278, 56.892)]
