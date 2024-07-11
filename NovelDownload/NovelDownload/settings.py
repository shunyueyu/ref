# Scrapy settings for NovelDownload project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "NovelDownload"

SPIDER_MODULES = ["NovelDownload.spiders"]
NEWSPIDER_MODULE = "NovelDownload.spiders"

HTTPERROR_ALLOWED_CODES = [403]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    ":authority":"www.bqbi.cc",
#    ":method":"GET",
#    ":path":"/book/388/1.html",
#     ":scheme":"https",
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#    "Accept-Encoding": "gzip, deflate, br, zstd",
#    "Accept-Language": "ja,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6",
#    "Cache-Control":"max-age=0",
#     "Cookie":"Hm_lvt_52624d0257fe48ed9dea61ff01fa3417=1720683328; HMACCOUNT=0B577EDE0AEB3230; Hm_lpvt_52624d0257fe48ed9dea61ff01fa3417=1720683334",
#    "If-Modified-Since": "Tue, 19 Mar 2024 03:00:54 +0000",
#    #"If-None-Match": "1720664223_br",
#    "Priority":"u=0, i",
#    "Referer":"https://wap.bqbwx.cc/53/53190_10/",
#    "Sec-Ch-Ua":'Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24',
#    "Sec-Ch-Ua-Mobile":"?0",
#    "Sec-Ch-Ua-Platform":"Windows",
#    "Sec-Fetch-Dest":"document",
#    "Sec-Fetch-Mode":"navigate",
#    "Sec-Fetch-Site":"same-origin",
#    "Sec-Fetch-User":"?1",
#    "Upgrade-Insecure-Requests":"1",
#    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
# }

# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#    "Accept-Encoding": "gzip, deflate, br, zstd",
#    "Accept-Language": "ja,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6",
#    "Cache-Control":"max-age=0",
#     "Host":"www.26ks.cc",
#    "Proxy-Connection":"keep-alive",
#    "Referer":"http://www.26ks.cc/book/24023/",
#    "Upgrade-Insecure-Requests":'1',
#    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
# }
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "NovelDownload.middlewares.NoveldownloadSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "NovelDownload.middlewares.NoveldownloadDownloaderMiddleware": 543,
# }
# DOWNLOADER_MIDDLEWARES = {
#         'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#         'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
#         'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
#         'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
# }
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "NovelDownload.pipelines.NoveldownloadPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# 配置日志
LOG_ENABLED = False  # 开启日志

LOG_LEVEL = 'DEBUG'  # 设置日志级别。例如，要将日志级别设置为输出所有信息，可以这样配置：通过将日志级别设置为 DEBUG，你可以获取爬虫程序执行过程中的所有详细信息，包括请求、响应、数据处理等各个环节的日志输出。当然，如果你只想获取部分信息，比如只关注警告和错误信息，也可以将日志级别设置为 WARNING 或 ERROR。在运行爬虫时，Scrapy 默认会将日志输出到控制台。如果你希望将日志保存到文件中，还可以设置 LOG_FILE 配置选项，例如：

LOG_FILE = 'scrapy.log'  # 设置日志文件名字 上述配置会将日志输出到名为 scrapy.log 的文件中。