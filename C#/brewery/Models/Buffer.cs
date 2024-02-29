namespace brewery;

public class BoundedBuffer <T> where T : new()
{
    private Queue<T> _queue;
    public int Count { get { return _queue.Count; }}
    public int CountInit { get; }
    private int _limit { get; set; }
    private Mutex _mutex;
    private Semaphore _empty;
    private Semaphore _full;

    public BoundedBuffer(int limit)
    {
        _limit = limit;
        _queue = new Queue<T>(_limit);
        _mutex = new Mutex();
        _empty = new Semaphore(0, _limit);
        _full = new Semaphore(_limit, _limit);
    }

    public void Insert(T obj) {
        _full.WaitOne();
        _mutex.WaitOne();

        _queue.Enqueue(obj);

        _mutex.ReleaseMutex();
        _empty.Release();
    }
    
    public void InsertRange(IEnumerable<T> objects) {
        foreach (T obj in objects) {
            Insert(obj);
        }
    }

    public T Take() {
        _empty.WaitOne();
        _mutex.WaitOne();

        T item = _queue.Dequeue();

        _full.Release();
        _mutex.ReleaseMutex();

        return item;
    }

    public IEnumerable<T> TakeRange(int range) {
        List<T> tmp = new List<T>();
        
        for (int i = 0; i < range; i++) {
            tmp.Add(Take());
        }

        return tmp;
    }
}
