class Excercise_Oops:

    def __init__ (self):
        print ("Inside a constructer.....!!")

    def getProductName(self, CategoryName):
        print("Inside getProductName...!!!")
        #product=["a","b"]
        product=[]
        for i in range(1,6):
            name=("product_"+CategoryName+ "_" +str(i))
            product.append(name)
        return product

    def getCategoryName(self, CategoryName):
        print("Inside getCategoryName...!!")
        category={}
        category["Electronics"]=self.getProductName("Electronics")
        return category

    def getEommSiteName(self, *args):
        print("Inside getEommSiteName")
        sites={}
        sites["Myntra"]=self.getCategoryName("Myntra")
        return sites


if __name__ == "__main__":
    a=Excercise_Oops()
    data=a.getEommSiteName("Myntra")
    print (data)
