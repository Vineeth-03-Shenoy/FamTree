import dbConnection
import FamMember

def main():
    dbConnection.connection()
    dbConnection.DBcreate()
    FamMember.relationFinder('Vin','Mom')

if __name__ =='__main__':
    main() 