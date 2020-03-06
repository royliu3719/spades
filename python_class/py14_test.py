'''# ------ page. 61 ------
import MySQLdb

db = MySQLdb.connect(host= 'localhost', user= 'dbuser', passwd= 'aabb1234', \
                     db= 'my_demo_db', port= 3306, charset= 'utf8')

cursor = db.cursor()

try:
    sql_str= 'select * from product'
    cursor.execute(sql_str)
    datarows = cursor.fetchall()

    for row in datarows:
        print(row)

except:
    print('unable to fetch data from db')

db.close()

print()
# ------ page. 62 ------
import MySQLdb

db = MySQLdb.connect(host= 'localhost', user= 'dbuser', passwd= 'aabb1234',
                     db= 'my_demo_db', port= 3306, charset= 'utf8')

cursor = db.cursor()
db.autocommit(True)

try:
    sql_str='insert into product(name,price) values(\'{}\',{});'.format('Nokia 7',7000)
    cursor.execute(sql_str)

except Exception as err:
    print('unable to insert data to db')
    print(err)

try:
    sql_str='select * from product;'
    cursor.execute(sql_str)
    datarows = cursor.fetchall()

    for row in datarows:
        print(row)

except:
    print('unable to fetch data from db')
'''

print()
# ------ page. 63 ------
# --- 修改
import MySQLdb

db = MySQLdb.connect(host= 'localhost', user= 'dbuser', passwd= 'aabb1234',
                     db= 'my_demo_db', port= 3306, charset= 'utf8')

cursor = db.cursor()
db.autocommit(True)

try:
    sql_str='update product set name=\'{}\',price={} where pid={} ;'.format('Nokia 6', 3200, 7)
    cursor.execute(sql_str)

except Exception as err:
    print('unable to update data to db')
    print(err)

try:
    sql_str='select * from product;'
    cursor.execute(sql_str)
    datarows = cursor.fetchall()

    for row in datarows:
        print(row)

except:
    print('unable to fetch data from db')
db.close()

# --- 刪除
import MySQLdb

db = MySQLdb.connect(host= 'localhost', user= 'dbuser', passwd= 'aabb1234',
                     db= 'my_demo_db', port= 3306, charset= 'utf8')

cursor = db.cursor()
db.autocommit(True)

try:
    sql_str='delete from product where pid={} ;'.format(8)
    cursor.execute(sql_str)

except Exception as err:
    print('unable to delete data to db')
    print(err)

try:
    sql_str='select * from product;'
    cursor.execute(sql_str)
    datarows = cursor.fetchall()

    for row in datarows:
        print(row)

except:
    print('unable to fetch data from db')
db.close()

print()
# ------ page. 65 ------
# --- 使用 SQLAlchemy 查詢
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Product(Base):
    __tablename__ = 'product'
    pid = Column(Integer, primary_key=True)
    name = Column(String(60))
    price = Column(Integer)

engine = create_engine('mysql://dbuser:aabb1234@localhost/my_demo_db', echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

print('列出全部的產品')
for row in session.query(Product):
    print(row.pid, row.name, row.price)
print('列出價格大於6000的產品')
for row in session.query(Product).filter(Product.price>6000):
    print(row.pid, row.name, row.price)

session.close()

print()
# ------ page. 68 ------
# --- 新增
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Product(Base):
    __tablename__ = 'product'
    pid = Column(Integer, primary_key=True)
    name = Column(String(60))
    price = Column(Integer)

engine = create_engine('mysql://dbuser:aabb1234@localhost/my_demo_db', echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

new_p1 = Product(name='HTC U12', price='4990')
new_p2 = Product(name='HTC U13', price='6990')
new_p3 = Product(name='HTC U14', price='8990')

session.add_all([new_p1,new_p2,new_p3])
session.commit()

print('列出全部的產品')
for row in session.query(Product):
    print(row.pid, row.name, row.price)

session.close()

print()
# --- 修改與刪除
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Product(Base):
    __tablename__ = 'product'
    pid = Column(Integer, primary_key=True)
    name = Column(String(60))
    price = Column(Integer)

engine = create_engine('mysql://dbuser:aabb1234@localhost/my_demo_db', echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

pd = session.query(Product).filter(Product.pid == 11).first()
pd.name = 'HTC Butterfly 4'
pd.price = 3000

pd = session.query(Product).filter(Product.pid == 10).delete()

session.commit()

print('列出全部的產品')
for row in session.query(Product):
    print(row.pid, row.name, row.price)

session.close()








