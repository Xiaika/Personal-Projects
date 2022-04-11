public class Ballot
{
    private String name, vote;
    private int age, id;
    boolean valid = true;

    public Ballot(String name, int age, int id, String vote)
    {
        this.name = name;
        this.age = age;
        this.id = id;
        this.vote = vote;
    }

    public String getName() { return name; }
    public int getId() { return id; }
    public int getAge() { return age; }
    public String getVote() { return vote; }

    public void invalidate() { this.valid = false; }

    @Override
    public String toString()
    { return "Ballot [name=" + this.name + ", age=" + this.age + ", id=" + this.id + ", vote=" + this.vote + "]"; }

}
