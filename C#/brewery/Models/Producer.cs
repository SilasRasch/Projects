namespace brewery;

public class Producer<T> where T : new()
{
    private Buffer<T> _buffer;
    public int ItemsProduced { get; }

    public Producer(Buffer<T> buffer)
    {
        _buffer = buffer;
        ItemsProduced = 0;
    }

    public void Produce() {
        
    }
}
