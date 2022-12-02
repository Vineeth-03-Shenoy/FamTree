import dbConnection
import FamMember

def main():
    dbConnection.connection()
    dbConnection.DBcreate()
    print(FamMember.FamList('Vin','Cous'))

if __name__ =='__main__':
    main() 