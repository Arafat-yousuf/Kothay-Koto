import scrapy
from bs4 import BeautifulSoup
import re
from KothayKoto.items import StartechItem


class StartechSpider(scrapy.Spider):
    name = 'StartechSpider'
    allowed_domains = ['startech.com.bd']
    start_urls = ['https://www.startech.com.bd/']

    def __init__(self):
        self.declare_xpath()

        #All the XPaths the spider needs to know go here
    def declare_xpath(self):
        self.getAllCategoriesXpath = '//*[@id="main-nav"]/div/ul/li/a/@href'
        self.getAllSubCategoriesXpath = '//*[@id="main-nav"]/div/ul/li/ul/li/a/@href'
        self.getAllSubSubCategoriesXpath = '//*[@id="main-nav"]/div/ul/li/ul/li/ul/li/a/@href'
        self.getAllPagesXpath = '//*[@id="content"]/div[3]/div/div[1]/ul/li/a/@href'
        self.getAllItemsXpath = '//*[@id="content"]/div[2]/div/div/div[2]/h4/a/@href'
        self.TitleXpath  = '//*[@id="product"]/div/div[1]/h1/text()'
        self.CategoryXpath = '/html/body/section/div/ul/li[2]/a/span/text()'
        self.PriceXpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "product-price", " " ))]/text()'
        self.DescriptionXpath = '//*[@id="description"]/div[2]/p/text()'
        # self.SpecsXpath = ''
        self.StatusXpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "product-status", " " ))]/text()'
        self.ImageXpath = '/html/body/div[5]/div[1]/div/div[2]/div[1]/div/div/a/img/@src'
        self.LinkXpath = '/html/body/section/div/ul/li/a/@href'

    def parse(self, response):
        for href in response.xpath(self.getAllCategoriesXpath):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url=url,callback=self.parse_category)
 
    def parse_category(self,response):
        for href in response.xpath(self.getAllSubCategoriesXpath):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url,callback=self.parse_subcategory)
            yield scrapy.Request(url,callback=self.parse_subsubcategory)

    def parse_subcategory(self,response):
        for href in response.xpath(self.getAllSubSubCategoriesXpath):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url,callback=self.parse_subsubcategory)
        
        # if bool(next_text) is not False and next_text[-1] == 'NEXT':
        #     next_url = response.xpath('//*[@id="content"]/div[3]/div/div[1]/ul/li/a/@href').getall()
        #     yield scrapy.Request(response.urljoin(next_url[-1]))

    
    def parse_subsubcategory(self,response):
        for href in response.xpath(self.getAllItemsXpath):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url,callback=self.parse_main_item)
        for href in response.xpath(self.getAllPagesXpath):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url,callback=self.parse_subsubcategory)

    
    def parse_main_item(self,response):
        item = StartechItem()
 
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