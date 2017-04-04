#create a class Car that can be used to instatiate various objects
class Car(object):
    def __init__( self, name='General', model='GM', car_type='saloon' ):
        self.name=name
        self.model=model
        self.car_type=car_type
        num_of_wheels=4
        is_saloon=True


        #number of doors
        if (name=='Koenigsegg' and model=='Agera R') or (name=='porshe' and model=='911 Turbo'):
            self.num_of_doors=2
            num_of_wheels==4
        else:
            self.num_of_doors=4

        # Number of Wheels
            if (self.car_type == 'trailer'):
                self.num_of_wheels = 8
            else:
                self.num_of_wheels = 4

        # is_saloon Car
        def is_saloon(self):
            if self.car_type == 'saloon':
                return True
            else:
                return False

        # Car Speed
        def drive(self, accelerate):
            if (self.car_type == 'trailer'):
                self.speed = accelerate * 11
                return self
            else:
                if(accelerate !=0):
                    self.speed = 10 ** accelerate
                else:
                    self.speed = 10 * accelerate
                return self
