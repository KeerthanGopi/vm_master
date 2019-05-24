# INBUILT
import multiprocessing

# MODULES
import to_send as sender
import back_changed as reciever

try:
   # rt = Thread(target = reciever.setup)
   # st = Thread(target = sender.setup)
   # rt.setDaemon(True)
   # rt.start()
   # st.start()
   #devnull = open(os.devnull, "wb")
   #Popen(["nohup", "python3 back_changed.py"], stdout = devnull, stderr = devnull)
   #Popen("python3 back_changed.py", shell = True)
   global rt
   queue = multiprocessing.Queue()
   queue.put(False)
   rt = multiprocessing.Process(target = reciever.setup, args = (queue, ))
   rt.start()
   sender.setup(queue)

except KeyboardInterrupt:
    print("Thank You")

finally:
    rt.join()
    print('Bye')
