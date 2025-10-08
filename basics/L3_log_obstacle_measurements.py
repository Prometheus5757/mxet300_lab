import L1_log as log
import L1_lidar as lidar
import L2_vector as vec
import time

if __name__ == "__main__":
    lidarsensor = lidar.Lidar() #Create a Lidar instance

    # Connect to the Lidar device
    lidarsensor.connect()

    # Start the Lidar thread
    processor = lidarsensor.run()
    time.sleep(1)  # Allow some time for the thread to start

    # Continuously retrieve and print the Lidar data
    try:
        while True:
            time.sleep(0.5)
            lidar_vals = lidarsensor.get() #[distance, angle]
            vector_vals = vec.getNearest(lidar_vals)
            vec_components = vec.polar2cart(*vector_vals) #[x,y] in cartesian
            log.tmpFile(vector_vals[0],"distance.txt")
            log.tmpFile(vector_vals[1],"angle.txt")
            
            log.tmpFile(vec_components[0],"x_comp.txt")
            log.tmpFile(vec_components[1],"y_comp.txt")
            
    except KeyboardInterrupt:
        print("Stopping Lidar...")
    finally:
        # Kill the Lidar thread when done
        lidarsensor.kill(processor)