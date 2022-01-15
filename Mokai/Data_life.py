from collections import UserDict
from threading import RLock, Lock
import time
#数据时效模块
# 使用方法
'''
ttl_dict = TTLDict()
ttl_dict.setex('变量名', 摧毁时间, 数据)
ttl_dict.ttl('a') 剩余时间
(ttl_dict['a']) 查询此变量名的数据

'''


class TTLDict(UserDict):
    def __init__(self, *args, **kwargs):
        self._rlock = RLock()
        self._lock = Lock()

        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<TTLDict@%#08x; %r;>' % (id(self), self.data)

    def expire(self, key, ttl, now=None):
        if now is None:
            now = time.time()
        with self._rlock:
            _expire, value = self.data[key]
            self.data[key] = (now + ttl, value)

    def ttl(self, key, now=None):
        if now is None:
            now = time.time()
        with self._rlock:
            expire, _value = self.data[key]
            if expire is None:
                # Persistent keys
                return -1
            elif expire <= now:
                # Expired keys
                del self[key]
                return -2
            return expire - now

    def setex(self, key, ttl, value):
        with self._rlock:
            expire = time.time() + ttl
            self.data[key] = (expire, value)

    def __len__(self):
        with self._rlock:
            for key in list(self.data.keys()):
                self.ttl(key)
            return len(self.data)

    def __iter__(self):
        with self._rlock:
            for k in self.data.keys():
                ttl = self.ttl(k)
                if ttl != -2:
                    yield k

    def __setitem__(self, key, value):
        with self._lock:
            self.data[key] = (None, value)

    def __delitem__(self, key):
        with self._lock:
            del self.data[key]

    def __getitem__(self, key):
        with self._rlock:
            self.ttl(key)
            return self.data[key][1]