class Instagram:
    def __init__(self, username,password):
        self.username=username
        self.__password=password
        self._posts=[]

    def getpassword(self):
        return self.__password

    def setpassword (self,newpassword):
        self.__password=newpassword

    @property
    def accessposts(self):
        return self._posts

    @accessposts.setter
    def accesspost(self,newpost):
        self._posts.append(newpost)

    def display(self):
        print(self.username,self.__password,self._posts)

sai= Instagram('sai','sai@13')

sai.display()
print(sai.username)
print(sai.getpassword())
print(sai.accessposts)
sai.username = 'benarji'
sai.setpassword('benarji@123')
sai.accesspost='sunrise.png'
sai.accesspost='beach.png'
sai.accesspost='temple.png'

print(sai.username)
print(sai.getpassword())
print(sai.accesspost)