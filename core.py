# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import model
import time
import datetime
import urllib2
import logging
import tushare as ts
import sys
from peewee import *

reload(sys);
sys.setdefaultencoding("utf8")

ts.set_token('57ff0a5d603b5d0eebfa48bca30fa45d034fd4aa8df49f77c64cdc4e')

pro = ts.pro_api()
pro = ts.pro_api('57ff0a5d603b5d0eebfa48bca30fa45d034fd4aa8df49f77c64cdc4e')

TODAY = time.strftime('%Y%m%d', time.localtime(time.time()))


def GetBasicStock():
    info = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
    data_source = []
    for EachStockID in info.index:
        dict_stcok = {}
        dict_stcok.update({u'ts_code': info.ix[EachStockID]['ts_code']})
        dict_stcok.update({u'symbol': info.ix[EachStockID]['symbol']})
        dict_stcok.update({u'name': info.ix[EachStockID]['name']})
        dict_stcok.update({u'area': info.ix[EachStockID]['area']})
        dict_stcok.update({u'industry': info.ix[EachStockID]['industry']})
        dict_stcok.update({u'fullname': info.ix[EachStockID]['fullname']})
        dict_stcok.update({u'enname': info.ix[EachStockID]['enname']})
        dict_stcok.update({u'market': info.ix[EachStockID]['market']})
        dict_stcok.update({u'exchange': info.ix[EachStockID]['exchange']})
        dict_stcok.update({u'curr_type': info.ix[EachStockID]['curr_type']})
        dict_stcok.update({u'list_status': info.ix[EachStockID]['list_status']})
        dict_stcok.update({u'list_date': info.ix[EachStockID]['list_date']})
        dict_stcok.update({u'delist_date': info.ix[EachStockID]['delist_date']})
        dict_stcok.update({u'is_hs': info.ix[EachStockID]['is_hs']})
        data_source.append(dict_stcok)
    with model.database.atomic():
        if data_source:
            model.StockBasic.insert_many(data_source).upsert().execute()

def GetDaily():
    # 获取所有股票
    stocks = model.StockBasic.select()
    for stock in stocks:
        data_source = []
        info = pro.daily(ts_code=stock.ts_code, start_date='20200708', end_date=TODAY)
        for EachStockID in info.index:
            dict_stcok = {}
            dict_stcok.update({u'ts_code': info.ix[EachStockID]['ts_code']})
            dict_stcok.update({u'trade_date': info.ix[EachStockID]['trade_date']})
            dict_stcok.update({u'open': info.ix[EachStockID]['open']})
            dict_stcok.update({u'high': info.ix[EachStockID]['high']})
            dict_stcok.update({u'low': info.ix[EachStockID]['low']})
            dict_stcok.update({u'close': info.ix[EachStockID]['close']})
            dict_stcok.update({u'pre_close': info.ix[EachStockID]['pre_close']})
            dict_stcok.update({u'change': info.ix[EachStockID]['change']})
            dict_stcok.update({u'pct_chg': info.ix[EachStockID]['pct_chg']})
            dict_stcok.update({u'vol': info.ix[EachStockID]['vol']})
            dict_stcok.update({u'amount': info.ix[EachStockID]['amount']})

            data_source.append(dict_stcok)

        with model.database.atomic():
            if data_source:
                model.Daily.insert_many(data_source).upsert().execute()

def GetDailyBasic():
    # 每日指标
    stocks = model.StockBasic.select()
    for stock in stocks:
        data_source = []
        try:
            info = pro.daily_basic(ts_code=stock.ts_code, start_date='20200710', end_date=TODAY)
        except Exception as e:
            print(e)

        for EachStockID in info.index:
            dict_stcok = {}
            dict_stcok.update({u'ts_code': info.ix[EachStockID]['ts_code']})
            dict_stcok.update({u'trade_date': info.ix[EachStockID]['trade_date']})
            dict_stcok.update({u'close': info.ix[EachStockID]['close']})
            dict_stcok.update({u'turnover_rate': info.ix[EachStockID]['turnover_rate']})
            dict_stcok.update({u'turnover_rate_f': info.ix[EachStockID]['turnover_rate_f']})
            dict_stcok.update({u'volume_ratio': info.ix[EachStockID]['volume_ratio']})
            dict_stcok.update({u'pe': info.ix[EachStockID]['pe']})
            dict_stcok.update({u'pe_ttm': info.ix[EachStockID]['pe_ttm']})
            dict_stcok.update({u'pb': info.ix[EachStockID]['pb']})
            dict_stcok.update({u'ps': info.ix[EachStockID]['ps']})
            dict_stcok.update({u'ps_ttm': info.ix[EachStockID]['ps_ttm']})
            dict_stcok.update({u'dv_ratio': info.ix[EachStockID]['dv_ratio']})
            dict_stcok.update({u'dv_ttm': info.ix[EachStockID]['dv_ttm']})
            dict_stcok.update({u'total_share': info.ix[EachStockID]['total_share']})
            dict_stcok.update({u'float_share': info.ix[EachStockID]['float_share']})
            dict_stcok.update({u'free_share': info.ix[EachStockID]['free_share']})
            dict_stcok.update({u'total_mv': info.ix[EachStockID]['total_mv']})
            dict_stcok.update({u'circ_mv': info.ix[EachStockID]['circ_mv']})

            data_source.append(dict_stcok)

        with model.database.atomic():
            if data_source:
                model.DailyBasic.insert_many(data_source).upsert().execute()

        time.sleep(0.3)

# 获取最近一段时间的涨幅



def GetDailyPool():
    # 获取所有股票
    stocks = model.StockPool.select()
    for stock in stocks:
        data_source = []
        info = pro.daily(ts_code=stock.ts_code, start_date='19910403', end_date=TODAY)
        for EachStockID in info.index:
            dict_stcok = {}
            dict_stcok.update({u'ts_code': info.ix[EachStockID]['ts_code']})
            dict_stcok.update({u'trade_date': info.ix[EachStockID]['trade_date']})
            dict_stcok.update({u'open': info.ix[EachStockID]['open']})
            dict_stcok.update({u'high': info.ix[EachStockID]['high']})
            dict_stcok.update({u'low': info.ix[EachStockID]['low']})
            dict_stcok.update({u'close': info.ix[EachStockID]['close']})
            dict_stcok.update({u'pre_close': info.ix[EachStockID]['pre_close']})
            dict_stcok.update({u'change': info.ix[EachStockID]['change']})
            dict_stcok.update({u'pct_chg': info.ix[EachStockID]['pct_chg']})
            dict_stcok.update({u'vol': info.ix[EachStockID]['vol']})
            dict_stcok.update({u'amount': info.ix[EachStockID]['amount']})

            data_source.append(dict_stcok)

        with model.database.atomic():
            if data_source:
                model.DailyPool.insert_many(data_source).upsert().execute()

def GetDailyBasicPool():
    # 每日指标
    stocks = model.StockPool.select()
    for stock in stocks:
        data_source = []
        try:
            info = pro.daily_basic(ts_code=stock.ts_code, start_date='20200812', end_date=TODAY)
        except Exception as e:
            print(e)

        for EachStockID in info.index:
            dict_stcok = {}
            dict_stcok.update({u'ts_code': info.ix[EachStockID]['ts_code']})
            dict_stcok.update({u'uuid': info.ix[EachStockID]['ts_code']+info.ix[EachStockID]['trade_date']})
            dict_stcok.update({u'trade_date': info.ix[EachStockID]['trade_date']})
            dict_stcok.update({u'close': info.ix[EachStockID]['close']})
            dict_stcok.update({u'turnover_rate': info.ix[EachStockID]['turnover_rate']})
            dict_stcok.update({u'turnover_rate_f': info.ix[EachStockID]['turnover_rate_f']})
            dict_stcok.update({u'volume_ratio': info.ix[EachStockID]['volume_ratio']})
            dict_stcok.update({u'pe': info.ix[EachStockID]['pe']})
            dict_stcok.update({u'pe_ttm': info.ix[EachStockID]['pe_ttm']})
            dict_stcok.update({u'pb': info.ix[EachStockID]['pb']})
            dict_stcok.update({u'ps': info.ix[EachStockID]['ps']})
            dict_stcok.update({u'ps_ttm': info.ix[EachStockID]['ps_ttm']})
            dict_stcok.update({u'dv_ratio': info.ix[EachStockID]['dv_ratio']})
            dict_stcok.update({u'dv_ttm': info.ix[EachStockID]['dv_ttm']})
            dict_stcok.update({u'total_share': info.ix[EachStockID]['total_share']})
            dict_stcok.update({u'float_share': info.ix[EachStockID]['float_share']})
            dict_stcok.update({u'free_share': info.ix[EachStockID]['free_share']})
            dict_stcok.update({u'total_mv': info.ix[EachStockID]['total_mv']})
            dict_stcok.update({u'circ_mv': info.ix[EachStockID]['circ_mv']})

            data_source.append(dict_stcok)

        with model.database.atomic():
            if data_source:
                model.DailyBasicPool.insert_many(data_source).upsert().execute()

        time.sleep(0.3)

#复权因子
def GetAdjFactor():
    # 获取所有股票
    stocks = model.StockBasic.select()
    for stock in stocks:
        data_source = []
        info = pro.adj_factor(ts_code=stock.ts_code, start_date='19940617', end_date=TODAY)
        for EachStockID in info.index:
            dict_stcok = {}
            dict_stcok.update({u'ts_code': info.ix[EachStockID]['ts_code']})
            dict_stcok.update({u'uuid': info.ix[EachStockID]['ts_code'] + info.ix[EachStockID]['trade_date']})
            dict_stcok.update({u'trade_date': info.ix[EachStockID]['trade_date']})
            dict_stcok.update({u'adj_factor': info.ix[EachStockID]['adj_factor']})
            data_source.append(dict_stcok)

        with model.database.atomic():
            if data_source:
                model.AdjFactor.insert_many(data_source).upsert().execute()
def GetAdjFactor2():
    # 获取所有股票
    stocks = model.StockBasic.select()
    for stock in stocks:
        data_source = []
        info = pro.adj_factor(ts_code=stock.ts_code, start_date='20100101', end_date=TODAY)
        for EachStockID in info.index:
            dict_stcok = {}
            dict_stcok.update({u'ts_code': info.ix[EachStockID]['ts_code']})
            dict_stcok.update({u'uuid': info.ix[EachStockID]['ts_code'] + info.ix[EachStockID]['trade_date']})
            dict_stcok.update({u'trade_date': info.ix[EachStockID]['trade_date']})
            dict_stcok.update({u'adj_factor': info.ix[EachStockID]['adj_factor']})
            data_source.append(dict_stcok)

        with model.database.atomic():
            if data_source:
                model.AdjFactor2.insert_many(data_source).upsert().execute()

#获取复权后的值
def GetProBar():
    # 获取所有股票
    stocks = model.StockBasic.select()
    for stock in stocks:
        data_source = []
        info = pro.adj_factor(ts_code=stock.ts_code, adj='qfq', start_date='19910403', end_date=TODAY)
        print(info)

        for EachStockID in info.index:
            dict_stcok = {}
            dict_stcok.update({u'ts_code': info.ix[EachStockID]['ts_code']})
            dict_stcok.update({u'trade_date': info.ix[EachStockID]['trade_date']})
            dict_stcok.update({u'adj_factor': info.ix[EachStockID]['adj_factor']})
            data_source.append(dict_stcok)


        # with model.database.atomic():
        #     if data_source:
        #         model.AdjFactor.insert_many(data_source).upsert().execute()

# 获取最近一段时间的涨幅

def GetIncom():
    df = pro.income(ts_code='600000.SH', start_date='20000101', end_date='20200730',
                    fields='ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,basic_eps,diluted_eps,operate_profit,n_income')
    print(df)

# 业绩预告
def GetForecast():
    df = pro.income(ts_code='600000.SH', start_date='20000101', end_date=TODAY,
                    fields='ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,basic_eps,diluted_eps,operate_profit,n_income')
# 业绩快报
def GetExpress():
    # 获取所有股票
    stocks = model.StockPool.select()
    for stock in stocks:
        data_source = []
        try:
            info = pro.express(ts_code=stock.ts_code, start_date='19900101', end_date=TODAY,
                               fields='ts_code,ann_date,end_date,revenue,operate_profit,total_profit,n_income,total_assets,'
                                      'total_hldr_eqy_exc_min_int,diluted_eps,diluted_roe,yoy_net_profit,bps,yoy_sales,yoy_op,yoy_tp,'
                                      'yoy_dedu_np,yoy_eps,yoy_roe,growth_assets,yoy_equity,growth_bps,or_last_year,op_last_year,'
                                      'tp_last_year,np_last_year,eps_last_year,open_net_assets,open_bps,perf_summary,is_audit,remark')
        except Exception as e:
            print(e)
        for EachStockID in info.index:
            dict_stcok = {}
            # print(get_value(info.ix[EachStockID]['yoy_sales']))
            # return
            dict_stcok.update({u'ts_code': get_value(info.ix[EachStockID]['ts_code'])})
            dict_stcok.update({u'uuid':  get_value(info.ix[EachStockID]['ts_code'] + info.ix[EachStockID]['ann_date'])})
            dict_stcok.update({u'ann_date':  get_value(info.ix[EachStockID]['ann_date'])})
            dict_stcok.update({u'end_date':  get_value(info.ix[EachStockID]['end_date'])})
            dict_stcok.update({u'revenue':  get_value(info.ix[EachStockID]['revenue'])})
            dict_stcok.update({u'operate_profit':  get_value(info.ix[EachStockID]['operate_profit'])})
            dict_stcok.update({u'total_profit':  get_value(info.ix[EachStockID]['total_profit'])})
            dict_stcok.update({u'n_income':  get_value(info.ix[EachStockID]['n_income'])})
            dict_stcok.update({u'total_assets':  get_value(info.ix[EachStockID]['total_assets'])})
            dict_stcok.update({u'total_hldr_eqy_exc_min_int':  get_value(info.ix[EachStockID]['total_hldr_eqy_exc_min_int'])})
            dict_stcok.update({u'diluted_eps':  get_value(info.ix[EachStockID]['diluted_eps'])})
            dict_stcok.update({u'diluted_roe':  get_value(info.ix[EachStockID]['diluted_roe'])})
            dict_stcok.update({u'yoy_net_profit':  get_value(info.ix[EachStockID]['yoy_net_profit'])})
            dict_stcok.update({u'bps':  get_value(info.ix[EachStockID]['bps'])})
            dict_stcok.update({u'yoy_sales':  get_value(info.ix[EachStockID]['yoy_sales'])})
            dict_stcok.update({u'yoy_op':  get_value(info.ix[EachStockID]['yoy_op'])})
            dict_stcok.update({u'yoy_tp':  get_value(info.ix[EachStockID]['yoy_tp'])})
            dict_stcok.update({u'yoy_dedu_np':  get_value(info.ix[EachStockID]['yoy_dedu_np'])})
            dict_stcok.update({u'yoy_eps':  get_value(info.ix[EachStockID]['yoy_eps'])})
            dict_stcok.update({u'yoy_roe':  get_value(info.ix[EachStockID]['yoy_roe'])})
            dict_stcok.update({u'growth_assets':  get_value(info.ix[EachStockID]['growth_assets'])})
            dict_stcok.update({u'yoy_equity':  get_value(info.ix[EachStockID]['yoy_equity'])})
            dict_stcok.update({u'growth_bps':  get_value(info.ix[EachStockID]['growth_bps'])})
            dict_stcok.update({u'or_last_year':  get_value(info.ix[EachStockID]['or_last_year'])})
            dict_stcok.update({u'op_last_year':  get_value(info.ix[EachStockID]['op_last_year'])})
            dict_stcok.update({u'tp_last_year':  get_value(info.ix[EachStockID]['tp_last_year'])})
            dict_stcok.update({u'np_last_year':  get_value(info.ix[EachStockID]['np_last_year'])})
            dict_stcok.update({u'eps_last_year':  get_value(info.ix[EachStockID]['eps_last_year'])})
            dict_stcok.update({u'open_net_assets':  get_value(info.ix[EachStockID]['open_net_assets'])})
            dict_stcok.update({u'open_bps':  get_value(info.ix[EachStockID]['open_bps'])})
            dict_stcok.update({u'perf_summary':  get_value(info.ix[EachStockID]['perf_summary'])})
            dict_stcok.update({u'is_audit':  get_value(info.ix[EachStockID]['is_audit'])})
            dict_stcok.update({u'remark':  get_value(info.ix[EachStockID]['remark'])})
            #print(dict_stcok)
            #return
            data_source.append(dict_stcok)

        with model.database.atomic():
            if data_source:
                model.Express.insert_many(data_source).upsert().execute()
        time.sleep(0.3)

def SetDailyBasicPollHuiche():
    stocks = model.StockPool.select()
    for stock in stocks:
        infos = model.DailyBasicPool.select().where(model.DailyBasicPool.ts_code == stock.ts_code).where(model.DailyBasicPool.trade_date > 20090101)
        for info in infos:
            item = model.DailyBasicPool.select(fn.MAX(model.DailyBasicPool.adj_close).alias('max_adj_close')).where(model.DailyBasicPool.ts_code == stock.ts_code).where(model.DailyBasicPool.trade_date < info.trade_date).get()
            if item.max_adj_close is not None:
                huicheVal = 1 - float(info.adj_close)/float(item.max_adj_close)
                print(item)
                print("****")
                print(info.trade_date)
                print(info.adj_close)
                print(item.max_adj_close)
                print(huicheVal)
                print(info.id)
                if huicheVal<0:
                    huicheVal = 0
                q = model.DailyBasicPool.update({model.DailyBasicPool.huiche:huicheVal}).where(model.DailyBasicPool.id == info.id)
                q.execute()
                exit()

        exit()


def get_value(val):
    if val is None:
        return ''
    return val


            #exit()
            #huiche = float(item.max_adj_close)/float(info.adj_close)
            #model.DailyBasicPool.update()
            #print(huiche)
            #表数据更新









