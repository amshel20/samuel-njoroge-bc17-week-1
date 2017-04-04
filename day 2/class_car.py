#create a class Car that can be used to instatiate various objects
class Car(object):
    def __init__( self, name='General', model='GM',  Car_type='saloon'):
        self.name=name
        self.model=model
        num_of_doors=4
        num_of_wheels=4
        speed=0


        #number of doors
        if (Car.name=='koenisseg' and Car.model=='Agera R') or (Car.name=='porshe' and Car.model=='911 turbo'):
            self.num_of_doors=2
        else:
            self.num_of_doors=4

        #number of wheels
        if Car_type!='saloon':
            self.num_of_wheels=8
        else:
            self.num_of_wheels=4

        #Car speed
        def drive(N):
            if Car.drive(0) and Car_type=='trailer':
                Car.speed=0
            elif Car.drive(7) and Car_type=='trailer':
                Car.speed=77

            if Car.name=='Mercedes' and Car.drive(0):
                Car.speed=0
            elif Car.name=='Mercedes' and Car.drive(3):
                Car.speed=1000
