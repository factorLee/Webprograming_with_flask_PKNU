from models import db, Puppy, Owner, Toy

db.create_all()

rufus = Puppy("Rufus")
fido = Puppy("Fido")



rufus = Puppy.query.filter_by(name='Rufus').all()[0]

# Create an owner to Rufus
jose = Owner("Jose", rufus.id)

# Give some Toys to  Rufus
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

#Commit these changes to the database
db.session.add_all([rufus,fido])
db.session.add_all([jose,toy1,toy2])
db.session.commit()

# Let' now grab rufus again after these addions
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

#show toys
print(rufus.report_toys())