#多进程的使用
from multiprocessing import Pool
pool = Pool(processes=4) #创建线程池
pool.map(func,iterable[,chunksize])