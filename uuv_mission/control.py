class PDController:
    """
    Proportional-Derivative (PD) controller for depth regulation.
    """
    def __init__(self, Kp=0.15, Kd=0.6):
        self.Kp = Kp  # proportional gain
        self.Kd = Kd  # derivative gain
        self.prev_error = 0.0  # store previous error for derivative term

    def update(self, reference, output):
        """
        Compute the control action.

        Parameters:
        - reference: desired depth (r[t])
        - output: current depth (y[t])

        Returns:
        - u: control input
        """
        error = reference - output
        derivative = error - self.prev_error
        u = self.Kp * error + self.Kd * derivative
        self.prev_error = error
        return u
    
    def reset(self):
        """Reset controller’s internal state so a new run starts clean."""
        self.prev_error = 0.0
        
        

    
    