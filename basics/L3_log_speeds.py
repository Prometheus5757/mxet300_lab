import L1_log as log
import L2_kinematics as km
import time

while(1):
    pd_currents = km.getPdCurrent() #[pdl, pdr]
    motion_vals = km.getMotion() #[xdot, thetadot]
    log.tmpFile(pd_currents[0],"Left_wheel.txt")
    log.tmpFile(pd_currents[1],"Right_wheel.txt")

    log.tmpFile(motion_vals[0],"enc_for_vel.txt")
    log.tmpFile(motion_vals[1],"enc_ang_vel.txt")
    time.sleep(0.2)