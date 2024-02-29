namespace brewery;

public class Bottle
{
    public int Id { get; set; }
    public bool Clean { get; set; }
    public bool Full { get; set; }
    public bool Capped { get; set; }

    public Bottle()
    {
        Clean = false;
        Full = false;
        Capped = false;
    }
}
