class Pid():
    """classic controller:PID
    p:proportion
    i:integral
    d:differential

    """

    def __init__(self):
        """init  a pid model"""
        self.kp=0.0
        self.ki=0.0
        self.kd=0.0
        self.alteration_times=1000

    def setparameters(self,kp,ki,kd):
        """set pid parameters"""
        self.kp=kp
        self.ki=ki
        self.kd=kd
        
    def tracksignal(self,ideal):
        """function as track the ideal output by alterating the error"""
        ideal_output=ideal
        actual_output=0.0
        error=0.0
        error_sum=0.0
        error_difference=0.0

        for i in range(self.alteration_times):
            #pid dispersed expression
            error_difference=ideal_output-actual_output-error
            error=ideal_output-actual_output
            error_sum+=error
            actual_output=self.kp*error+self.ki*error_sum+self.kd*error_difference
            print(i,actual_output)

#test
pid=Pid()
pid.setparameters(0.2,0.015,0.2)
pid.tracksignal(200)