from peewee import *
import datetime
import settings


if settings.DBENGINE.lower() == 'mysql':
    database = MySQLDatabase(
        settings.DBNAME,
        host=settings.DBHOST,
        port=settings.DBPORT,
        user=settings.DBUSER,
        passwd=settings.DBPASSWORD,
        charset='utf8',
        use_unicode=True,
    )

elif settings.DBENGINE.lower() == 'sqlite3':
    database = SqliteDatabase(settings.DBNAME)

elif settings.DBENGINE.lower() == 'postgresql':
    database = PostgresqlDatabase(
        settings.DBNAME,
        user=settings.DBUSER,
        password=settings.DBPASSWORD,
        host=settings.DBHOST,
        charset='utf8',
        use_unicode=True,
    )

else:
    raise AttributeError("Please setup datatbase at settings.py")


class BaseModel(Model):

    class Meta:
        database = database


class StockBasic(BaseModel):
    id = BigIntegerField(primary_key=True)
    ts_code = CharField(default='')
    symbol = CharField(default='', null=True)
    name = CharField(default='', null=True)
    area = CharField(default='', null=True)
    industry = CharField(default='', null=True)
    fullname = CharField(default='', null=True)
    enname = CharField(default='', null=True)
    market = CharField(default='', null=True)
    exchange = CharField(default='', null=True)
    curr_type = CharField(default='', null=True)
    list_status = CharField(default='', null=True)
    list_date = CharField(default='', null=True)
    delist_date = CharField(default='', null=True)
    is_hs = CharField(default='', null=True)
    create_time = DateTimeField(default=datetime.datetime.now)

class Daily(BaseModel):
    id = BigIntegerField(primary_key=True)
    ts_code = CharField(default='')
    trade_date = CharField(default='', null=True)
    open = CharField(default='', null=True)
    high = CharField(default='', null=True)
    low = CharField(default='', null=True)
    close = CharField(default='', null=True)
    pre_close = CharField(default='', null=True)
    change = CharField(default='', null=True)
    pct_chg = CharField(default='', null=True)
    vol = CharField(default='', null=True)
    amount = CharField(default='', null=True)
    create_time = DateTimeField(default=datetime.datetime.now)

class DailyBasic(BaseModel):
    id = BigIntegerField(primary_key=True)
    ts_code = CharField(default='')
    trade_date = CharField(default='', null=True)
    close = CharField(default='', null=True)
    turnover_rate = CharField(default='', null=True)
    turnover_rate_f = CharField(default='', null=True)
    volume_ratio = CharField(default='', null=True)
    pe = CharField(default='', null=True)
    pe_ttm = CharField(default='', null=True)
    pb = CharField(default='', null=True)
    ps = CharField(default='', null=True)
    ps_ttm = CharField(default='', null=True)
    dv_ratio = CharField(default='', null=True)
    dv_ttm = CharField(default='', null=True)
    total_share = CharField(default='', null=True)
    float_share = CharField(default='', null=True)
    free_share = CharField(default='', null=True)
    total_mv = CharField(default='', null=True)
    circ_mv = CharField(default='', null=True)
    create_time = DateTimeField(default=datetime.datetime.now)


class StockPool(BaseModel):
    id = BigIntegerField(primary_key=True, unique=True,
                         constraints=[SQL('AUTO_INCREMENT')])
    ts_code = CharField(default='', unique=True)
    create_time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        indexs = (('ts_code', 'trade_date'), True)

class DailyPool(BaseModel):
    id = BigIntegerField(primary_key=True, unique=True,
                         constraints=[SQL('AUTO_INCREMENT')])
    uuid = CharField(default='', null=True)
    ts_code = CharField(default='')
    trade_date = CharField(default='', null=True)
    open = CharField(default='', null=True)
    high = CharField(default='', null=True)
    low = CharField(default='', null=True)
    close = CharField(default='', null=True)
    pre_close = CharField(default='', null=True)
    change = CharField(default='', null=True)
    pct_chg = CharField(default='', null=True)
    vol = CharField(default='', null=True)
    amount = CharField(default='', null=True)
    create_time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        indexs = (('ts_code', 'trade_date'), True)

class DailyBasicPool(BaseModel):
    id = BigIntegerField(primary_key=True, unique=True,
                           constraints=[SQL('AUTO_INCREMENT')])
    uuid = CharField(default='', null=True)
    ts_code = CharField(default='')
    trade_date = CharField(default='', null=True)
    close = CharField(default='', null=True)
    adj_close = CharField(default='', null=True)
    huiche = CharField(default='', null=True)
    turnover_rate = CharField(default='', null=True)
    turnover_rate_f = CharField(default='', null=True)
    volume_ratio = CharField(default='', null=True)
    pe = CharField(default='', null=True)
    pe_ttm = CharField(default='', null=True)
    pb = CharField(default='', null=True)
    ps = CharField(default='', null=True)
    ps_ttm = CharField(default='', null=True)
    dv_ratio = CharField(default='', null=True)
    dv_ttm = CharField(default='', null=True)
    total_share = CharField(default='', null=True)
    float_share = CharField(default='', null=True)
    free_share = CharField(default='', null=True)
    total_mv = CharField(default='', null=True)
    circ_mv = CharField(default='', null=True)
    create_time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        indexs = (('ts_code', 'trade_date'), True)

class AdjFactor(BaseModel):
    id = BigIntegerField(primary_key=True, unique=True,
                           constraints=[SQL('AUTO_INCREMENT')])
    uuid = CharField(default='', null=True)
    ts_code = CharField(default='')
    trade_date = CharField(default='', null=True)
    adj_factor = CharField(default='', null=True)
    create_time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        indexs = (('ts_code', 'trade_date'), True)

class AdjFactor2(BaseModel):
    id = BigIntegerField(primary_key=True, unique=True,
                           constraints=[SQL('AUTO_INCREMENT')])
    uuid = CharField(default='', null=True)
    ts_code = CharField(default='')
    trade_date = CharField(default='', null=True)
    adj_factor = CharField(default='', null=True)
    create_time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        indexs = (('ts_code', 'trade_date'), True)

# class ProBar(BaseModel):
#     id = BigIntegerField(primary_key=True, unique=True,
#                            constraints=[SQL('AUTO_INCREMENT')])
#     uuid = CharField(default='', null=True)
#     ts_code = CharField(default='')
#     trade_date = CharField(default='', null=True)
#     adj_factor = CharField(default='', null=True)
#     create_time = DateTimeField(default=datetime.datetime.now)
#
#     class Meta:
#         indexs = (('ts_code', 'trade_date'), True)


# todo
class Income(BaseModel):
    id = BigIntegerField(primary_key=True, unique=True,
                           constraints=[SQL('AUTO_INCREMENT')])
    uuid = CharField(default='', null=True)
    ts_code = CharField(default='')
    ann_date = CharField(default='', null=True)
    f_ann_date = CharField(default='', null=True)
    adj_close = CharField(default='', null=True)
    huiche = CharField(default='', null=True)
    turnover_rate = CharField(default='', null=True)
    turnover_rate_f = CharField(default='', null=True)
    volume_ratio = CharField(default='', null=True)
    pe = CharField(default='', null=True)
    pe_ttm = CharField(default='', null=True)
    pb = CharField(default='', null=True)
    ps = CharField(default='', null=True)
    ps_ttm = CharField(default='', null=True)
    dv_ratio = CharField(default='', null=True)
    dv_ttm = CharField(default='', null=True)
    total_share = CharField(default='', null=True)
    float_share = CharField(default='', null=True)
    free_share = CharField(default='', null=True)
    total_mv = CharField(default='', null=True)
    circ_mv = CharField(default='', null=True)
    create_time = DateTimeField(default=datetime.datetime.now)

class Forecast(BaseModel):
    id = BigIntegerField(primary_key=True, unique=True,
                           constraints=[SQL('AUTO_INCREMENT')])
    uuid = CharField(default='', null=True)
    ts_code = CharField(default='')
    ann_date = CharField(default='', null=True)
    end_date = CharField(default='', null=True)
    type = CharField(default='', null=True)
    p_change_min = CharField(default='', null=True)
    p_change_max = CharField(default='', null=True)
    net_profit_min = CharField(default='', null=True)
    net_profit_max = CharField(default='', null=True)
    last_parent_net = CharField(default='', null=True)
    first_ann_date = CharField(default='', null=True)
    summary = CharField(default='', null=True)
    create_time = DateTimeField(default=datetime.datetime.now)

class Express(BaseModel):
    id = BigIntegerField(primary_key=True, unique=True,
                           constraints=[SQL('AUTO_INCREMENT')])
    uuid = CharField(default='', null=True)
    ts_code = CharField(default='')
    ann_date = CharField(default='', null=True)
    end_date = CharField(default='', null=True)
    revenue = CharField(default='', null=True)
    operate_profit = CharField(default='', null=True)
    total_profit = CharField(default='', null=True)
    n_income = CharField(default='', null=True)
    total_assets = CharField(default='', null=True)
    total_hldr_eqy_exc_min_int = CharField(default='', null=True)
    diluted_eps = CharField(default='', null=True)
    diluted_roe = CharField(default='', null=True)
    yoy_net_profit = CharField(default='', null=True)
    bps = CharField(default='', null=True)
    yoy_sales = CharField(default='', null=True)
    yoy_op = CharField(default='', null=True)
    yoy_tp = CharField(default='', null=True)
    yoy_dedu_np = CharField(default='', null=True)
    yoy_eps = CharField(default='', null=True)
    yoy_roe = CharField(default='', null=True)
    growth_assets = CharField(default='', null=True)
    yoy_equity = CharField(default='', null=True)
    growth_bps = CharField(default='', null=True)
    or_last_year = CharField(default='', null=True)
    op_last_year = CharField(default='', null=True)
    tp_last_year = CharField(default='', null=True)
    np_last_year = CharField(default='', null=True)
    eps_last_year = CharField(default='', null=True)
    open_net_assets = CharField(default='', null=True)
    open_bps = CharField(default='', null=True)
    perf_summary = CharField(default='', null=True)
    is_audit = CharField(default='', null=True)
    remark = CharField(default='', null=True)
    create_time = DateTimeField(default=datetime.datetime.now)


def database_init():
    database.connect()
    database.create_tables(
        [StockBasic, Daily, DailyBasic, StockPool, DailyPool, DailyBasicPool, AdjFactor, AdjFactor2, Express], safe=True)
    database.close()
