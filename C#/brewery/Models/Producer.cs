namespace brewery;

public class Producer<T> where T : new()
{
    private BoundedBuffer<T> _buffer;
    public int ItemsProduced { get; }

    public Producer(BoundedBuffer<T> buffer)
    {
        _buffer = buffer;
        ItemsProduced = 0;
    }

    public void Produce() {
        
    }
}
