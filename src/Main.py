import dbConnection
import FamMember

def main():
    dbConnection.connection()
    dbConnection.DBcreate()
    FamMember.fam_MemberTable()
    FamMember.FM_Insert()
    #FamMember.relationFinder('Vin','PgD')

if __name__ =='__main__':
    main() 