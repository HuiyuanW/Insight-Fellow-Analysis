import scrapy
from ..items import InsightfellowItem

class  FellowSpider(scrapy.Spider):
    name = 'Fellow'
    page_num = 2
    start_urls = [
        'https://www.insightdatascience.com/fellows'
    ]

    def parse(self, response):
        items = InsightfellowItem()

        all_div_Fellows = response.css('div.fellows_tooltip')

        for Fellow in all_div_Fellows:
            Name = Fellow.css('div.tooltip_name::text').extract()
            Title = Fellow.css('div.toottip_title::text').extract() 
            Company = Fellow.css('div.tooltip_company::text').extract()
            Project = Fellow.css('div.tooltip_project::text').extract()
            Background = Fellow.css('div.tooltip_background::text').extract()

            items['Name'] = Name
            items['Title'] = Title
            items['Company'] = Company
            items['Project'] = Project
            items['Background'] = Background
            
            yield items

        Next_page = 'https://www.insightdatascience.com/fellows?61ea5d1b_page=' + str(FellowSpider.page_num)

        if FellowSpider.page_num <= 8:
            FellowSpider.page_num += 1
            yield response.follow(Next_page,callback = self.parse)


        
