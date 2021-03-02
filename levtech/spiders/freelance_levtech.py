import scrapy
import bs4
from levtech.items import LevtechItem


class FreelanceLevtechSpider(scrapy.Spider):
    name = 'freelance-levtech'
    allowed_domains = ['freelance.levtech.jp']
    start_urls = ['http://freelance.levtech.jp/project/search']

    def parse(self, response):
        fee = ''
        job_content = ''
        # nearest_station = ''
        # prefecture = ''
        # job_title = ''
        # development_enviroment = ''
        # required_skill = ''

        soup = bs4.BeautifulSoup(response.body, 'html.parser')
        prjs = soup.findAll(
            name='div',
            attrs={'class': 'prjContent'}
        )

        for prj in prjs:

            if prj.select('li.prjContent__summary__price'):
                fee = prj.select('li.prjContent__summary__price')[0].span. get_text()
            
            items = prj.select('li.prjTable__item')
            job_content_block = list(filter(
                lambda i: i.select('p.prjTable__item__ttl')[0].get_text() == '募集職種', items))
            if job_content_block:
                job_content = job_content_block[0].\
                    select('p.prjTable__item__desc')[0].get_text().replace('\n', '')

            yield LevtechItem(
                fee=fee,
                job_content=job_content
            )
        
        # ページネーションの「次ページ」へのリンクを取得し、再起的にクローリングする
        next_page = response.css('a[rel="next"]').css('a::attr(href)').extract
        if next_page:
            print(f'crawling: https://freelance/levtech.jp{next_page}')
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

