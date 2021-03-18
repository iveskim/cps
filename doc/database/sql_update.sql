alter table daily2  change uuid uuid varchar(20) not null;
alter table daily2  change ts_code ts_code varchar(16) not null;
alter table daily2  change trade_date trade_date varchar(16) not null;
alter table daily2  change open  open varchar(8) ;
alter table daily2  change high  high varchar(8) ;
alter table daily2  change low  low varchar(8) ;
alter table daily2  change close  close varchar(8) ;
alter table daily2  change adj_close  adj_close varchar(16) ;
alter table daily2  change pre_close  pre_close varchar(8) ;
alter table daily2  change adj_close  adj_close varchar(16) ;


