import scrapy
from bs4 import BeautifulSoup
import re
from KothayKoto.items import TechlandItem


class TechlandSpider(scrapy.Spider):
    name = 'TechlandSpider'
    allowed_domains = ['techlandbd.com']
    start_urls = ['https://www.techlandbd.com/']

    def __init__(self):
        self.declare_xpath()

        #All the XPaths the spider needs to know go here
    def declare_xpath(self):
        self.getAllCategoriesXpath = '//*[@class="flyout-menu flyout-menu-7"]/ul/li/a/@href'
        # self.getAllSubCategoriesXpath = '//*[@class="dropdown-menu j-dropdown "]/ul/li/a/@href'
        # self.getAllSubSubCategoriesXpath ='//*[@class="dropdown-menu j-dropdown "]/ul/li/div/ul/li/a/@href' 
        # self.getAllSubSubSubCategoriesXpath = '//*[@class="dropdown-menu j-dropdown "]/ul/li/div/ul/li/div/ul/li/a/@href'
        # self.getAllPagesXpath = '//*[@id="content"]/div[2]/div[3]/div[1]/ul/li[2]/a/@href'
        self.getAllPagesXpath = '//*[@class="pagination"]/li/a/@href'
        # self.getAllItemsXpath = '//*[@id="content"]/div[2]/div[2]/div/div/div[2]/div[2]/a/@href'
        self.getAllItemsXpath = '//*[@class="main-products product-grid"]/div[1]/div/div[2]/div[2]/a/@href'
        self.TitleXpath  = '//*[@id="product"]/div[1]/text()'
        self.CategoryXpath = '/html/body/div[4]/ul/li[2]/a/text()'
        self.PriceXpath = '//*[@id="product"]/div[5]/div/div/div/text()'
        self.DescriptionXpath = '//*[@id="content"]/div[1]/div[1]/div[3]/div[2]/div[2]/div/div/div/p[2]/text()'
        # self.SpecsXpath = ''
        self.StatusXpath = '//*[@class="product-stats"]/ul/li[1]/span/text()'
        self.ImageXpath = '//*[@id="content"]/div[1]/div[1]/div[1]/div[1]/div[1]/div/div[1]/img/@src'
        self.LinkXpath = '/html/body/div[4]/ul/li/a/@href'

    def parse(self, response):
        for href in response.xpath(self.getAllCategoriesXpath):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url=url,callback=self.parse_allitems)
 
    # def parse_category(self,response):
    #     for href in response.xpath(self.getAllSubCategoriesXpath):
    #         url = response.urljoin(href.extract())
    #         yield scrapy.Request(url,callback=self.parse_subcategory)
    #         yield scrapy.Request(url,callback=self.parse_subsubsubcategory)

    # def parse_subcategory(self,response):
    #     for href in response.xpath(self.getAllSubSubCategoriesXpath):
    #         url = response.urljoin(href.extract())
    #         yield scrapy.Request(url,callback=self.parse_subsubsubcategory)
    #         yield scrapy.Request(url,callback=self.parse_subsubcategory)
            

    # def parse_subsubcategory(self,response):
    #     for href in response.xpath(self.getAllSubSubSubCategoriesXpath):
    #         url = response.urljoin(href.extract())
    #         yield scrapy.Request(url,callback=self.parse_subsubsubcategory)
    
    # def parse_subsubsubcategory(self,response):
    #     for href in response.xpath(self.getAllItemsXpath):
    #         url = response.urljoin(href.extract())
    #         yield scrapy.Request(url,callback=self.parse_main_item)
    #     for href in response.xpath(self.getAllPagesXpath):
    #         url = response.urljoin(href.extract())
    #         yield scrapy.Request(url,callback=self.parse_subsubsubcategory)

    def parse_allitems(self,response):
        for href in response.xpath(self.getAllItemsXpath):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url,callback=self.parse_main_item)
        for href in response.xpath(self.getAllPagesXpath):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url,callback=self.parse_allitems)




    def parse_main_item(self,response):
        item = TechlandItem()
 
        Title = response.xpath(self.TitleXpath).extract_first()
        if Title is not None:
            Title = self.cleanText(self.parseText(Title))
        else:
            Title = 'N/A'
 
        Category = response.xpath(self.CategoryXpath).extract_first()
        if Category is not None:
            Category = self.cleanText(self.parseText(Category))
        else:
            Category = 'N/A'

        Price = response.xpath(self.PriceXpath).extract_first()
        if Price is not None:
            Price = self.cleanText(self.parseText(self.keepDigit(Price)))
        else:
            Price = 'nan'


        Description = response.xpath(self.DescriptionXpath).extract_first()
        if Description is not None:
            Description = self.cleanText(self.parseText(Description))
        else:
            Description = 'N/A'
        # Specs = response.xpath(self.SpecsXpath).extract()
        # Specs = self.cleanText(self.parseText(Specs))

        Status = response.xpath(self.StatusXpath).extract_first()
        if Status is not None:
            Status = self.cleanText(self.parseText(Status))
        else:
            Status = 'N/A'
        
        Image = response.xpath(self.ImageXpath).extract_first()
        if Image is not None:
            Image = Image
        else:
            Image = 'N/A'

        Link = response.xpath(self.LinkXpath).extract()
        if Link is not None:
            Link = Link[-1]
        else:
            Link = 'N/A'

        #Put each element into its item attribute.
        item['Title']           = Title
        item['Category']        = Category
        item['Price']           = Price
        item['Description']     = Description
        # item['Specs']           = Specs
        item['Status']          = Status
        item['Image']           = Image
        item['Link']            = Link
        
        return item
 
    #Methods to clean and format text to make it easier to work with later
    def listToStr(self,MyList):
        dumm = ""
        MyList = [i.encode('utf-8') for i in MyList]
        for i in MyList:dumm = "{0}{1}".format(dumm,i)
        return dumm
 
    def parseText(self, str):
        soup = BeautifulSoup(str, 'html.parser')
        return re.sub(" +|\n|\r|\t|\0|\x0b|\xa0",' ',soup.get_text()).strip()

    def keepDigit(self, str):
        soup = BeautifulSoup(str, 'html.parser')
        return re.sub("[^0-9]",'',soup.get_text()).strip()
 
    def cleanText(self,text):
        soup = BeautifulSoup(text,'html.parser')
        text = soup.get_text()
        text = re.sub("( +|\n|\r|\t|\0|\x0b|\xa0|\xbb|\xab)+",' ',text).strip()
        return text