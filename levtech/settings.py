# -*- coding: utf-8 -*-

# Scrapy settings for levtech project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'levtech'

SPIDER_MODULES = ['levtech.spiders']
NEWSPIDER_MODULE = 'levtech.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# ユーザーエージェントの名前
USER_AGENT = 'levtech'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# サイトへの同時リクエスト数(デフォルトは16)
# サイトへの負荷を考慮する場合は値を小さく設定する
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# リクエストごとの遅延秒数
# サイトへの負荷を考慮して設定する
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# ログの出力レベル
LOG_LEVEL = 'INFO'

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'levtech.pipelines.LevtechCsvWriterPipeline': 1,
}
