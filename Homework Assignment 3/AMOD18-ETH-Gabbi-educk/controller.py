import math
import numpy as np


class Controller():

    def __init__(self):

        # Set your parameters here
        # Gains for controller
        self.k_P = 2.5
        self.k_D = 1.4
        self.k_I = 0.1
        self.err = 0
        self.errInt = 0

    # Inputs:   d_est   Estimation of distance from lane center (positve when
    #                   offset to the left of driving direction) [m]
    #           phi_est Estimation of angle of bot (positive when angle to the
    #                   left of driving direction) [rad]
    #           d_ref   Reference of d (for lane following, d_ref = 0) [m]
    #           v_ref   Reference of velocity [m/s]
    #           t_delay Delay it took from taking image up to now [s]
    #           dt_last Time it took from last processing to current [s]

    # Output:   v_out       forward linear velocity of Duckiebot [m/s]
    #           omega_out   angular velocity of Duckiebot [rad/s]
    def getControlOutput(self, d_est, phi_est, d_ref, phi_ref, v_ref, t_delay, dt_last):

        # Do your calculations here

        # Calculate the output y
        ref =   (6 * d_ref + 1 * phi_ref)
        y =     (6 * d_est + 1 * phi_est)
        err = ref - y
	
	# Naive P-Controller
        C_P = self.k_P * err


        # PD
        C_D = self.k_D * (err-self.err)/dt_last
        self.err = err

        # PI
        self.errInt = err + self.errInt
        C_I = self.k_I * self.errInt

        omega = C_P + C_D + C_I

        # Declaring return values
        omega_out = omega
        v_out = v_ref


        return (v_out, omega_out)
                                                                                                                                    56,9          Bot
                                                                                                                                    1,9           Top

