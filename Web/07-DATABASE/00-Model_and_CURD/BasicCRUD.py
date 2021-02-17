from BasicModelApp import db, Puppy

######## 데이터베이스/테이블 생성 ######## 
#db.create_all()

######### 데이터(행) 한개 삽입 ######## 
#my_puppy = Puppy('Rufus', 5)
#db.session.add(my_puppy)
#db.session.commit()
#
#
######### 테이블 내에 레코드(행) 읽기 ######## 
#all_puppies = Puppy.query.all()
#print(all_puppies)
#
########## 다중삽입 ######## 
#db.session.add_all([
#    Puppy('LEE', 3),
#    Puppy('Bach', 5),
#    Puppy('Sammy', 7)
#    ])
#db.session.commit()

#all_puppies = Puppy.query.all()
#print(all_puppies)

######### 필터링 ######## 
puppy_sam = Puppy.query.filter_by(name='Bach').all()
print(puppy_sam) 

########## 원하는 데이터를 골라서 수정 ######## 
#first_puppy=Puppy.query.get(1) # 테이블 내의 첫번째 데이터를 골라라
#first_puppy.age = 10 # 첫번째 레코드(행)의 나이를 10으로 변경
#db.session.add(first_puppy)# 데이터베이스에서 수정(덮어씌우기)
#db.session.commit() #데이터베이스에서 커밋하기
#print(Puppy.query.all())

########## 원하는 데이터를 골라서 삭제 ######## 
Puppy.query.filter_by(name='Rufus').delete()
db.session.commit()
print(Puppy.query.all())

# https://docs.sqlalchemy.org/en/13/orm/tutorial.html