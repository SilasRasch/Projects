using brewery;

System.Console.WriteLine("Starting");
System.Console.WriteLine();

BoundedBuffer<Bottle> buffer = new BoundedBuffer<Bottle>(3);

buffer.Insert(new Bottle());
System.Console.WriteLine(buffer.Count);
buffer.Insert(new Bottle());
System.Console.WriteLine(buffer.Count);
buffer.Take();
System.Console.WriteLine(buffer.Count);
buffer.Take();
System.Console.WriteLine(buffer.Count);
buffer.Take();
System.Console.WriteLine(buffer.Count);