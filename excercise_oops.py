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

    def getCategoryName(self, *args):
        print("Inside getCategoryName...!!")
        category={}
        for CategoryName in args:
            #to get prodcut for each category
            category[CategoryName]=self.getProductName(CategoryName)
        return category

    def getEommSiteName(self, *args):
        print("Inside getEommSiteName")
        sites={}
        #sites["Myntra"]=self.getCategoryName("Myntra")
        for site in args:
            #print(site)
            #sites[site]=self.getCategoryName(site)
            sites[site]=self.getCategoryName("Electronics", "Books", "Automobile")

        return sites


if __name__ == "__main__":
    a=Excercise_Oops()
    data=a.getEommSiteName("Myntra", "Flipkart", "Jobong")
    #Excercise_Oops.printData(data)
    #print (data)
    #@staticmethod
    #def printData(data):
    
    for i in data:
        aa = data[i]
        #print (aa)
        for item in aa:
            #print (type(aa[item]))
            bb = aa[item]
            #print (bb)
            for prodcut in bb:
                print (i + "--- " + item + "-" + "-"+prodcut)
