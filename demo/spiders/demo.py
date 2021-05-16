import scrapy
from scrapy_splash import SplashRequest
import csv


class Demo2Spider(scrapy.Spider):
    name = 'demo2'
    domain = "https://www.ncbi.nlm.nih.gov/nuccore/"

    f = open("//data/data.csv", 'a+')
    writer = csv.writer(f)


    def start_requests(self):

        urls = [
            'MED16',
            'POLR2E',
            'C19orf25',
            # 'NCLN',
            # 'CELF5',
            # 'CACTIN',
            # 'ZFR2',
            # 'SLC25A23',
            # 'MAP2K7',
            # 'NPPA-AS1',
            # 'BX647356',
            # 'DKFZp547H118',
            # 'DNM2',
            # 'CTC-510F12.4',
            # 'AX747599',
            # 'ZNF625',
            # 'ZNF44',
            # 'FBXW9',
            # 'BABAM1',
            # 'KIAA1683',
            # 'HOMER3',
            # 'NR2C2AP',
            # 'ZNF506',
            # 'SRP9',
            # 'ZNF253',
            # 'ZNF90',
            # 'AX746719',
            # 'BC038574',
            # 'CTD-2540B15.13',
            # 'AX747741',
            # 'HSPB6',
            # 'ZNF678',
            # 'MIA-RAB4B',
            # 'RAB4B',
            # 'CEACAM1',
            # 'PSG3',
            # 'PSG1',
            # 'ZNF284',
            # 'ZNF235',
            # 'APOC2',
            # 'ERCC2',
            # 'AX747088',
            # 'SIGLEC8',
            # 'AF086165',
            # 'ZNF808',
            # 'ZNF813',
            # 'LILRB3',
            # 'LILRA6',
            # 'KIAA1932',
            # 'KIR2DS4',
            # 'FCAR',
            # 'RDH13',
            # 'COX6B2',
            # 'TSNAX-DISC1',
            # 'DISC1',
            # 'ZNF470',
            # 'ZNF530',
            # 'AX721128',
            # 'ZNF586',
            # 'ZNF587',
            # 'DL490846',
            # 'ZNF418',
            # 'ZNF329',
            # 'ZNF8',
            # 'SLC27A5',
            # 'DQ588114',
            # 'RASSF2',
            # 'TASP1',
            # 'AX747264',
            # 'NAPB',
            # 'C20orf203',
            # 'AL122050',
            # 'EIF6',
            # 'AK128252',
            # 'C20orf173',
            # 'AX747164',
            # 'AK098303',
            # 'PABPC1L'
        ]
        for url in urls:
            yield scrapy.Request(url=Demo2Spider.domain + url, meta={'name': url}, callback=self.parse)

    def parse(self, response):
        hrefs = response.xpath('//*[@id="ReportShortCut6"]/@href').extract()
        meta_name = response.meta['name']
        new_url = "https://www.ncbi.nlm.nih.gov"
        yield SplashRequest(new_url + hrefs[0], meta={'name': meta_name}, callback=self.parse2)

        # pass

    def parse2(self, response):
        texts = response.xpath('//*[@id="viewercontent1"]/pre/text()').extract()
        meta_name = response.meta['name']
        for text in texts:
            print(meta_name + "\t ==> \t" + text)
            new_text = text.replace("\n", "")
            Demo2Spider.writer.writerow((meta_name, new_text))
            break

