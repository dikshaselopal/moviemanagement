def movie():
    userinput1=input("enter the movie name")
    userinput2 = input("enter the release date")
    userinput3 = input("enter the rating")
    return [userinput1,userinput2,userinput3]
def add():
    print("press A to add \n press V to view \n press e to exit")
    movielist=[]
    #movielist.extend(movie())
    #data()
    flag=True
    while flag:
        userchoice=input("enter your choice")
        if(userchoice=='a' or userchoice=='A'):
            movielist.extend(movie())
            data(movielist)
        elif(userchoice=='v' or userchoice=='V'):
            movieList = data1()
            print(movieList)
        else:
            print("thank you")
def data(movielist):
    fopen =open("movielist.txt",'a')

    data =fopen.write(str(movielist))
    fopen.close()
    return data
def data1():
    fopen =open("movielist.txt",'r')
    data =fopen.read()
    fopen.close()
    return data




