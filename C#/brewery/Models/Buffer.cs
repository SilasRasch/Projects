namespace brewery;

public class Buffer <T> where T : new()
{
    private Queue<T> _queue;
    public int Count { get { return _queue.Count; }}
    public int CountInit { get; }
    public int Limit { get; set; }

    public Buffer()
    {
        _queue = new Queue<T>();

    }

    public void Insert(T obj) {
        if (Count < Limit) {
                _queue.Enqueue(obj);
        }
    }
    
    public void InsertRange(IEnumerable<T> objects) {
        foreach (T obj in objects) {
            Insert(obj);
        }
    }

    public T Take() {
        if (Count == 0)
            throw new InvalidOperationException("Queue is empty");
        return _queue.Dequeue();
    }

    public IEnumerable<T> TakeRange(int range) {
        List<T> tmp = new List<T>();
        
        for (int i = 0; i < range; i++) {
            tmp.Add(Take());
        }

        return tmp;
    }
}
