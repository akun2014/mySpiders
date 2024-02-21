from requests import post
import time
import requests
import json
import csv
import random
import time


class Luyahu(object):

    def __init__(self):
        self.url = 'https://shopsearch.taobao.com/search?'
        self.hearders = {
            "cookie": "thw=cn; cookie2=184dfba7061f4e5b280fa7aa297d2dd1; t=1ae9fd11828f2ea032bdd07b316bb7ba; _tb_token_=31ee66b141ba3; _samesite_flag_=true; mtop_partitioned_detect=1; hng=CN%7Czh-CN%7CCNY%7C156; xlly_s=1; _uetvid=52fbcd60b14d11ee97ed81bf39e803a2; _m_h5_tk=ad220f9e009aebd2bf9289faca1f33ed_1705850546244; _m_h5_tk_enc=0c0d8b2995edc550c4e725ee33badc62; cna=6ZYoHSqaBH4CATpkqlwy6mmU; 3PcFlag=1705846755719; sgcookie=E100j3%2Fa1TD6flZuIet10eLTjbzagKQP7JU87BMoQoMSE4KxT98jLrDl2R6rdia%2FgEfmhXSEsi6H0dDp9DovaVQhUd7hKLSFxJzNYcugngHVjmdglmfnUONKWIli4saQdT5MA039uPZu8O2FOprbWVrNYA%3D%3D; unb=925615859; uc3=nk2=EvywP7FQwiQV&vt3=F8dD3ChAyktHJiY0L3w%3D&lg2=URm48syIIVrSKA%3D%3D&id2=WvKSnFLmRjvW; csg=7975e8c3; lgc=qiankun92; cancelledSubSites=empty; cookie17=WvKSnFLmRjvW; dnk=qiankun92; skt=a369ad1454823013; existShop=MTcwNTg0Njc1OA%3D%3D; uc4=id4=0%40WDWhqC9vaJyA7Q43SY7ndr8rDFo%3D&nk4=0%40EIOda3mS%2B%2BjZGCgPtBUz4%2B9LdvU%3D; publishItemObj=Ng%3D%3D; tracknick=qiankun92; _cc_=V32FPkk%2Fhw%3D%3D; _l_g_=Ug%3D%3D; sg=299; _nk_=qiankun92; cookie1=W8nVEKDDUzw2qf7%2F0ekUyWERKQnLanMdPCS8qKihgIA%3D; mt=ci=15_1; uc1=cookie21=URm48syIZJTgsdYlwpiWOA%3D%3D&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0&cookie14=UoYekEsQ1UIAtw%3D%3D&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&existShop=false; JSESSIONID=54B2CC9E7E4D86EE0CFD243C5912A0ED; tfstk=ecgJbrXshKvoWhWamUKm8IKFURADj4hzMYl1-J2lAxHxOYwuK8AzJkMIFk_H4zqLJxwmr8cuPJ_KKX0oK2hFJWGILQyHancrayzBIdAMSblP5t5rZFx0YI6TRdvMoifb4L4Iqow7tisG6BskOa0o27t_PT_gOsl_wued--QKAq7gVR683wQLe7ERqbwARwgV4CuiW3xPIrwPVIdAYMr7gtSW66FRfCI3MRA7VMSUxSPYIIdAYMr7gSeMN7sFYkVV.; isg=BNracgqAa3gzieYqgVE3y6amK4D8C17lAnHazeRSlG04V3uRzJ3N9erlJyNLh9Z9",
            "pragma": "no-cache",
            "referer": "https://shopsearch.taobao.com/search?q=%E5%8D%A4%E9%B8%AD%E8%B4%A7&js=1&initiative_id=staobaoz_20230303&ie=utf8&s=20",
            "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "script",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }

    def get_data(self, params):
        response = requests.get(url=self.url, params=params, headers=self.hearders)

        print(response.json())
        return response.json()

    def paras_data(self, response):
        # with open('淘宝卤鸭货.csv', 'a', encoding='utf-8', newline='') as f:
        #     file_name = ['店铺名称', '好评率', '荣誉等级', '动态评分_描述相符', '动态评分_描述相符同行业相比',
        #                  '动态评分_服务态度', '动态评分_服务态度同行业相比', '动态评分_物流服务',
        #                  '动态评分_物流服务同行业相比']
        #     writer = csv.DictWriter(f,file_name)
        #     # writer.writeheader()

        data_list = response['mods']['shoplist']['data']['shopItems']
        for i in data_list:
            item = {}
            item['店铺名称'] = i['title']
            if 'goodratePercent' in i:
                item['好评率'] = i['goodratePercent']
            else:
                item['好评率'] = '无'
            item['荣誉等级'] = i['shopIcon']['iconClass'].split('-')[2]
            Dynamic_scoring_dict = json.loads(i['dsrInfo']['dsrStr'])
            item['动态评分_描述相符'] = Dynamic_scoring_dict['mas']
            if float(Dynamic_scoring_dict['mg'].strip('%')) / 100 >= 0:

                item['动态评分_描述相符同行业相比'] = '高于' + Dynamic_scoring_dict['mg']
            else:
                item['动态评分_描述相符同行业相比'] = '低于' + Dynamic_scoring_dict['mg']
            item['动态评分_服务态度'] = Dynamic_scoring_dict['sas']
            if float(Dynamic_scoring_dict['cas'].strip('%')) / 100 >= 0:
                item['动态评分_服务态度同行业相比'] = '高于' + Dynamic_scoring_dict['cas']
            else:
                item['动态评分_服务态度同行业相比'] = '低于' + Dynamic_scoring_dict['cas']
            item['动态评分_物流服务'] = Dynamic_scoring_dict['mas']
            if float(Dynamic_scoring_dict['cg'].strip('%')) / 100 >= 0:
                item['动态评分_物流服务同行业相比'] = '高于' + Dynamic_scoring_dict['cg']
            else:
                item['动态评分_物流服务同行业相比'] = '低于' + Dynamic_scoring_dict['cg']
            # print(Dynamic_scoring_dict)
            print(item)

            yield item

    def get_totalPage(self):
        params = {
            "data-key": "s",
            "data-value": 0,
            "ajax": "true",
            "_ksTS": "1677832873316_506",
            # "callback": "jsonp507",
            "q": "卤鸭货",
            "js": "1",
            "initiative_id": "staobaoz_20230304",
            "ie": "utf8",
            "s": 0
        }
        res = requests.get(url=self.url, params=params, headers=self.hearders).json()
        print(res)
        totalPage = res['mods']['pager']['data']['totalPage']
        return totalPage

    def main(self):
        page = int(self.get_totalPage())
        with open('淘宝卤鸭货.csv', 'a', encoding='utf-8', newline='') as f:
            file_name = ['店铺名称', '好评率', '荣誉等级', '动态评分_描述相符', '动态评分_描述相符同行业相比',
                         '动态评分_服务态度', '动态评分_服务态度同行业相比', '动态评分_物流服务',
                         '动态评分_物流服务同行业相比']
            writer = csv.DictWriter(f, fieldnames=file_name)
            writer.writeheader()

            for i in range(0, page):
                params = {
                    "data-key": "s",
                    "data-value": i * 20,
                    "ajax": "true",
                    "_ksTS": "1677832873316_506",
                    # "callback": "jsonp507",
                    "q": "卤鸭货",
                    "js": "1",
                    "initiative_id": "staobaoz_20230304",
                    "ie": "utf8",
                    "s": i * 20
                }
                print('正在抓取第{}页数据'.format(i))
                response = self.get_data(params)
                res = self.paras_data(response)
                writer.writerows(res)
                time.sleep(round(random.uniform(2, 5), 3))
            print('数据抓取已完成')


if __name__ == '__main__':
    l = Luyahu()
    # l.get_totalPage()
    l.main()
