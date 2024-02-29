namespace brewery;

public class Bottle
{
    private static int _nextId = 0;
    public int Id { get; set; }
    public bool Clean { get; set; }
    public bool Full { get; set; }
    public bool Capped { get; set; }

    public Bottle()
    {
        Id = _nextId++;
        Clean = false;
        Full = false;
        Capped = false;
    }
}
