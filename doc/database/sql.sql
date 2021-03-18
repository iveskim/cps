select * from stockbasic where ts_code in (
select ts_code from (select ts_code,max(convert(close,decimal(18,2))) as maxv, min(convert(close,decimal(18,2))) as minv from daily where trade_date > '20200607' and trade_date< '20200707' group by ts_code order by (max(close)-min(close))/min(close) desc ) b where (maxv/minv)>1.2 )



select ts_code from (select ts_code,max(convert(close,decimal(18,2))) as maxv, min(convert(close,decimal(18,2))) as minv from daily where trade_date > '20200307' and trade_date< '20200707' group by ts_code order by (max(close)-min(close))/min(close) desc ) b where (maxv/minv)>2 ) order by industry

select d.zhangfu,c.*,d.* from stockbasic c , ( select  (a.close-b.close)/b.close as zhangfu,b.*  from (select * from daily where trade_date = 20200707) a , ( select * from daily where trade_date = 20200407) b  where a.ts_code = b.ts_code )d where c.ts_code = d.ts_code order by zhangfu desc


-- alter table daily add key(trade_date)


select * from (select  (a1.close-a2.close)/a2.close as zhangfu,a2.*  from (select * from daily where trade_date = 20191231) a1 , ( select * from daily where trade_date = 20190102) a2  where a1.ts_code = a2.ts_code ) a3 where zhangfu>0.2

select * from (select  (a1.close-a2.close)/a2.close as zhangfu,a2.*  from (select * from daily where trade_date = 20181228) a1 , ( select * from daily where trade_date = 20180102) a2  where a1.ts_code = a2.ts_code ) a3 where zhangfu>0.2



# 修改name
update stockpool a set name = (select name from stockbasic where ts_code = a.ts_code)

# 统计最近一段时间的涨幅

select * from (select (b.close/a.close)*100-100 as zhangfu,  a.ts_code, a.close, b.close as bclose, a.trade_date, b.trade_date as btrade_date from (select * from dailybasicpool where trade_date = '20200709') a, (select * from dailybasicpool where trade_date = '20200811')   b  where a.ts_code = b.ts_code) c, stockbasic d where c.ts_code = d.ts_code order by zhangfu desc

# 处理后复权值
update dailybasicpool a set adj_close = close* (select adj_factor from adjfactor where uuid = a.uuid )

# 最新复权因子
select b.* from (select max(trade_date) maxtd, ts_code from adjfactor group by ts_code )a , adjfactor b where a.ts_code = b.ts_code and a.maxtd = b.trade_date

# 复权关联表
select a.*,b.adj_factor from dailybasicpool a , adjfactor b where a.uuid = b.uuid

# 最近涨幅adj_close
select * from (select (b.adj_close/a.adj_close)*100-100 as zhangfu,  a.ts_code, a.adj_close, b.adj_close as bclose, a.trade_date, b.trade_date as btrade_date from (select * from dailybasicpool where trade_date = '20200601') a, (select * from dailybasicpool where trade_date = '20200819')   b  where a.ts_code = b.ts_code) c, stockbasic d where c.ts_code = d.ts_code order by zhangfu desc





-- select * from (select (b.adj_close/a.adj_close)*100-100 as zhangfu,  a.ts_code, a.adj_close, b.adj_close as bclose, a.trade_date, b.trade_date as btrade_date from (select * from dailybasicpool where trade_date = '20200117') a, (select * from dailybasicpool where trade_date = '20200819')   b  where a.ts_code = b.ts_code) c, stockbasic d where c.ts_code = d.ts_code order by zhangfu desc

-- select * from (select (b.adj_close/a.adj_close)*100-100 as zhangfu,  a.ts_code, a.adj_close, b.adj_close as bclose, a.trade_date, b.trade_date as btrade_date from (select * from dailybasicpool where trade_date = '20190117') a, (select * from dailybasicpool where trade_date = '20200117')   b  where a.ts_code = b.ts_code) c, stockbasic d where c.ts_code = d.ts_code order by zhangfu desc

-- select * from (select (b.adj_close/a.adj_close)*100-100 as zhangfu,  a.ts_code, a.adj_close, b.adj_close as bclose, a.trade_date, b.trade_date as btrade_date from (select * from dailybasicpool where trade_date = '20180117') a, (select * from dailybasicpool where trade_date = '20190117')   b  where a.ts_code = b.ts_code) c, stockbasic d where c.ts_code = d.ts_code order by zhangfu desc

-- select * from (select (b.adj_close/a.adj_close)*100-100 as zhangfu,  a.ts_code, a.adj_close, b.adj_close as bclose, a.trade_date, b.trade_date as btrade_date from (select * from dailybasicpool where trade_date = '20170117') a, (select * from dailybasicpool where trade_date = '20180117')   b  where a.ts_code = b.ts_code) c, stockbasic d where c.ts_code = d.ts_code order by zhangfu desc

-- select * from (select (b.adj_close/a.adj_close)*100-100 as zhangfu,  a.ts_code, a.adj_close, b.adj_close as bclose, a.trade_date, b.trade_date as btrade_date from (select * from dailybasicpool where trade_date = '20160115') a, (select * from dailybasicpool where trade_date = '20170117')   b  where a.ts_code = b.ts_code) c, stockbasic d where c.ts_code = d.ts_code order by zhangfu desc

-- select * from (select (b.adj_close/a.adj_close)*100-100 as zhangfu,  a.ts_code, a.adj_close, b.adj_close as bclose, a.trade_date, b.trade_date as btrade_date from (select * from dailybasicpool where trade_date = '20160115') a, (select * from dailybasicpool where trade_date = '20200819')   b  where a.ts_code = b.ts_code) c, stockbasic d where c.ts_code = d.ts_code order by zhangfu desc
-- select * from (select (b.adj_close/a.adj_close)*100-100 as zhangfu,  a.ts_code, a.adj_close, b.adj_close as bclose, a.trade_date, b.trade_date as btrade_date from (select * from dailybasicpool where trade_date = '20150115') a, (select * from dailybasicpool where trade_date = '20160115')   b  where a.ts_code = b.ts_code) c, stockbasic d where c.ts_code = d.ts_code order by zhangfu desc
-- select * from (select (b.adj_close/a.adj_close)*100-100 as zhangfu,  a.ts_code, a.adj_close, b.adj_close as bclose, a.trade_date, b.trade_date as btrade_date from (select * from dailybasicpool where trade_date = '20140115') a, (select * from dailybasicpool where trade_date = '20150115')   b  where a.ts_code = b.ts_code) c, stockbasic d where c.ts_code = d.ts_code order by zhangfu desc
-- select * from (select (b.adj_close/a.adj_close)*100-100 as zhangfu,  a.ts_code, a.adj_close, b.adj_close as bclose, a.trade_date, b.trade_date as btrade_date from (select * from dailybasicpool where trade_date = '20130115') a, (select * from dailybasicpool where trade_date = '20140115')   b  where a.ts_code = b.ts_code) c, stockbasic d where c.ts_code = d.ts_code order by zhangfu desc
-- select * from (select (b.adj_close/a.adj_close)*100-100 as zhangfu,  a.ts_code, a.adj_close, b.adj_close as bclose, a.trade_date, b.trade_date as btrade_date from (select * from dailybasicpool where trade_date = '20120116') a, (select * from dailybasicpool where trade_date = '20130115')   b  where a.ts_code = b.ts_code) c, stockbasic d where c.ts_code = d.ts_code order by zhangfu desc
-- select * from (select (b.adj_close/a.adj_close)*100-100 as zhangfu,  a.ts_code, a.adj_close, b.adj_close as bclose, a.trade_date, b.trade_date as btrade_date from (select * from dailybasicpool where trade_date = '20110117') a, (select * from dailybasicpool where trade_date = '20120116')   b  where a.ts_code = b.ts_code) c, stockbasic d where c.ts_code = d.ts_code order by zhangfu desc
select * from (select (b.adj_close/a.adj_close)*100-100 as zhangfu,  a.ts_code, a.adj_close, b.adj_close as bclose, a.trade_date, b.trade_date as btrade_date from (select * from dailybasicpool where trade_date = '20090505') a, (select * from dailybasicpool where trade_date = '20110117')   b  where a.ts_code = b.ts_code) c, stockbasic d where c.ts_code = d.ts_code order by zhangfu desc

# 创新高股
select * from (select max(close) as max_close ,ts_code from dailybasic  where trade_date < 20200720  group by ts_code)a , (select max(close) as after_max_close,ts_code as after_ts_code from dailybasic  where trade_date > 20200720  group by ts_code)b where a.ts_code = b.after_ts_code and a.max_close<b.after_max_close

select * from stockbasic where ts_code in(select a.ts_code from (select max(adj_close) as max_close ,ts_code from daily2  where trade_date < 20200819  group by ts_code)a , (select max(adj_close) as after_max_close,ts_code as after_ts_code from daily2  where trade_date > 20200819  group by ts_code)b where a.ts_code = b.after_ts_code and a.max_close<b.after_max_close)


# 修改表字段为两个字段拼接
update daily a set uuid = CONCAT(ts_code, trade_date)

#设置复权值

#计算涨幅
select d.ts_code,d.`name`,c.zhangfu from stockbasic d, (select a.*,(a.adj_close-b.adj_close)/b.adj_close zhangfu  from daily3 a,daily2017 b where a.ts_code = b.ts_code )c where d.ts_code = c.ts_code order by zhangfu desc




# 计算股票池中的涨幅
select sum(zhangfu)/11 from (select d.*,c.zhangfu from stockbasic d, (select a.*,(a.adj_close-b.adj_close)/b.adj_close zhangfu  from daily20200327 a,daily20200305 b where a.ts_code = b.ts_code )c where d.ts_code = c.ts_code and d.ts_code in(select ts_code from stockpool where is_del=0) order by zhangfu desc ) h



# 计算组合涨幅
delete from daily20200327;
delete from daily20200305;
insert into daily20200327 select * from daily2 where trade_date = 20200820;
insert into daily20200305 select * from daily2 where trade_date = 20150120;
select sum(zhangfu)/count(*),count(*) from (select d.*,c.zhangfu from stockbasic d, (select a.*,(a.adj_close-b.adj_close)/b.adj_close zhangfu  from daily20200327 a,daily20200305 b where a.ts_code = b.ts_code )c where d.ts_code = c.ts_code and d.ts_code in(select ts_code from stockpool where is_del=0) order by zhangfu desc ) h